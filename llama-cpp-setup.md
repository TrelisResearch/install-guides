# Llama.cpp Installation Guide

## Warnings / Expectations
- Macs with M1 or M2 chips will deliver 10+ tokens/second, even with only 8 GB RAM. Difficulty to install = 3/10.
- Macs with an intel chip can deliver about 2 tokens/second. It's interesting to test, but slow to use. Difficulty to install = 5/10.
- Windows computers:
    - Tedious to install - involves multiple packages to set up CPU or GPU acceleration (w64devkit + OpenBLAS). Difficulty to install = 8/10.
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

- Download [w64devkit-fortran-1.20.0.zip](https://github.com/skeeto/w64devkit/releases)
- Extract the zipped file
- Navigate to w64devkit.exe within the folder structure and run that file (by clicking on it in a file explorer)
- 'cd' into your llama.cpp folder
- Issue the command `make` to build llama.cpp

Go to the [original repo](https://github.com/ggerganov/llama.cpp), for other install options, including acceleration. Be warned that this quickly gets complicated.

3. After compilation is finished, download the [model weights](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q3_K_M.bin) to your llama.ccp folder.

4. cd into your folder from your terminal and run
    ```
    ./server -m llama-2-7b-chat.ggmlv3.q3_K_M.bin -ngl 48 -c 2048
    ```

Note that the '-ngl 48' offloads layers of the model to the GPU. That flag will be ignored if you didn't compile with GPU or accelerate support.

For Windows, use:
    ```
    server.exe -m llama-2-7b-chat.ggmlv3.q3_K_M.bin -ngl 48 -c 2048
    ```

5. Open the local port that you see in your terminal.
