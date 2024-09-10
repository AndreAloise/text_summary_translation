# This is a sample Python script.
from ia_models.text_summary import TextSummary
from ia_models.text_translation import TextTranslation
from services.text_summary_service import TextSummaryService
from services.text_translation_service import TextTranslationService


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

BASE_TEXT = """
    Artificial intelligence (AI) is an area of computer science that emphasizes creating intelligent machines that work and react like humans.
    Some of the activities that computers with artificial intelligence are
    designed to do include: speech recognition, learning, planning and problem solving. The research associated with artificial intelligence is highly technical and specialized. The main problems of artificial intelligence include computer programming for certain traits such as knowledge,
    reasoning, problem solving, perception, learning, planning, skill
    to manipulate and move objects.
    """


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def create_summary():
    model = TextSummary()
    service = TextSummaryService(model)
    summary = service.summarize_text(BASE_TEXT)
    print(summary)

def translate_text():
    model = TextTranslation()
    service = TextTranslationService(model)
    translated_text = service.translate_text(BASE_TEXT)
    print(translated_text)

def translate_summary():
    model = TextSummary()
    service = TextSummaryService(model)
    summary = service.summarize_text(BASE_TEXT)
    model = TextTranslation()
    service = TextTranslationService(model)
    translated_text = service.translate_text(summary)
    print(f'Summary: {summary}\n'
          f'Translation: {translated_text}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # create_summary()
    # translate_text()
    translate_summary()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/