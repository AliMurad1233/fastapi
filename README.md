# First-FastAPI-Project

## A Quick Walk Through The Project

### Description
FastAPI is fast web framework used for building APIs, I went with it because it's easy to use and it provides automatic data validation and documentation. This FastAPI project written in Python provides APIs for uploading,training a logistic regression model and saving it, showing the progress of the training phase and listing all the models saved. This process only works with (csv,xlsx,xls) extensions

### Instructions 
#### how to install and get the project running
- Create a local copy by cloning the repository
- Open it with Pycharm or any other IDE you prefer
- Install all requirements with pip install -r requirements.txt
- Make sure there are not any errors showing
- Go to loc_variables.py and edit the paths to match your device
- Then open the terminal in your IDE
- Enter the following line "uvicorn app.main:app --reload" to get the project running
- Finally, click the localhost path and add /docs to load it in swagger IU to test it

## Prerequisites

- Python 3.8+
- FastAPI
- Joblib
- Pandas
- Uvicorn (for running the app)
