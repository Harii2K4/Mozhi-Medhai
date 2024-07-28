import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def filter_ethical_words(text):
    # Azure setup
    key = os.environ["c852dc84217149ea80c0e8e51f84e1c4"]
    endpoint = os.environ["https://filterrecognition.cognitiveservices.azure.com/"]
    azure_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    # Split text into words
    words = text.split()

    # Analyze sentiment for ethical filtering
    results = azure_client.analyze_sentiment(words)

    ethical_words = []
    non_ethical_words = []

    for result in results:
        if result.confidence_scores.positive > 0.6:
            ethical_words.append(result.id)
        elif result.confidence_scores.negative > 0.6:
            non_ethical_words.append(result.id)

    return {
        "ethical_words": ethical_words,
        "non_ethical_words": non_ethical_words
    }

if __name__ == "__main__":
    # Example usage
    sample_text = "honesty kindness deceit compassion theft integrity greed generosity"
    result = filter_ethical_words(sample_text)
    print("Ethical words:", result["ethical_words"])
    print("Non-ethical words:", result["non_ethical_words"])