import json
from pathlib import Path

from ia_models.text_translation import TextTranslation
from services.text_translation_service import TextTranslationService


class SummarizerTranslatorService:
	def __init__(self, summary_service):
		self._summary_service = summary_service

	@staticmethod
	def get_data_from_json():
		file_path = Path('data_files/translator_languages.json')
		with file_path.open('r', encoding='utf-8') as file:
			data = json.load(file)

		return data

	def _get_languages_from_json(self, source: str, target: str) -> tuple[str, str]:
		data = self.get_data_from_json()
		return data.get(source), data.get(target)

	def translate_summary(self, text, source: str, target: str):
		languages = self._get_languages_from_json(source, target)
		lan_source = languages[0]
		lan_target = languages[1]

		summary = self._summary_service.summarize_text(
			text) if lan_source == "eng_Latn" else self._get_summary_from_translated_text_to_english(lan_source, text)

		translation_model_from_english = TextTranslation("eng_Latn", lan_target)
		translate_service = TextTranslationService(translation_model_from_english)
		translated_summary_from_english = translate_service.translate_text(summary, 512)

		return translated_summary_from_english

	def _get_summary_from_translated_text_to_english(self, lan_source: str, text):
		translation_model_to_english = TextTranslation(lan_source, "eng_Latn")
		translate_service = TextTranslationService(translation_model_to_english)
		translated_to_english_text = translate_service.translate_text(text, 512)
		summary = self._summary_service.summarize_text(translated_to_english_text, 300)
		return summary
