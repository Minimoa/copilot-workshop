# Task3 Web Interface

This project is a simple web application built using Flask that displays a user interface with an input field and a send button.

## Project Structure

```
Task3
├── app.py                # Main application file
├── static
│   ├── css
│   │   └── style.css     # CSS styles for the web interface
│   └── js
│       └── script.js     # JavaScript for handling user interactions
├── templates
│   └── index.html        # HTML template for the web interface
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Requirements

To run this project, you need to have the following dependencies installed:

- Flask

You can install the required dependencies by running:

```
pip install -r requirements.txt
```

## Running the Application

To start the Flask web server, run the following command in your terminal:

```
python app.py
```

Once the server is running, open your web browser and navigate to `http://127.0.0.1:5000` to view the web interface.

## Usage

1. Enter your input in the text field at the top of the page.
2. Click the "Send" button to submit your input.

## License

This project is open source and available under the MIT License.