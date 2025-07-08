import dropbox as dbx
from dropbox.exceptions import AuthError


class Cloud:
    def __init__(self):
        pass

    def dbx_auth(self, key):
        if key is None:
            print("!=> The KEY field is empty")
            return
