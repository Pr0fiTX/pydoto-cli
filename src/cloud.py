import dropbox as dbx
from dropbox.dropbox_client import BadInputException
from dropbox.exceptions import AuthError


class Cloud:
    def __init__(self):
        pass

    @classmethod
    def dbx_auth(cls, key):
        if key is None:
            print("!=> The KEY field is empty")
            return

        try:
            drbx = dbx.Dropbox(key)
            drbx_acc_info = drbx.users_get_current_account()
        except (AuthError, BadInputException) as e:
            print(f"!=> Can't log in into your Dropbox acccount: {e}")
            return

        print(f"Good Day, {drbx_acc_info.name.display_name}!")
        return drbx
