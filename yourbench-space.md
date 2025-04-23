# Evals with YourBench

WORK IN PROGRESS.

>[!TIP]
>For more detailed guidance and advanced techniques, see [this youtube video](https://youtu.be/cO_MA1JjCZ0) and subsequent videos on data generation from [Trelis YouTube Channel](https://youtube.com/@TrelisResearch).

![Setup Instructions](image.png)

## Running on HuggingFace
Run this [here](https://huggingface.co/spaces/yourbench/advanced) on a Chrome or Brave Browser. You'll also need to have a credit card set up on HuggingFace to pay for inference costs (probably <$1 per dataset run).

To ensure the space is up, it may be wise to clone the repo into your HuggingFace organisation.

## Running Locally

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

## Notes on Dataset Generation
- Question coverage: question coverage will be reasonably good, although there is no second pass done to fill in any gaps.
- Question Contextualisation: A major weakness is that questions do not provide sufficient context. This can be improved through prompt engineering AND the use of a strong instruciton following model, like Claude Sonnet 3.7. See the video for instructions there.
- Document processing is done by MarkItDown from Microsoft. This is probably a bit inferior to marker-pdf or using Gemini-Flash raw.
- The current approach creates questions and answers. Using 'criteria' for scoring of answers can be more robust than using ground truth answers.

See [this youtube video](https://youtu.be/cO_MA1JjCZ0) and subsequent videos on data generation from [Trelis YouTube Channel](https://youtube.com/@TrelisResearch) for more content on the topic.

Getting to the detailed video:

![Detailed video](youtube_cO_MA1JjCZ0_qr.png)
