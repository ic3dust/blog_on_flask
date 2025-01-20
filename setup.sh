#!/bin/bash

# Define project directory and Flask app file
PROJECT_DIR="/mnt/c/Users/DELL/Desktop/blog_on_flask"
FLASK_APP_FILE="microblog.py"

# Navigate to the project directory
cd "$PROJECT_DIR" || { echo "Project directory not found!"; exit 1; }

# Remove old virtual environment if it exists
if [ -d "venv" ]; then
    echo "Removing existing virtual environment..."
    rm -rf venv
fi

# Create a new virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip and install required dependencies
echo "Upgrading pip and installing dependencies..."
pip install --upgrade pip
pip install flask flask-wtf

# Check if the Flask app file exists
if [ ! -f "$FLASK_APP_FILE" ]; then
    echo "Error: $FLASK_APP_FILE not found in $PROJECT_DIR"
    deactivate
    exit 1
fi

# Export the Flask app environment variable
export FLASK_APP=$FLASK_APP_FILE

# Run the Flask application
echo "Starting Flask server..."
flask run
