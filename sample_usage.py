"""This file demonstrates the usage of In-Memory Zipper."""
from safezip import SafeZip
from pathlib import Path
from io import BytesIO
import requests

# Longer approach without a context manager
sz = SafeZip(Path("encrypted1.zip"), password='hello')
sz.add_from_bytes("readme-md.txt", Path("README.md").read_bytes())
sz.add_from_http_response("example-com.html", requests.get('http://example.com'))
sz.close()

# Context manager with data saved straight to an encrypted ZIP file
with SafeZip(Path("encrypted2.zip"), password='hello') as sz:
    sz.add_from_bytes("readme-md.txt", Path("README.md").read_bytes())
    sz.add_from_http_response("example-com.html", requests.get('http://example.com'))

# Context manager with data saved to an encrypted ZIP file via an in-memory buffer
buff = BytesIO()

with SafeZip(buff, password='hello') as sz:
    sz.add_from_bytes("readme-md.txt", Path("README.md").read_bytes())
    sz.add_from_http_response("example-com.html", requests.get('http://example.com'))

Path("encrypted3.zip").write_bytes(buff.getvalue())
