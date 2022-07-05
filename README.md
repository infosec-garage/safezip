# Safe ZIP
Create an in-memory zip file.

Welcome to the Safe ZIP documentation.


## Installation

The package is made available in the MDR Package index,
as such it can be installed with `pip install safezip`.

### For developers

You can install an editable version of safezip by cloning this repository locally
and then from within the repository root run:
```bash
pip install -e .[dev]
```
This will make the package available to the (virtual) python environment,
while all project dependencies and an associated toolset that is used for development (type checking, code style...)
is included, as well as packages used for running the unit tests.

Running unit tests locally before committing is recommended,
this can be done by running `pytest -v` in the root of the repository.

## API Documentation

Auto-generated API documentation is available at https://pages.github.com/infosec-garage/safezip


## Sample usage

Create an in-memory zip file.
```python
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
```
