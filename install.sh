#!/bin/bash

PYTHON_VERSION="3.10"  
VENV_DIR="venv"  

echo "Updating package list..."
sudo apt update

echo "Installing Python and pip..."
sudo apt install -y python$PYTHON_VERSION python3-pip

echo "Creating a virtual environment..."
python$PYTHON_VERSION -m venv $VENV_DIR

echo "Activating the virtual environment..."
source $VENV_DIR/bin/activate

echo "Installing required Python packages..."
pip install flask requests

echo "Setup complete!"
echo "To run the application, activate the virtual environment with:"
echo "source $VENV_DIR/bin/activate"
echo "Then run the application with:"
echo "python main.py" 

echo -e "\n\n"
echo -e "\033[36m ███████╗██╗███╗   ██╗██╗██╗  ██╗██╗  ██╗██╗  ██╗\033[0m"
echo -e "\033[36m ██╔════╝██║████╗  ██║██║██║  ██║██║  ██║██║  ██║\033[0m"
echo -e "\033[36m ███████╗██║██╔██╗ ██║██║███████║███████║███████║\033[0m"
echo -e "\033[36m ╚════██║██║██║╚██╗██║██║██╔══██║██╔══██║██╔══██║\033[0m"
echo -e "\033[36m ███████║██║██║ ╚████║██║██║  ██║██║  ██║██║  ██║\033[0m"
echo -e "\033[36m ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝\033[0m"
echo -e "\033[36m               RAZORxzy\033[0m"

echo -e "\n\033[32mFinis install go to user a tool!\033[0m"
