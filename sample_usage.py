"""This file demonstrates the usage of In-Memory Zipper."""
from safezip import zipbytes_from_bytes
from pathlib import Path


input_file_1 = Path("setup.py")
input_file_name_1 = "setup-py.txt"
binary_data_1 = input_file_1.read_bytes()

input_file_2 = Path("README.md")
input_file_name_2 = "readme-md.txt"
binary_data_2 = input_file_2.read_bytes()

binary_data = {
    input_file_name_1: binary_data_1,
    input_file_name_2: binary_data_2,
}

zip_file_name = "thezip.zip"
zip_output_file = Path(zip_file_name)
zip_binary_data = zipbytes_from_bytes(binary_data)

zip_output_file.write_bytes(zip_binary_data)
