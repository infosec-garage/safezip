#!/usr/bin/env python3
"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""
from io import open
from os import environ, path, walk
from typing import List

from setuptools import find_packages, setup

# Base Parameters
PACKAGE_NAME = "safezip"
AUTHOR = "InfoSec Garage Dev Team"
AUTHOR_EMAIL = 'devs@infosec-garage.org'
DESCRIPTION = "Create an in-memory zip file."
PROJECT_URL = "https://github.com/infosec-garage/safezip"
# Set version  here.
# The version will be compiled as <MAJOR>.<MINOR>.<MICRO>.
V_MAJOR = 0  # Major version
V_MINOR = 1  # Minor version
V_MICRO_DEFAULT = 0  # This is the default Micro version, if left to 0, it will be replaced by the build environment.

# Add your commands (console scripts) below.
# An entry has to be formulated this way:
# `<command-name>=<python-module.python-submodule:function>`
# For instance: "safezip=safezip:cli"
# where `cli` is a method exposed in your package.
CONSOLE_SCRIPTS: List[str] = [
    #   "safezip=safezip:cli",
]

# Package requirements/dependencies.
# List your requirements here.
REQUIREMENTS: List[str] = [
    # "click",   # Recommended command line utility for building your own CLI tools.
    # "pydantic",  # Recommended way to work with data objects in python.
    # "httpx",  # Like python requests, but also supporting async calls.
    "pyzipper",  # A replacement for Python's zipfile that can read and write AES encrypted zip files.
]

# Testing requirements are listed here.
# Install with `pip install safezip[test]`
REQUIREMENTS_TEST: List[str] = [
    "pytest",
    "pytest-cov",
    "coverage",
]

# Development requirements are listed here.
# Install with `pip install safezip[dev]`
# This will include testing requirements above automatically.
REQUIREMENTS_DEV: List[str] = [
    "twine",
    "wheel",
    "flake8",
    "pydocstyle",
    "pycodestyle",
    "mypy",
    "pylint",
    "bump2version",
    "python-dotenv",
]

# Documentation generation requirements
# Install with `pip install safezip[doc]`
# You only need to install these if you plan to develop/troubleshoot documentation generation locally.
REQUIREMENTS_DOC: List[str] = [
    "Sphinx==4.0.1",
    "docutils<0.17",
    "autoapi==2.0.1",
    "sphinx-autodoc-typehints==1.12.0",
    "sphinx-rtd-theme==0.5.2",
    "sphinxcontrib-applehelp==1.0.2",
    "sphinxcontrib-devhelp==1.0.2",
    "sphinxcontrib-htmlhelp==1.0.3",
    "sphinxcontrib-jsmath==1.0.1",
    "sphinxcontrib-qthelp==1.0.3",
    "sphinxcontrib-serializinghtml==1.1.4",
    "sphinx-click==3.0.1",
]

##########################################
# Here be dragons, do not edit below...  #
##########################################

# Generate version string
if not V_MICRO_DEFAULT:
    V_MICRO = environ.get(
        "TRAVIS_BUILD_NUMBER", V_MICRO_DEFAULT
    )  # Micro version from Travis
else:
    V_MICRO = V_MICRO_DEFAULT

VERSION = f"{V_MAJOR}.{V_MINOR}.{V_MICRO}"

# Get the long description from the `README.md` file.
HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    # This is the name of your project. The first time you publish this
    # package, this name will be registered for you. It will determine how
    # users can install this project, e.g.:
    #
    # $ pip install sampleproject
    #
    # And where it will live on PyPI: https://pypi.org/project/sampleproject/
    #
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name
    name=PACKAGE_NAME,  # Required
    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    #
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=VERSION,  # Required
    # This is a one-line description or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#summary
    description=DESCRIPTION,  # Optional
    # This is an optional longer description of your project that represents
    # the body of text which users will see when they visit PyPI.
    #
    # Often, this is the same as your README, so you can just read it in from
    # that file directly (as we have already done above)
    #
    # This field corresponds to the "Description" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=LONG_DESCRIPTION,  # Optional
    # Denotes that our long_description is in Markdown; valid values are
    # text/plain, text/x-rst, and text/markdown
    #
    # Optional if long_description is written in reStructuredText (rst) but
    # required for plain-text or Markdown; if unspecified, "applications should
    # attempt to render [the long_description] as text/x-rst; charset=UTF-8 and
    # fall back to text/plain if it is not valid rst" (see link below)
    #
    # This field corresponds to the "Description-Content-Type" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    # This should be a valid link to your project's main homepage.
    #
    # This field corresponds to the "Home-Page" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#home-page-optional
    url=PROJECT_URL,  # Optional
    # This should be your name or the name of the organization which owns the
    # project.
    author=AUTHOR,  # Optional
    # This should be a valid email address corresponding to the author listed
    # above.
    author_email=AUTHOR_EMAIL,  # Optional
    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # These classifiers are *not* checked by 'pip install'. See instead
        # 'python_requires' below.
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a string of words separated by whitespace, not a list.
    keywords="sample mdr setuptools development demo",  # Optional
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(exclude=["contrib", "docs", "tests"]),  # Required
    # Specify which Python versions you support. In contrast to the
    # 'Programming Language' classifiers above, 'pip install' will check this
    # and refuse to install the project if the version does not match. If you
    # do not support Python 2, you can simplify this to '>=3.5' or similar, see
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
    python_requires=">=3.6.8, <4",
    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=REQUIREMENTS,  # Optional
    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    extras_require={
        "test": REQUIREMENTS_TEST,
        "doc": REQUIREMENTS_DOC,
        "dev": REQUIREMENTS_DEV + REQUIREMENTS_TEST,
        "all": REQUIREMENTS_TEST + REQUIREMENTS_DEV + REQUIREMENTS_DOC,
    },
    # If there are data files included in your packages that need to be
    # installed, specify them here.
    #
    # If using Python 2.6 or earlier, then these have to be included in
    # MANIFEST.in as well.
    # package_data={  # Optional
    #    'sample': ['package_data.dat'],
    # },
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],  # Optional
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={"console_scripts": CONSOLE_SCRIPTS},  # Optional
    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    # project_urls={  # Optional
    #    'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
    #    'Funding': 'https://donate.pypi.org',
    #    'Say Thanks!': 'http://saythanks.io/to/example',
    #    'Source': 'https://github.com/pypa/sampleproject/',
    # },
    # Gather all scripts from the `bin` and `scripts` folders.
    # scripts=['some_script.py']
)
