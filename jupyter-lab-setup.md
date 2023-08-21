# Installing Jupyter Lab

1. You'll need to have both python and pip installed to do this. Ask ChatGPT how if you don't. On a Mac, it's best to install python using homebrew, which itself needs to be installed from the homebrew repo on GitHub.
2. Open a terminal.
3. Set up and activate a virtual environment, by running (note that you may not need to install venv as it may be there already):
```
pip install venv
```
then
```
python -m venv LlamaEnv
```
4. Activate the virtual environment:
- On Mac, run
```
source llamaEnv/bin/activate
```
- On Windows, run
```
llamaEnv\Scripts\activate
```
5. Install *jupyterlab*:
```
pip install jupyterlab
```
6. Install ipykernel
```
pip install ipykernel
```
8. Make the virtual environment available to Jupyter Labs with
```
python -m ipykernel install --user --name=llamaEnv
```
8. Start Jupyter with the command
```
jupyter lab
```
9. Menu -> Run -> Run All Cells.
10. Once all cells have run, you'll find the chat interface at the bottom.
