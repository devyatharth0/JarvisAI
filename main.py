import speech_recognition as sr
import os
import webbrowser
import datetime
import pyttsx3
import sys
import random
import json
import subprocess


class JarvisAI:
    def __init__(self):
        self.engine = self.configure_voice()
        self.load_responses()

    def configure_voice(self):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 180)
        return engine

    def load_responses(self):
        """Load predefined responses"""
        self.responses = {
            "greeting": [
                "Hello! How can I help you today?",
                "Hi! What can I do for you?",
                "Greetings! How may I assist you?"
            ],
            "farewell": [
                "Goodbye! Have a great day!",
                "See you later!",
                "Goodbye! Take care!"
            ],
            "thanks": [
                "You're welcome!",
                "Happy to help!",
                "My pleasure!"
            ],
            "about": [
                "I am Jarvis, your AI assistant. I can help you with various tasks.",
                "I'm Jarvis, designed to make your tasks easier.",
            ],
            "unknown": [
                "I'm not sure about that. Would you like me to help you with something else?",
                "I don't have information about that. Is there something else I can help with?",
                "I'm still learning about that. Can I help you with something else?"
            ]
        }

    def say(self, text):
        """Text to speech function"""
        try:
            print("Jarvis:", text)
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Text-to-speech error: {e}")

    def get_response(self, query):
        """Generate appropriate response based on query"""
        query = query.lower()

        # Check for greetings
        if any(word in query for word in ["hello", "hi", "hey"]):
            return random.choice(self.responses["greeting"])

        # Check for farewell
        if any(word in query for word in ["bye", "goodbye", "exit", "quit"]):
            return random.choice(self.responses["farewell"])

        # Check for thanks
        if any(word in query for word in ["thank", "thanks"]):
            return random.choice(self.responses["thanks"])

        # Check for identity questions
        if any(phrase in query for phrase in ["who are you", "what are you", "what's your name"]):
            return random.choice(self.responses["about"])

        # Check for time
        if "time" in query:
            return f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}"

        # Check for date
        if "date" in query:
            return f"Today's date is {datetime.datetime.now().strftime('%B %d, %Y')}"

        # Check for calculations
        if any(word in query for word in ["calculate", "plus", "minus", "multiply", "divide"]):
            return self.handle_calculation(query)

        # Default response
        return random.choice(self.responses["unknown"])

    def handle_calculation(self, query):
        """Handle basic calculations"""
        try:
            # Extract numbers
            numbers = [int(s) for s in query.split() if s.isdigit()]
            if len(numbers) != 2:
                return "I need two numbers to perform a calculation."

            if "plus" in query or "add" in query:
                return f"The result is {numbers[0] + numbers[1]}"
            elif "minus" in query or "subtract" in query:
                return f"The result is {numbers[0] - numbers[1]}"
            elif "multiply" in query:
                return f"The result is {numbers[0] * numbers[1]}"
            elif "divide" in query:
                if numbers[1] == 0:
                    return "I cannot divide by zero."
                return f"The result is {numbers[0] / numbers[1]}"

            return "I'm not sure what calculation to perform."
        except:
            return "Sorry, I couldn't perform that calculation."

    def takeCommand(self):
        """Take microphone input from the user"""
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            try:
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                print("Recognizing...")
                query = r.recognize_google(audio, language="en-in")
                print(f"User said: {query}")
                return query.lower()
            except sr.UnknownValueError:
                return "none"
            except sr.RequestError:
                return "none"
            except Exception as e:
                print(f"An error occurred: {e}")
                return "none"

    def run(self):
        """Main execution function"""
        print('Welcome to Jarvis AI')
        self.say("Welcome to Jarvis AI")

        # Dictionary of sites and their URLs
        sites = {
            "youtube": "https://www.youtube.com",
            "chatgpt": "https://chat.openai.com",
            "gmail": "https://mail.google.com",
            "gemini": "https://gemini.google.com/app",
            "adobe firefly": "https://firefly.adobe.com/",
            "github": "https://github.com/dashboard",
            "replit": "https://replit.com/~",
            "vercel": "https://vercel.com/yatharths-projects-e2dfdb78",
            "netlify": "https://app.netlify.com/teams/devyatharth0-3vtjwr4/sites",
            "render": "https://dashboard.render.com/",
            "firebase": "https://console.firebase.google.com/u/0/",
            "instagram": "https://www.instagram.com/",
            "whatsapp": "https://web.whatsapp.com/"
        }

        # Dictionary of applications
        apps = {
            "chrome": "chrome.exe",
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "discord": "discord.exe",
            "spotify": "spotify.exe",
            "visual studio code": "code.exe",
            "pycharm": "pycharm64.exe",
            "git": "git-bash.exe",
            "zoom": "zoom.exe",
            "steam": "steam.exe",
            "obs": "obs64.exe",
            "winrar": "winrar.exe"
        }

        while True:
            try:
                query = self.takeCommand()

                if query == "none":
                    continue

                # Exit commands
                if any(word in query for word in ["exit", "quit", "goodbye", "bye"]):
                    self.say(random.choice(self.responses["farewell"]))
                    sys.exit()

                # Open websites
                site_opened = False
                for site, url in sites.items():
                    if f"open {site}" in query:
                        self.say(f"Opening {site}")
                        webbrowser.open(url)
                        site_opened = True
                        break
                if site_opened:
                    continue

                # Open applications
                app_opened = False
                for app, command in apps.items():
                    if f"open {app}" in query:
                        self.say(f"Opening {app}")
                        app_opened = self.open_application(app, command)
                        break
                if app_opened:
                    continue

                # Handle other queries
                response = self.get_response(query)
                self.say(response)

            except KeyboardInterrupt:
                self.say("Goodbye! Have a nice day!")
                sys.exit()

            except Exception as e:
                print(f"An error occurred: {e}")
                self.say("I encountered an error. Please try again.")

    def open_application(self, app_name, command):
        """Function to open applications with robust error handling and debugging."""
        try:
            # First, try to execute the command directly
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            # Debug logs (optional, toggle with DEBUG flag)
            DEBUG = False
            if DEBUG:
                print(f"Debug Output:\nSTDOUT: {stdout.decode().strip()}\nSTDERR: {stderr.decode().strip()}")

            # If the process executed successfully, return True
            if process.returncode == 0:
                return True

            # If direct command fails, search in common directories
            program_files = [
                os.environ.get('PROGRAMFILES', 'C:/Program Files'),
                os.environ.get('PROGRAMFILES(X86)', 'C:/Program Files (x86)'),
                os.environ.get('LOCALAPPDATA', ''),
                os.environ.get('APPDATA', ''),
                r"C:\Users\YourUsername\AppData\Local"  # Include specific Discord path
            ]

            for directory in program_files:
                for root, dirs, files in os.walk(directory):
                    if command.lower() in [f.lower() for f in files]:
                        full_path = os.path.join(root, command)
                        os.startfile(full_path)
                        return True

            # If no match is found, inform the user
            self.say(f"Sorry, I couldn't find {app_name}")
            return False

        except Exception as e:
            # Catch and log unexpected exceptions
            print(f"Error opening {app_name}: {e}")
            self.say(f"Sorry, I couldn't open {app_name}.")
            return False


if __name__ == "__main__":
    jarvis = JarvisAI()
    try:
        jarvis.run()
    except KeyboardInterrupt:
        jarvis.say("Goodbye! Have a nice day!")
        sys.exit()
