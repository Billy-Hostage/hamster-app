import pysvn

from .common import wc_notify_action_map

def svn_checkout(checkout_url: str, dest_path: str):
    def log_action(d):
        if d["action"] == pysvn.wc_notify_action.update_completed:
            path = d["path"]
            print(f"{wc_notify_action_map[d["action"]]} {path}")
    client = pysvn.Client()
    client.callback_notify = log_action
    client.checkout(
        checkout_url,
        dest_path
    )

