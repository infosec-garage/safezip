"""This file demonstrates the usage of In-Memory Zipper."""
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
zip_output_file = Path("encrypted.zip")
zip_output_file.write_bytes(sz.get_bytes())
