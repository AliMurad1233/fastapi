# Model Training API On The Titanic Dataset

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

## reference for what to expect
- You should have this file structure format after opening the repository
- <img width="473" alt="Screenshot 2024-09-19 at 12 43 20 PM" src="https://github.com/user-attachments/assets/492928e9-e86c-4dc0-84c7-c1439cc3caaa">
