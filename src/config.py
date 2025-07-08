from pathlib import Path


class Config:
    CONFIG_NAME = "pydoto.conf"
    DB_NAME = "pydoto.json"

    HOME_FOLDER_PATH = Path.home()
    CONFIG_PATH = HOME_FOLDER_PATH / ".config" / "pydoto" / CONFIG_NAME
    DB_PATH = HOME_FOLDER_PATH / ".config" / "pydoto" / DB_NAME

    def __init__(self):
        pass
