from api.models import Session, FileData

def get_file_by_id(file_id: str) -> str:
    """ Getting file by id

    Parameters
    ----------
    file_id : str

    Returns
    -------
    str
        file md5 hash

    """
    session = Session()
    file_record = session.query(FileData).filter_by(id=file_id).first()

    if file_record:
        return file_record.md5_hash
    else:
        return "File not found"
