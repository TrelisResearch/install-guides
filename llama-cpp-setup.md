# Llama.cpp Installation Guide

## Warnings / Expectations
- Macs with M1 or M2 chips will deliver 10+ tokens/second, even with only 8 GB RAM.
- Macs with an intel chip can deliver about 2 tokens/second. That's interesting to test, but slow to use.
- Windows computers:
    - Tedious to install - involves multiple packages to set up CPU or GPU acceleration (w64devkit + OpenBLAS).
    - Slow to run, as low as <0.1 tokens per second, depending on CPU/GPU.

## Recommendations
1. If you have an M1/M2 Mac, install/run on Mac using the instructions below OR in a Jupyter Notebook with automated installation. ([paid](https://buy.stripe.com/dR65l6f4p95V7AI6oA)).
2. Otherwise, run in Google Colab ([free notebook here](https://colab.research.google.com/drive/1u8x41Jx8WWtI-nzHOgqTxkS3Q_lcjaSX?usp=sharing)).

## Installation

1. **Download the Code**:
    ```bash
    git clone https://github.com/ggerganov/llama.cpp && cd llama.cpp
    ```

2. **Compile the Code**:

On Mac, for compilation with GPU acceleration:
    ```bash
    LLAMA_METAL=1 make
    ```

On Windows, for standard compilation (no acceleration):
```bash
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

For the above to work, you'll need to first have installed CMake from [cmake.org](cmake.org/download/#latest) - download the Windows x64 Installer version. Make sure to add CMake to the system path - you'll be prompted during installation.

Go to the [original repo](https://github.com/ggerganov/llama.cpp), for acceleration options, although be warned that these are complicated.

3. After compilation is finished, download the [model weights](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q3_K_M.bin) to your llama.ccp folder

4. cd into your folder from your terminal and run
    ```
    ./server -m llama-2-7b-chat.ggmlv3.q3_K_M.bin -ngl 48 -c 2048
    ```

Note that the '-ngl 48' offloads layers of the model to the GPU.

5. Open the local port that you see in your terminal.
