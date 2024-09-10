import gradio as gr

from services.summarizer_translator_service import SummarizerTranslatorService


class SummarizerTranslatorView:
	def __init__(self, service: SummarizerTranslatorService):
		self.service = service

	def _get_language_list(self):
		languages = self.service.get_data_from_json()
		return languages.keys()

	@staticmethod
	def _get_inputs(languages: []):
		entries = [
			gr.Textbox(lines=5, label='Insira o texto'),
			gr.Dropdown(languages, value='English', label='Texto original'),
			gr.Dropdown(languages, value='Portuguese', label='Texto final')
		]
		return entries

	@staticmethod
	def _get_outputs():
		outputs = gr.Textbox(lines=5, label='Texto final')
		return outputs

	def create_gradio_interface(self):
		languages = self._get_language_list()
		entries = self._get_inputs(languages)
		outputs = self._get_outputs()
		title = 'Tradução e Resumo'
		descr = 'Esta aplicação resume e traduz o texto inserido.'

		app = gr.Interface(
			fn=self.service.translate_summary,
			inputs=entries,
			outputs=outputs,
			title=title,
			description=descr
		)

		app.launch(share=False)
