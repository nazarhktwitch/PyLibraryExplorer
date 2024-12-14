# PyLibrary Explorer

A simple Python application built with `tkinter` to search for Python libraries on PyPI and view their available versions. This application allows users to:
- Search for a Python library by name.
- View the latest version of the library.
- View all available versions of the library.

## Features
- Search for libraries on PyPI.
- Display the latest version of the library.
- View all available versions of the library.
- User-friendly graphical interface built with `tkinter`.

## Requirements
- Python 3.x
- `requests` library (for fetching data from PyPI)

## Installation

1. Clone or download the repository.
2. Install the required dependencies:
   ```bash
   pip install requests
Or:
   ```bash
   pip install -r requirements.txt
```

## Usage

    Run the script using Python:

    python library_explorer.py

    The application will open with the following features:
        Search: Enter the name of a Python library and click "Search" to see if it exists on PyPI and view its latest version.
        Get Available Versions: After searching, click "Get Available Versions" to see all available versions of the library.

## Example

    To search for a library like requests:
        Enter requests in the search bar.
        Click "Search" to get information about the latest version.
        Click "Get Available Versions" to see all available versions of requests.

## Contributing

Feel free to fork the repository and submit pull requests with improvements. If you encounter any bugs or have feature requests, please open an issue on the GitHub repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
