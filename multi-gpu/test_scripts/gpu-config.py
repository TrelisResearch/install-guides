## By Trelis Research - learn more at Trelis.com/ADVANCED-fine-tuning
# Trelis GPU Configuration Guide Decision Tree
# |
# ├── Enter Model Size (in billions of parameters)
# |
# ├── Enter VRAM per GPU (e.g. 80 for A100 80GB)
# |
# ├── Choose Fine-Tuning Approach
# │   ├── a) 4-bit with LoRA (moderate quality, fewer GPUs, lower cost)
# │   ├── b) 16-bit with LoRA (good quality, moderate GPUs, moderate cost)
# │   └── c) Full fine-tuning in 16-bit (best quality, many GPUs, high cost)
# |
# ├── Calculate Estimated VRAM Required
# │   - Full fine-tuning in 16-bit (option 'c'):
# │       2 bytes (16-bit) for each parameter
# │     + 2 bytes (16-bit) for gradients for each parameter (one gradient per param)
# │     + 4x2 bytes (32-bit) x 2 optimiser states (m, v) per parameter [for Adam optimiser]
# │     + 4 bytes (32-bit) for each parameter, to store the model in 32-bits for the optimiser!!!
# │     = 16 bytes per parameter
# │   - For 16-bit with LoRA (option 'b')
# │       LoRA matrices are ~1-2% of full matrices = rank 32 / hidden dimension 2048.
# │       2 bytes (16-bit) for each parameter
# │       gradients only required for a tiny number of parameters
# │       optimizer only required for a tiny number of parameters
# │     = 2 bytes per parameter
# │   - For 4-bit with LoRA (option 'a'), the factor is 1.25.
# │       LoRA matrices are ~1-2% of full matrices = rank 32 / hidden dimension 2048.
# │       0.5 bytes (4-bit) for each parameter
# │       gradients only required for a tiny number of parameters
# │       optimizer only required for a tiny number of parameters
# │     = 0.5 bytes per parameter
# |
# ├── Calculate Minimum Number of GPUs Required
# │   = VRAM Required / VRAM per GPU
# │   e.g. 160 GB required / 80 GB = 2 GPUs
# |
# └── GPU Setup:
#     │   Depends on:
#     ├── a) Does the model fit on one GPU?
#     │   └── For speed: Use Distributed Data Parallel (DDP) on multiple GPUs.
#     │   └── For minimum-VRAM: Use device_map='auto' and 'python train.py' (or Unsloth).
#     │
#     ├── b) Is the model too big for one GPU?
#     │   ├── Fpr speed: Use Fully Sharded Data Parallel (FSDP) on multiple GPUs.
#     │   └── For minimum-VRAM: Use device_map='auto' and 'python train.py' (or Unsloth).

# Additional Tips:
# - Use gradient_checkpointing to reduce VRAM requirements.
# - Start with a batch size of 1, and increase the number of GPUs until you don't run out of memory (CUDA error).
# - Then, double the batch size until you run out of memory (OOM) and pare back the batch size.

import math

def calculate_vram_requirements(model_size_billion_params, tuning_option):
    """Calculate the VRAM requirements based on the tuning option."""
    model_size_bytes = model_size_billion_params * 1e9  # Convert billion to actual number of parameters
    if tuning_option == 'a':
        # Fine-tuning in 4-bit with LoRA
        # 0.5 bytes per parameter
        return model_size_bytes * 0.5 / 1e9  # Convert bytes back to GB
    elif tuning_option == 'b':
        # Fine-tuning in 16-bit with LoRA
        # gradients and optimizer states only for a tiny number of parameters
        # Assuming LoRA matrices are ~1-2% of full matrices = 2 bytes per parameter
        return model_size_bytes * 2 / 1e9  # Convert bytes back to GB
    elif tuning_option == 'c':
        # Full fine-tuning in 16-bit
        # 16 bytes per parameter
        return model_size_bytes * 16 / 1e9  # Convert bytes back to GB
    else:
        raise ValueError("Invalid tuning option selected.")

def main():
    print("Welcome to the Trelis GPU Configuration Guide!")
    
    model_size_billion_params = float(input("Enter your model size in billions of parameters: "))
    tuning_option = input("\nChoose your fine-tuning approach:\n a) 4-bit with LoRA (lowest cost, moderate quality)\n b) 16-bit with LoRA (moderate cost, high quality)\n c) Full fine-tuning in 16-bit (high cost, highest quality - only needed for long trainings >10,000 rows of data)\nYour choice (a/b/c): ").lower()
    
    estimated_vram = calculate_vram_requirements(model_size_billion_params, tuning_option)
    print(f"\nEstimated VRAM required: {estimated_vram:.2f} GB")
    
    gpu_vram = float(input("Enter amount of VRAM you have per GPU: "))
    min_gpus = estimated_vram / gpu_vram
    print(f"\nMinimum number of GPUs required: {max(1, math.ceil(min_gpus))}")
    
    # GPU setup advice
    if min_gpus <= 1:
        speed_preference = input("Do you wish to maximise speed or minimize GPUs (SPEED, GPUs)? ").lower()
        if speed_preference == 'speed':
            print("\nRecommendation: Use Distributed Data Parallel (DDP) and increase the number of GPUs and batch size for more speed.")
        else:
            print("\nRecommendation: Use Unsloth for minimum-VRAM.")
    else:
        minimize_choice = input("Do you wish to minimize the number of GPUs or training time (GPUs or TIME)? ").lower()
        if minimize_choice == 'gpus':
            print("\nRecommendation: Use Unsloth for minimum-VRAM.")
        else:
            print("\nRecommendation: Use Fully Sharded Data Parallel (FSDP) and increase the number of GPUs and batch size for speed.")

if __name__ == "__main__":
    main()