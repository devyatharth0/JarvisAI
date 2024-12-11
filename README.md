# JarvisAI

JarvisAI is an AI assistant implemented in Python that can perform various tasks through voice commands and text input.

## Features

- Voice recognition and text-to-speech capabilities
- Handles greetings, farewells, and general queries
- Provides current time and date information
- Performs basic calculations
- Opens websites and applications on command
- Accessible via a web interface

## Installation

To install JarvisAI, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/JarvisAI.git
   cd JarvisAI
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run JarvisAI as a web server, execute the following command in your terminal:

```
python main.py
```

Once running, open your web browser and navigate to `http://localhost:5000` to interact with JarvisAI using the web interface.

## Dependencies

JarvisAI requires the following Python libraries:

- speech_recognition
- pyttsx3
- flask
- datetime
- webbrowser
- random
- json
- subprocess
- threading

## Examples

Here are some example commands you can try with JarvisAI:

- "What time is it?"
- "Open YouTube"
- "Calculate 5 plus 3"
- "Who are you?"

## Contributing

Contributions to JarvisAI are welcome! Please feel free to submit a Pull Request.

## License

[MIT]