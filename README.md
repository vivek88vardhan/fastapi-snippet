# fastapi-snippet

## Freeze all pip3 installations
pip3 freeze > requirements.txt

## Creating the virtual environment
sudo apt install python3-virtualenv
virtualenv venv

## Activating virtualenv on Linux Ubuntu /macOS
source venv/bin/active

## Activate virtualenv on Windows 10
.\venv\Scripts\activate

## Installing Python dependencies
pip3 install -r requirements.txt

## Running app as Service
uvicorn main:app --reload