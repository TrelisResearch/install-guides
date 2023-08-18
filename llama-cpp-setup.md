## Mac Installation:
*for detailed instructions go to the [original repo](https://github.com/ggerganov/llama.cpp)

1. **Download the Code**:
    ```bash
    git clone https://github.com/ggerganov/llama.cpp && cd llama.cpp
    ```

2. **Standard Build**:
    ```bash
    make
    ```

3. **GPU Acceleration on Apple Devices**:
    ```bash
    LLAMA_METAL=1 make
    ```

> **Note for Mac with M1**: Simply prepend `LLAMA_M1=1` before any `make` command mentioned above.

## Windows Installation:
1. **Download the Code**:
    ```bash
    git clone https://github.com/ggerganov/llama.cpp && cd llama.cpp
    ```

2. **Setup and Build**:
    - Download and extract the latest `fortran` version of `w64devkit`.
    - Run `w64devkit.exe`.
    - Navigate to the `llama.cpp` directory.
    ```bash
    make
    ```

3. **BLAS Acceleration with OpenBLAS**:
    - Download `OpenBLAS` for Windows.
    - Copy necessary files from the `OpenBLAS` zip to the appropriate `w64devkit` directories.

    ```bash
    make LLAMA_OPENBLAS=1
    ```

## Running the server:
1. After installation is finished, download the [model weights](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q3_K_M.bin) to your llama.ccp folder

2. cd into your folder from your terminal and run
    ```
    ./server -m llama-2-7b-chat.ggmlv3.q3_K_M.bin -ngl 48 -c 2048
    ```

Note that the '-ngl 48' offloads layers of the model to the GPU.

3. Open the local port that you see in your terminal.
