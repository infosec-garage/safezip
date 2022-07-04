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
import requests

# Create the SafeZip object with a 'hello' password
sz = SafeZip(password='hello')

# Add from bytes
input_file = Path("README.md")
input_file_name = "readme-md.txt"
sz.add_from_bytes(input_file.read_bytes(), input_file_name)

# Add from HTTP response
sz.add_from_http_response(requests.get('http://example.com'), "example-com.html")

# Write the ZIP file
zip_file_name = "encrypted.zip"
zip_output_file = Path(zip_file_name)
zip_output_file.write_bytes(sz.get_bytes())
```
