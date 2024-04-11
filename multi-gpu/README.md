# Multi GPU Training
> This folder contains the test scripts covered in [this YouTube video](https://youtu.be/gXDsVcY8TXQ). You can purchase access to more comprehensive scripts for a one-off lifetime payment, see more at [Trelis.com/ADVANCED-fine-tuning](https://Trelis.com/ADVANCED-fine-tuning).

## Getting Started
To get started, connect to a GPU instance (locally OR using a runpod template provided on main).

The following are the instructions if using RunPod via a terminal [it is better, and RECOMMENDED, to ssh in using VSCode - see Runpod Tips further below], specifically this [template](https://runpod.io/console/gpu-cloud?template=ifyqsvjlzj&ref=jmfkcdio).

1. Connect to the pod via ssh.
1. `cd workspace` to move into the workspace folder.
1. `git clone https://github.com/TrelisResearch/install-guides.git` (you'll need to enter your username and password, as this is a private repo).
1. Then:
```
cd install-guides/multi-gpu
```
to get onto the multi-gpu branch of the repo.

> To edit any of these files when in the runpod instance, it can be easiest to do so within a Jupyter notebook (although you should run python commands from your ssh terminal). Even better, ssh into your instance from VSCode (see Runpod tips below).

Set up a virtual environment and run the installs:
```
python -m venv trelisEnv
source trelisEnv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install flash-attn --no-build-isolation
export HF_HUB_ENABLE_HF_TRANSFER=True
huggingface-cli login
```
> flash-attn has to be installed separately (as per the commands above) or can give issues if installed from the requirements file.

IMPORTANT: If you plan to a) use private models on HuggingFace, or b) push models to Hub, then you'll need to input a token from [here](https://huggingface.co/settings/tokens).

## Running the test scripts
Check out the top of the test scripts for guidance on running them, and see the YouTube video for configuration.

## Runpod Tips
> To support the Trelis Research YouTube channel, you can sign up for an account with [this link](https://runpod.io?ref=jmfkcdio). Thereafter, Trelis is also supported by a 1-2% commission by your use runpod.

The recommended approach is to SSH into the pod. To do this you'll need:
1. to generate a public-private key pair in the .ssh folder on your local device [Runpod Instructions here](https://docs.runpod.io/pods/configuration/use-ssh), and then
2. copy the *public* key into your Runpod Settings.
3. When the pod has started, you can copy the details from the TCP connection instructions into your VSCode ssh configuration and then connect. See the multi-gpu video on [Trelis YouTube](https://youtu.be/gXDsVcY8TXQ) for more info.

### Making git commits using VSCode when connected via SSH
Once you are connected, via SSH, in VSCode, you'll need to set your username and email:
```
git config --global user.name "YOURUSERNAME"
git config --global user.email "[GET THIS FROM YOUR GITHUB SETTINGS]@users.noreply.github.com"
```

## Changelog
11Apr2024:
- Release test scripts.