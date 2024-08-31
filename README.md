# FaatAPI

## Setup
Set up virtual environment for Windows
```bash
python -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```
Set up virtual environment for Linux or MacOS you'll instead run
```bash
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```
For conda environment run
```bash
conda activate
pip install -r requirements.txt
```

## Running the app
If the python file name: `xyz.py`
```bash
uvicorn xyz:app --port=5000
```
And for reload
```bash
uvicorn main:app --reload
```
