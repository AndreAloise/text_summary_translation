from transformers import pipeline


class TextTranslation:
	def __init__(self, source="eng_Latn", target="por_Latn"):
		self._pipe = pipeline(
			"translation",
			model="facebook/nllb-200-distilled-600M",
			src_lang=source,
			tgt_lang=target,
			trust_remote_code=True
		)

	def get_pipeline(self):
		return self._pipe