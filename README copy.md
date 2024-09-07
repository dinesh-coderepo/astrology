# Zodiac Sign Finder

This is a simple Flask application that determines a user's zodiac sign based on their birth date.

## Prerequisites

- Python 3.8 or higher (3.11 recommended)
- pip (Python package manager)

## Installation

1. Clone this repository or download the source code.

2. Navigate to the project directory:
   ```
   cd path/to/zodiac-sign-finder
   ```

3. Install the required dependencies:
   ```
   pip install flask
   ```

## Running the Application

1. Start the Flask server:
   ```
   python main.py
   ```

2. Open your web browser and go to:
   ```
   http://localhost:5000
   ```

   Note: If you want to access the application from a different machine on the same network, replace 'localhost' with the IP address of the machine running the server.

You should now see the Zodiac Sign Finder application running in your browser.

## Usage

1. Enter your birth date in the provided input field.
2. Click the "Find My Zodiac Sign" button.
3. Your zodiac sign and some information about it will be displayed.

## File Structure

- `main.py`: The main Flask application file
- `zodiac.py`: Contains functions for determining zodiac signs
- `templates/index.html`: The HTML template for the web interface
- `static/js/app.js`: JavaScript file for handling user interactions
- `static/css/styles.css`: CSS file for styling the web interface

Enjoy finding your zodiac sign!
