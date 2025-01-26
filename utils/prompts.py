from langchain.prompts import PromptTemplate

class Prompts:
    def __init__(self):
        self.general_template = PromptTemplate(
            input_variables=["question"],
            template="Ты ассистент кардиолог. Ответь на вопрос пациента: {question}. Дай ответ краткий и понятный.",
        )

    def get_general_prompt(self):
        return self.general_template