def preprocess_text(text):  
    text = text.lower()
    
    text = ''.join(char for char in text if char.isalnum() or char.isspace())
    
    
    text = text.strip()
    
    return text

def split_into_sentences(text):
    sentences = text.split('.')
    return [sentence.strip() for sentence in sentences if sentence.strip()]