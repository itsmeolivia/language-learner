from textblob import TextBlob

def to_english(message, original_language=None):

	blob = TextBlob(text)

	if original_language is not None:
		return blob.translate(from_lang=original_language, to="en")
	else:
		return blob.translate(to="en")