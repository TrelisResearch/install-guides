# Evals with YourBench

WORK IN PROGRESS.

>[!TIP]
>For more detailed guidance, see [this youtube video](https://youtu.be/cO_MA1JjCZ0)

1. Clone the repo: `git clone https://huggingface.co/spaces/yourbench/advanced`
2. cd into the repo: `cd advanced`
3. After it, run `uv sync` in the project folder 
4. Build the project with `docker build -t yourbench .` (you need to start docker first)
5. Log in to huggingface with `uv run --with huggingface-hub huggingface-cli login`
6. Run the project with `docker run --rm --name=yourbench -p 7860:7860 -e HF_TOKEN=<your_token> yourbench` (get your token from [here](https://huggingface.co/settings/tokens))
7. After successful run, you will be able to open the project at `http://localhost:7860/`

Current issues:
- Unclear whether login AND passing the token via -e is required (it would seem only -e should be required).
- Error shown due to missing token (even though datasets are pushed/created)
- Error in running evals due to misisng token