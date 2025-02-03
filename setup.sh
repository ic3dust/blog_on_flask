#!/bin/bash

# Get the directory where this script is located
PROJECT_DIR=$(dirname "$(realpath "$0")")

# Define the Flask app file (adjust as needed)
FLASK_APP="$PROJECT_DIR/app.py"
FLASK_APP_FILE="microblog.py"
echo "Project directory: $PROJECT_DIR"

echo "Flask app file: $FLASK_APP"

# Navigate to the project directory
cd "$PROJECT_DIR" || { echo "Project directory not found!"; exit 1; }

# Check if the virtual environment exists, if not, create it
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip and install required dependencies
echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing flask..."
pip install flask

echo "Installing python-dotenv..."
pip install python-dotenv

echo "Installing flask-wtf..."
pip install flask-wtf

echo "Installing flask-sqlalchemy..."
pip install flask-sqlalchemy 

echo "Installing flask-migrate..."
pip install flask-migrate 

echo "Installing flask-login..."
pip install flask-login

echo "Installing email-validator..."
pip install email-validator

echo "You can enter python interpreter with 'py', 'python' or 'python3' to check DB on the current stage(1st-2nd commit)!"

echo "
Use:

(venv) $ flask db downgrade base
(venv) $ flask db upgrade

before utilizing flask shell database.
"

# Check if the Flask app file exists
if [ ! -f "$FLASK_APP_FILE" ]; then
    echo "Error: $FLASK_APP_FILE not found in $PROJECT_DIR"
    exit 1
fi

# Export the Flask app environment variable
export FLASK_APP=$FLASK_APP_FILE

# Run the Flask application
echo "Starting Flask server..."
flask run

# Keep the environment active after Flask stops (optional)
trap "echo 'Server stopped. You can now use the virtual environment again with 'source venv/bin/activate' and then 'flask run'.'" EXIT
