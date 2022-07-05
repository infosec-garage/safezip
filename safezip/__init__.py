"""Top-level package for SafeZip."""
from typing import Protocol, Union
from io import BytesIO, IOBase
from pathlib import PurePath
from os import PathLike
import pyzipper


class ResponseLike(Protocol):

    @property
    def status_code(self) -> int:
        ...

    @property
    def content(self) -> bytes:
        ...


class SafeZip:
    """A password protected in-memory ZIP file."""

    def __init__(
            self,
            file: Union[PurePath, PathLike, str, IOBase],  # types supported by `pyzipper`
            password: str = "infected"):
        """Create a new SafeZip object."""
        self.zf = pyzipper.AESZipFile(
            file,
            mode="w",
            compression=pyzipper.ZIP_LZMA,
            encryption=pyzipper.WZ_AES)
        self.zf.setpassword(bytes(password, 'utf-8'))

    def add_from_bytes(self, filename: str, data: bytes) -> None:
        """Add file data from bytes."""
        self.zf.writestr(filename, data)

    def add_from_iostream(self, filename: str, data: BytesIO) -> None:
        """Add file data from an IO Stream."""
        data.seek(0)
        self.add_from_bytes(filename, data.read())

    def add_from_http_response(self, filename: str, data: ResponseLike) -> None:
        """Add file data from a Requests or Httpx Response object."""
        if data.status_code >= 200 and data.status_code < 300:
            self.add_from_bytes(filename, data.content)
        else:
            raise BytesWarning("HTTP {}: unable to retrieve data. Skipping bytes.".format(data.status_code))

    def close(self):
        """Close """
        self.zf.close()

    def __enter__(self):
        """Context manager function."""
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Context manager function."""
        self.close()
