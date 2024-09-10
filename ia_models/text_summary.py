from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class TextSummary:
	def __init__(self):
		model_name = "facebook/bart-large-cnn"
		self._tokenizer = AutoTokenizer.from_pretrained(model_name)
		self._model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

	def get_tokenizer(self):
		return self._tokenizer

	def get_model(self):
			return self._model