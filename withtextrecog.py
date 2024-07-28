import speech_recognition as sr
from better_profanity import profanity
def recognize_speech_multi_language(language):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Speak something...")
        
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        
        # Listen for speech
        audio = recognizer.listen(source)

       


        try:
            text = recognizer.recognize_google(audio, language=language)
            
            text= profanity.censor(text)
            return text, language
        except sr.UnknownValueError:
            print(f"Google Speech Recognition could not understand audio for {language}")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service for {language}; {e}")

    print("Could not recognize speech in any of the specified languages.")
    return None, None

