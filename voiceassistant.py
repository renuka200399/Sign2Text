import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Function to speak the input text
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    # Take input from the user via terminal
    text_input = input("Enter the text you want to convert to speech: ")
    
    # Convert the entered text to speech
    text_to_speech(text_input)
