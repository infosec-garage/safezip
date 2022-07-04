"""Top-level package for In-Memory Zipper."""
from typing import Dict, List
from pathlib import Path
from io import BytesIO
import zipfile


def zipbytes_from_bytes(files: Dict[str, bytes]) -> bytes:
    """Create an in-memory zip file from a dictionary of bytes data.

    Hat tip: https://www.neilgrogan.com/py-bin-zip/
    """
    mem_zip = BytesIO()

    with zipfile.ZipFile(mem_zip, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
        for filename, data in files.items():
            zf.writestr(filename, data)

    return mem_zip.getvalue()


def zipfile_from_bytes(files: Dict[str, bytes]) -> Path:
    """Create a zip file from a dictionary of bytes data."""
    pass


def zipbytes_from_files(files: List[Path]) -> bytes:
    """Create an in-memory zip file from a list of files."""
    pass


def zipfile_from_files(files: List[Path]) -> Path:
    """Create a zip file from a list of files."""
    pass
