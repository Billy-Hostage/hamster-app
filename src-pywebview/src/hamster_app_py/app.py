import os
import sys
from typing import Optional

import webview
import webview.menu as wm

from .app_api import HamsterAppApi
from .svn.checkout import svn_checkout

def force_quit(main_window: webview.Window):
    main_window.destroy()

def open_file_dialog():
    active_window = webview.active_window()
    out = active_window.create_file_dialog(webview.FOLDER_DIALOG, directory=r'G:\subversion\hamster-dev\checkout-test')
    print(out)
    if out:
        r = active_window.create_confirmation_dialog('Question', 'Are you ok with this?')
        if r:
            # start checkout svn
            svn_checkout("https://svn.apache.org/repos/asf/subversion/trunk", out[0])


def build_mainwindow_menu(main_window: webview.Window):
    return [
        wm.Menu(
            '文件',
            [
                wm.MenuAction('退出', lambda: force_quit(main_window)),
            ]
        ),
        wm.Menu(
            'DEBUG',
            [
                wm.MenuSeparator(),
                wm.Menu(
                    'SVN-Feature-Test',
                    [
                        wm.MenuAction('检出Subversion-选择目录', open_file_dialog),
                    ],
                ),
            ],
        )
    ]

def get_page_urls(name: str, dev_port: Optional[str]) -> str:
    filename = "index.html"
    match name:
        case "connection_prompt":
            filename = "index_connection_prompt.html"
        case "home":
            filename = "index.html"
        case _:
            sys.stderr.write(f"invalid name {name} for page routing\n default to index")

    if dev_port:
        assert dev_port.isdigit()
        # devmode
        return f"http://localhost:{dev_port}/{filename}"
    else:
        return f"fe/{filename}"

# Entry point for the entire app
def main(
    predefined_repo_url: Optional[str], # when user launched the app via cli and specified args for repo
    vite_dev_port: Optional[str], use_devtool: bool # dev related
):
    # TODO if predefined_repo_url is none, start connection prompt first!

    # start home
    url = get_page_urls("home", vite_dev_port)
    main_window = webview.create_window(
        "Hamster", url, width=1500, height=950, js_api=HamsterAppApi(
            repo_root_url="https://svn.apache.org/repos/asf/subversion"
        )
    )
    menu_items = build_mainwindow_menu(main_window)
    webview.start(None, main_window, debug=use_devtool, ssl=not vite_dev_port, gui="edgechromium", menu=menu_items)  # blocks
