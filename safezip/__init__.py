"""Top-level package for SafeZip."""
from typing import Protocol
from io import BytesIO
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

    def __init__(self, password: str = "infected"):
        """Create a new SafeZip object."""
        self.password = bytes(password, 'utf-8')
        self.mem_zip = BytesIO()

    def add_from_bytes(self, data: bytes, filename: str) -> None:
        """Add file data from bytes."""
        with pyzipper.AESZipFile(
                self.mem_zip,
                mode="a",
                compression=pyzipper.ZIP_LZMA,
                encryption=pyzipper.WZ_AES) as zf:
            zf.setpassword(self.password)
            zf.writestr(filename, data)

    def add_from_iostream(self, data: BytesIO, filename: str) -> None:
        """Add file data from an IO Stream."""
        data.seek(0)
        self.add_from_bytes(data.read(), filename)

    def add_from_http_response(self, data: ResponseLike, filename: str) -> None:
        """Add file data from a Requests or Httpx Response object."""
        if data.status_code >= 200 and data.status_code < 300:
            self.add_from_bytes(data.content, filename)
        else:
            raise BytesWarning("HTTP {}: unable to retrieve data. Skipping bytes.".format(data.status_code))

    def get_bytes(self) -> bytes:
        """Return the ZIP file as bytes."""
        return self.mem_zip.getvalue()
