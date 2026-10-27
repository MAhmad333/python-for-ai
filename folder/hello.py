# Functions operate on data
def clean_text(text):
    return text.strip().lower()

def remove_punctuation(text):
    return text.replace(".", "").replace(",", "")

# Chain functions together
result = remove_punctuation(clean_text("  Hello, World.  "))