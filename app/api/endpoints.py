from fastapi import BackgroundTasks, Query
from app.core.ml_model import train_model_async,training_status, list_saved_models
from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os
from app.core.file_cleanup import delete_old_files
import threading
import time


router = APIRouter()

model_file = "/Users/alimurad/my_fastAPI:/temp_file/"
model_directory = "/Users/alimurad/my_fastAPI:/app/models_saved/"

def periodic_cleanup():
    while True:
        delete_old_files("temp_file", 2)
        time.sleep(86400)

cleanup_thread = threading.Thread(target=periodic_cleanup, daemon=True)
cleanup_thread.start()


@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):

    allowed_extensions = {"csv", "xlsx", "xls"}
    file_extension = file.filename.split('.')[-1].lower()

    if file_extension not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Invalid file type. Only CSV and Excel files are allowed.")

    try:
        file_location = f"temp_file/{file.filename}"
        os.makedirs(os.path.dirname(file_location), exist_ok=True)

        with open(file_location, "wb") as f:
            f.write(file.file.read())

        return JSONResponse(content={"filename": file.filename, "message": "File uploaded successfully!"})
    except Exception as e:
        return JSONResponse(content={"message": f"An error occurred: {str(e)}"}, status_code=500)


@router.post("/train-model/")
async def train_mode(
        background_tasks: BackgroundTasks,
        file_name: str = Query(...)
):
    file_location = f"temp_file/{file_name}"

    allowed_extensions = ["csv", "xlsx", "xls"]

    # Check if the file exists for any of the allowed extensions
    for ext in allowed_extensions:
        file_location = f"{file_location}.{ext}"
        if os.path.exists(file_location):
            background_tasks.add_task(train_model_async, file_location, file_name)
            return {"message": "Training has started in the background", "file_name": file_name}

        if not os.path.exists(file_location):
            raise HTTPException(status_code=404, detail="File not found with any of the allowed extensions.")


@router.get("/training-status/")
async def get_training_status():
    return {"status": training_status["status"], "details": training_status["details"], "progress": training_status["progress"]}


@router.get("/list-models/")
async def list_models():
    try:
        models = list_saved_models(model_directory)
        return {"models": models}
    except Exception as e:
        return {"error": str(e)}



