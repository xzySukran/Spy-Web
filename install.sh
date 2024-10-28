#!/bin/bash

# Define the Python version you want to use (modify as necessary)
PYTHON_VERSION="3.10"  # Change to your preferred Python version
VENV_DIR="venv"  # Name of the virtual environment directory

# Update package list and install required packages
echo "Updating package list..."
sudo apt update

echo "Installing Python and pip..."
sudo apt install -y python$PYTHON_VERSION python3-pip

# Create a virtual environment
echo "Creating a virtual environment..."
python$PYTHON_VERSION -m venv $VENV_DIR

# Activate the virtual environment
echo "Activating the virtual environment..."
source $VENV_DIR/bin/activate

# Install required Python packages
echo "Installing required Python packages..."
pip install flask requests

# Inform the user about how to run the application
echo "Setup complete!"
echo "To run the application, activate the virtual environment with:"
echo "source $VENV_DIR/bin/activate"
echo "Then run the application with:"
echo "python your_flask_app.py"  # Replace with the name of your main Python file

