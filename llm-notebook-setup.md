# LLM Notebook Setup

A quick guide for getting set for fine-tuning or inference using a jupyter notebook.

You have a few options for running fine-tuning notebooks:
1. Hosted service (Recommended), e.g. Runpod or Vast.ai:
- Runpod one-click template [here](https://runpod.io/gsc?template=ifyqsvjlzj&ref=jmfkcdio) - easier setup.
    - To support the Trelis Research YouTube channel, you can first sign up for an account with [this link](https://runpod.io?ref=jmfkcdio).
- Vast.ai one-click template [here](https://cloud.vast.ai/?ref_id=98762&creator_id=98762&name=Fine-tuning%20Notebook%20by%20Trelis%20-%20Cuda%2012.1) - offers smaller GPUs (which are cheaper to run).
    - To support the Trelis Research YouTube channel, you can first sign up for an account with [this affiliate link](https://cloud.vast.ai/?ref_id=98762).
2. Google Colab (free and good for 7B models or smaller):
- Upload the .ipynb notebook
- Select a T4 GPU from Runtime -> Change Runtime Type.
- make sure to comment out flash attention when loading the model.
3. Your own computer (assuming you have an AMD or Nvidia GPU) - ADVANCED:
- Set up jupyter lab and a virtual environment using the instructions in the 'jupyter-lab-setup.md' file of this repo. [see here](https://github.com/TrelisResearch/install-guides/blob/main/jupyter-lab-setup.md).
