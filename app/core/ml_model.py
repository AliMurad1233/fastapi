from app.data_preprocessing.data_preprocessing import preprocess_data
from utilities.operations import date_format
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import os

model_file = "/Users/alimurad/my_fastAPI:/temp_file/"
file_path = "/Users/alimurad/my_fastAPI:/app/models_saved/"
training_status = {"status": "Not Started", "details": "", "progress": 0}


async def train_model_async(file_location: str, file_name:str):

    global training_status
    training_status["status"] = "In Progress"

    try:
        df = pd.read_csv(file_location)
        X_train, y_train = preprocess_data(df)
        model = LogisticRegression(max_iter=100000)

        for i in range(1,11):
            model.set_params(max_iter=i * 100)
            model.fit(X_train, y_train)
            training_status["progress"] = i * 10

        formated_date = date_format()
        joblib.dump(model, f"{file_path}_{file_name}_{formated_date}.joblib")

        print(f"Model training complete. Model saved at {file_path}")
        training_status["progress"] = 100

        training_status["status"] = "Completed"
        training_status["details"] = f"Model saved at {file_path}"
    except Exception as e:
        training_status["status"] = "Failed"
        training_status["details"] = str(e)
        training_status["progress"] = 0


def list_saved_models(directory: str):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    model_files = [f for f in files if f.endswith('.joblib')]
    return model_files




