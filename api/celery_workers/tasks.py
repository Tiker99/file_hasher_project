import os
import hashlib
import logging

from filelock import FileLock

from api.models import Session, FileData

from .worker import app

log_filename = "./api/logs/workers.log"
lock_filename = f"{log_filename}.lock"

WORKER_ID = os.environ.get("WORKER_ID", "default_worker")


def setup_custom_logger():
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter(
        fmt=f'%(asctime)s [%(levelname)s | Worker {WORKER_ID}] %(message)s'
    )
    handler = logging.FileHandler(log_filename, mode='a')
    handler.setFormatter(formatter)

    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger


logger = setup_custom_logger()


def log_message(message):
    with FileLock(lock_filename):
        logger.info(message)


@app.task
def store_md5(file_content, file_id):
    file_md5_hash = hashlib.md5(file_content).hexdigest()
    log_message(f"File hash: {file_md5_hash}")

    session = Session()
    file_data = FileData(id=file_id, md5_hash=file_md5_hash)
    log_message(f"Session: {session}")

    session.add(file_data)
    session.commit()
    session.close()
    log_message("Completed")

    return file_md5_hash
