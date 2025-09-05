import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)

def clean_text(text):
    # Lowercase
    text = text.lower()
    # Remove punctuation/numbers
    text = re.sub(r'[^a-z\s]', '', text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in text.split() if word not in stop_words]
    return " ".join(words)
