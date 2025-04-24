# Evals with YourBench

WORK IN PROGRESS.

>[!TIP]
>For more detailed guidance and advanced techniques, see [this youtube video](https://youtu.be/cO_MA1JjCZ0) and subsequent videos on data generation from [Trelis YouTube Channel](https://youtube.com/@TrelisResearch).

![Setup Instructions](image.png)

## Running on HuggingFace
Run this [here](https://huggingface.co/spaces/yourbench/advanced) on a Chrome or Brave Browser.

Costs:
- With a free HuggingFace account, you'll have $0.1 in credits, just about enough to run a simple benchmark and eval.
- Adding a credit card will then allow you to continue running.

Tip: If the space is overloaded,  clone the repo into your HuggingFace organisation.

## Running Locally

```bash
# Clone the repo and navigate to it
git clone https://huggingface.co/spaces/yourbench/advanced
cd advanced

# Install dependencies
uv sync

# Build the Docker image
docker build -t yourbench .

# Run the container with your HuggingFace token
# Option 1: Directly specify your token
docker run --rm --name=yourbench -p 7860:7860 -e HF_TOKEN=<your_token> yourbench

# Option 2: Load token from .env file
# First create a .env file with HF_TOKEN=your_token_here
# Then run:
docker run --rm --name=yourbench -p 7860:7860 --env-file ../.env yourbench
```

After successful run, you will be able to open the project at `http://localhost:7860/`

You can get your HuggingFace token from [here](https://huggingface.co/settings/tokens).

## Notes on Dataset Generation
- Question coverage: question coverage will be reasonably good, although there is no second pass done to fill in any gaps.
- Question Contextualisation: A major weakness is that questions do not provide sufficient context. This can be improved through prompt engineering AND the use of a strong instruciton following model, like Claude Sonnet 3.7. See the video for instructions there.
- Document processing is done by MarkItDown from Microsoft. This is probably a bit inferior to marker-pdf or using Gemini-Flash raw.
- The current approach creates questions and answers. Using 'criteria' for scoring of answers can be more robust than using ground truth answers.

See [this youtube video](https://youtu.be/cO_MA1JjCZ0) and subsequent videos on data generation from [Trelis YouTube Channel](https://youtube.com/@TrelisResearch) for more content on the topic.

Getting to the detailed video:

![Detailed video](youtube_cO_MA1JjCZ0_qr.png)
