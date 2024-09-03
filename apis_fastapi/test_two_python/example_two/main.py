# don't move
import sys
import os
import uuid
from typing import Annotated
import asyncio

sys.path.append('../')
from example_one import large_csv_processing as csv_processing

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse, FileResponse


app = FastAPI()
UPLOAD_DIR = "../uploads_temp"
os.makedirs(UPLOAD_DIR, exist_ok=True)
tasks_processed: dict[str, dict[str, str]] = {}
principal_path = os.getcwd()

@app.get("/items/{task_id}")
async def getting_tasks(task_id: str):
    task_to_send = tasks_processed.get(task_id) or None
    if (task_to_send is not None and task_to_send.get('response') == 'success'):
        return FileResponse(path=task_to_send.get('path'), media_type="text/csv") # type: ignore
    raise HTTPException(
        status_code=404, detail="Task not found...")


@app.post("/upload-file/")
async def create_upload_file(
    file_in: Annotated[UploadFile, File(description="A file read as UploadFile")],
):
    if file_in.content_type != 'text/csv':
        raise HTTPException(
            status_code=400, detail="Invalid file type...")

    os.makedirs(UPLOAD_DIR, exist_ok=True)
    task_id = str(uuid.uuid4())

    file_location = os.path.join(UPLOAD_DIR, f"{file_in.filename}")

    if (os.path.exists(file_location)):
        file_location = file_location.replace('.csv', f'-{task_id}.csv')

    with open(file_location, "wb") as f:
        f.write(await file_in.read())

    uploads_temp_path = principal_path.replace('example_two', 'uploads_temp')
    file_path_read = f"{uploads_temp_path}/{file_in.filename}"
    file_path_write = f"{uploads_temp_path}/csv_file_saved.csv"

    if (os.path.exists(file_path_write)):
        file_path_write = file_path_write.replace('.csv', f'-{task_id}.csv')

    finishing_process_csv: str = ""
    correct_csv: dict[str,str] = {
        "response": "success",
        "path": file_path_write
    }
    incorrect_csv: dict[str, str] = {
        "response": "error",
        "path": ''
    }
    try:
        task_result = asyncio.create_task(
            get_task_file(file_path_read,file_path_write))
        finishing_process_csv = await task_result
        tasks_processed[task_id] = correct_csv if finishing_process_csv == "ok" else incorrect_csv
    except Exception:
        tasks_processed[task_id] = incorrect_csv

    print(tasks_processed)
    return JSONResponse(content={"ID": task_id})


async def get_task_file(file_path_read: str, file_path_write: str):
    return csv_processing.start_processing(
        file_path_read, file_path_write)
