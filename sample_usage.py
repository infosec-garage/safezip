"""This file demonstrates the usage of In-Memory Zipper."""
from safezip import SafeZip
from pathlib import Path
import requests

sz = SafeZip(password='hello')

# Add bytes 1
input_file_1 = Path("setup.py")
input_file_name_1 = "setup-py.txt"
sz.add_from_bytes(input_file_1.read_bytes(), input_file_name_1)

# Add bytes 2
input_file_2 = Path("README.md")
input_file_name_2 = "readme-md.txt"
sz.add_from_bytes(input_file_2.read_bytes(), input_file_name_2)

# Add via http request
sz.add_from_http_response(requests.get('http://example.com'), "example-com.html")

zip_file_name = "encrypted.zip"
zip_output_file = Path(zip_file_name)
zip_binary_data = sz.get_bytes()

zip_output_file.write_bytes(zip_binary_data)
