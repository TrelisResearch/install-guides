# Install Guides
Short guides for Large Language Models.

> Discover more resources/support [here](https://Trelis.com/About).

## Getting Started

(I've put this in an order that might be useful for newcomers)

Basic:
- `yourbench-space.md`: Explains the options for running LLM fine-tuning or inference (generating responses) using a simple jupyter or Google Colab notebook.
- llm-notebook-setup.md: Explains the options for running LLM fine-tuning or inference (generating responses) using a simple jupyter or Google Colab notebook.
- Pushing_to_Hub.ipynb : all about downloading, uploading and pushing models (including adapters and quantized models) to HuggingFace Hub.
- Google_Colab_Llama_Simple_Inference.ipynb : A simple notebook to generate responses from a Llama 2 language model.

Intermediate:
- `multi-gpu` folder. This contains simple scripts to run training in model parallel, distributed data parallel and Fully Sharded Data Parallel.
- Understanding_Quantization_and_AWQ : Pairs with a YouTube video by TrelisResearch on AWQ quantization.
- 8_bit_quantization.ipynb : Use this notebook to push models to hub in 8-bit.
- LLM_Comparison.ipynb : Perform some basic comparisons of Language Model Performance
- llama-cpp-setup.md : Run an LLM on your laptop using llama.cpp
- jupyter-lab-setup : How to set up jupyter lab on your laptop

## From here..
Once you've tried the basic scripts, consider trying:
- Embeddings
- Chat fine-tuning
- Fine-tuning for structured responses
- Supervised and Unsupervised fine-tuning
- Server Setup

One way to advance on these is via the [Trelis YouTube Channel](https://youtube.com/@TrelisResearch). You can also check out [Trelis.com](https://trelis.com) to purchase advanced fine-tuning and inference scripts.

## Changelog
- Add in basic scripts for running `yourbench`
