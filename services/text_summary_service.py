import re

from ia_models.text_summary import TextSummary


class TextSummaryService:
	def __init__(self, model: TextSummary):
		self._model = model

	def summarize_text(self, text: str, output_max_length: int = 200):
		processed_text = self._get_processed_text_without_white_space(text)

		input_ids = self._model.get_tokenizer()(
			[processed_text],
			return_tensors="pt",
			padding="max_length",
			truncation=True,
			max_length=1024,
		)["input_ids"]

		output_ids = self._model.get_model().generate(
			input_ids=input_ids,
			max_length=output_max_length,
			no_repeat_ngram_size=2,
			num_beams=4
		)[0]

		summary = self._model.get_tokenizer().decode(
			output_ids,
			skip_special_tokens=True,
			clean_up_tokenization_spaces=False
		)
		return summary

	@staticmethod
	def _get_processed_text_without_white_space(text: str):
		handler = lambda k: re.sub(r'\s+', ' ', re.sub(r'\n+', ' ', k.strip()))
		processed_text = handler(text)
		return processed_text
