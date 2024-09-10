from ia_models.text_translation import TextTranslation


class TextTranslationService:
	def __init__(self, model: TextTranslation):
		self.model = model

	def translate_text(self, text: str):
		length = 200
		translated_text = self.model.get_pipeline()(text, max_length=length)
		return translated_text[0].get('translation_text')