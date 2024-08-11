"""
    The main class for Python-JavaScript Inter-op
"""

from typing import Optional

from .svn.list_svn import svn_list

class HamsterAppApi:
    """
        This servers as the api hub for js <-> python interop
        Thanks to python, we can store quite a lot of global states here.
    """

    def __init__(self, repo_root_url: str) -> None:
        self._repo_root_url = repo_root_url

    def svn_list(self, abs_repo_url: Optional[str] = None):
        if not abs_repo_url:
            return svn_list(self._repo_root_url)
        return svn_list(abs_repo_url)

    @property
    def repo_root_url(self) -> str:
        return self._repo_root_url
