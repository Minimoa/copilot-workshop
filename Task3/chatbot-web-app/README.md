# Chatbot Web Application

This is a simple chatbot web application built using Python and Flask. The application allows users to interact with a chatbot through a modern web interface.

## Project Structure

```
chatbot-web-app
├── app.py                # Main entry point of the web application
├── static
│   ├── css
│   │   └── style.css     # CSS styles for the web application
│   └── js
│       └── main.js       # JavaScript for handling user interactions
├── templates
│   └── index.html        # HTML template for the main page
├── chatbot
│   ├── __init__.py       # Marks the chatbot directory as a package
│   └── bot.py            # Logic for the chatbot
├── requirements.txt       # Python dependencies for the project
└── README.md             # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd chatbot-web-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your web browser and go to `http://127.0.0.1:5000` to interact with the chatbot.

## Usage

Type your message in the input box and press enter or click the send button. The chatbot will respond with a generated reply based on your input.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.