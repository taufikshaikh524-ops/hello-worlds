import speech_recognition as sr
import pyttsx3
import datetime

# Step 1: Create recognizer and speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Step 2: Define speak() function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Step 3: Define listen() function (so we can reuse it)
def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("🧠 You said:", text)
        return text.lower()  # Return what you said
    except sr.UnknownValueError:
        print("❌ Sorry, I didn’t understand.")
        return ""  # Empty means didn’t understand
    except sr.RequestError:
        print("⚠️ Speech service not available.")
        return ""

# Step 4: Keep the assistant running
while True:
    command = listen()

    if "hello" in command:
        speak("Hi there!")
    elif "your name" in command:
        speak("My name is Mini Jarvis.")
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
    elif "stop" in command or "exit" in command:
        speak("Goodbye!")
        break
    elif command != "":
        speak("I didn’t hear a known command.")
