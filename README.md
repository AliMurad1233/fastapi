# Model Training API On The Titanic Dataset

## A Quick Walk Through The Project

### Description
FastAPI is a fast web framework used for building APIs, I went with it because it's easy to use and it provides automatic data validation and documentation. This FastAPI project written in Python provides APIs for uploading,training a logistic regression model and saving it, showing the progress of the training phase and listing all the models saved. This process only works with (csv,xlsx,xls) extensions. 
This app contains 4 API endpoints; 2 POST and 2 GET. the POST's requests are resposible for uploading the the file and training the dataset. And the 2 GET's requests are responsible for the progress of the training phase and listing the models saved
The goal of this app is to allow the client to upload a file with any of the extensions mentioned above, and training a logistic regression model on the same uploaded file while also monitoring and showing its progress. After that the client can download the model and use it whenever its needed.

### Instructions 
#### how to install and get the project running
- Create a local copy by cloning the repository
- Open it with Pycharm or any other IDE you prefer
- Install all requirements with pip install -r requirements.txt
- Make sure there are not any errors showing
- Go to loc_variables.py and edit the paths to match your device
- Then open the terminal in your IDE
- Enter the following line "uvicorn app.main:app --reload" to get the app running
- Finally, click the localhost path and add /docs to load it in swagger IU to test it

## reference for what to expect
- You should have this file structure format after opening the repository
- <img width="473" alt="Screenshot 2024-09-19 at 12 43 20 PM" src="https://github.com/user-attachments/assets/492928e9-e86c-4dc0-84c7-c1439cc3caaa">

- After running the "uvicorn" command, in the response you will get a line similar to this 
- <img width="528" alt="Screenshot 2024-09-19 at 12 48 07 PM" src="https://github.com/user-attachments/assets/43683c7d-ab6e-45df-8d3b-baa1a92f6fde">

- After clicking on the link, you will open a localhost, go to the localhost's URL and add the "docs"
- <img width="354" alt="Screenshot 2024-09-19 at 12 52 04 PM" src="https://github.com/user-attachments/assets/b732f710-dbf0-440d-a6f8-447009270788">

- Finally, you will find yourself at the Swagger IU documentary, where you can test the project
- <img width="1440" alt="Screenshot 2024-09-19 at 12 53 38 PM" src="https://github.com/user-attachments/assets/c9685105-5d3e-403b-a334-3c7f963f47f6">




