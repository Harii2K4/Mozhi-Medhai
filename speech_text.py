import speech_recognition as sr

def speech_to_text():
    # Create a recognizer object
    recognizer = sr.Recognizer()
    languages = ['en-IN', 'hi-IN', 'ta-IN']

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening... Speak now.")
        
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        
        # Listen for audio input
        audio = recognizer.listen(source)

    try:
        # Use Google Speech Recognition to convert audio to text
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")




