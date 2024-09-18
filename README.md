#FastAPI Project

This project provides an API for training a logistic regression model on Titanic dataset data, with endpoints for data upload only allowing (csv,xlsx,xls), training the model on the uploaded data and monitoring its progress, and finally, it saves the models in a special directory so that they can all be retrieved and ready for later use.

## Prerequisites

- Python 3.8+
- FastAPI
- Joblib
- Pandas
- Uvicorn (for running the app)

- You can install all required dependencies by running:

```bash
pip install -r requirements.txt
