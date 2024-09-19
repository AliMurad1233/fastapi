from app.data.preprocessing_titanic_data import preprocess_data
from utilities.operations import date_format
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import os
from app.loc_variables import file_path

training_status = {"status": "Not Started", "details": "", "progress": 0}


def calculate_max_iter(n_samples: int, n_features: int) -> int:

    base_iter = 100
    sample_factor = n_samples // 100
    feature_factor = n_features // 10

    # Calculate max_iter
    max_iter = base_iter + (sample_factor * 50) + (feature_factor * 20)
    return max(max_iter, 100)


async def train_model_async(file_location: str, file_name: str):
    global training_status
    training_status["status"] = "In Progress"
    training_status["progress"] = 0

    try:
        df = pd.read_csv(file_location)
        X_train, y_train = preprocess_data(df)

        n_samples, n_features = X_train.shape
        max_iter = calculate_max_iter(n_samples, n_features)


        model = LogisticRegression(max_iter=max_iter)
        model.fit(X_train, y_train)

        # Update progress
        training_status["progress"] = 100
        training_status["status"] = "Completed"

        formatted_date = date_format()
        joblib.dump(model, f"{file_path}_{file_name}_{formatted_date}.joblib")
        print(f"Model training complete. Model saved at {file_path}")

    except Exception as e:
        training_status["status"] = "Failed"
        training_status["details"] = str(e)
        training_status["progress"] = 0


def list_saved_models(directory: str):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    model_files = [f for f in files if f.endswith('.joblib')]
    return model_files




