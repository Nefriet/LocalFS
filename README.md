# File Share

A simple Flask web application for uploading and downloading files.

## Features

- Upload files via a web interface
- Download files from a shared directory
- Simple, clean UI

## Requirements

- Python 3.8+
- Flask

## Installation

```bash
git clone https://github.com/rast28/LocalFS.git
cd LocalFS
python -m venv env
source env/bin/activate on windows: .\env\Scripts\Activate
pip install -r requirements.txt
```

## Usage
Locate in terminal the folder where you installed the app and then run: python run.py



Then open [http://yourip:5000]in your browser. The link you will need to open will be displayed in your terminal.

## Configuration

- Uploaded files are stored in the `uploads/` directory by default.
- Edit `myapp/__init__.py` to change configuration options.

