# Shu
## Introduction
Shu is the script use for build deep learning model. This model is the core of the In0ri system to classififer images.
- `screenshot.py` uses for screenshot interface website.
- `Model training.ipynb` uses for training model.
## Requirement
* Python3 (version >=3.6)

## Installation
### Change filename contain URLs
Edit the file `screenshot.py`
```py
myfile = open("govt_urls_full.txt", "r") //govt_urls_full.txt is filename
```
## Usage
### Screenshot.
Installing the required packages:
```sh
sudo apt-get install -y chromium-chromedriver
python3 -m pip install webdriver-manager
python3 -m pip install selenium
python3 -m pip install Pillow
```

Run the file:
```py
python3 screenshot.py
```
### Model training
Before start, you need upload your dataset to your Google Driver with structure such as:
```sh
/dataset/Training/clean
/dataset/Training/defaced
/dataset/Test/clean
/dataset/Test/defaced
```
Afterall, import `Model training.ipynb` to Goodle Colab and running
