from transformers import pipeline


class TextTranslation:
	def __init__(self):
		self._pipe = pipeline(
			"translation",
			model="facebook/nllb-200-distilled-600M",
			src_lang="eng_Latn",
			tgt_lang="por_Latn",
			trust_remote_code=True
		)

	def get_pipeline(self):
		return self._pipe