import logging
from uuid import uuid4

from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, File, UploadFile

from api.file_manager import get_file_by_id
from api.celery_workers.tasks import store_md5


app = FastAPI()

app.mount(
    "/usr/src/api/static",
    StaticFiles(directory="/usr/src/api/static"),
    name="static"
)

logging.basicConfig(filename='./api/logs/app.log', level=logging.INFO)


@app.get("/", response_class=FileResponse)
async def read_root():
    return FileResponse("api/templates/base.html")


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_id = str(uuid4())
    file_content = await file.read()
    task = store_md5.delay(file_content, file_id)
    logging.info(task)

    return {"file_id": file_id}


@app.get("/files/{file_id}")
async def get_file_md5(file_id: str):
    if md5_hash := get_file_by_id(file_id):
        return {"file_id": file_id, "md5_hash": md5_hash}
    else:
        return {"error": "File ID not found"}