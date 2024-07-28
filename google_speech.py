from typing import List
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech

def transcribe_multiple_languages_v2(
    project_id: str,
    language_codes: List[str],
    audio_file: str,
) -> cloud_speech.RecognizeResponse:
    """Transcribe an audio file in multiple languages."""
    client = SpeechClient()
    lang={}

    with open(audio_file, "rb") as f:
        content = f.read()

    for i in language_codes:
     config = cloud_speech.RecognitionConfig(
        auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
        language_codes=[i],  # This should now correctly use all specified languages
        model="latest_long",
    )
     request = cloud_speech.RecognizeRequest(
         recognizer=f"projects/{project_id}/locations/global/recognizers/_",
        config=config,
        content=content,
    )
     response = client.recognize(request=request)
     for i, result in enumerate(response.results):
        lang[i] = result.alternatives[0].confidence




    return lang

# Usage
response = transcribe_multiple_languages_v2(
    "speech-to-speech-hackathon",
    ["en-US", "ta-IN", "hi-IN"],
    "/content/test.wav"
)
print(response)