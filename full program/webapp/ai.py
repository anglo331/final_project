from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import ollama


def llm_init(path: str = '') -> bool:
    """
    path is the path for the modefile
    """
    llms = ollama.list()

    found_llms = [modle['name'] for modle in llms['models']]

    if not 'llama3:8b' in found_llms:
        ollama.pull('llama3:8b')

    if not 'delta_llm' in found_llms:
        status = ollama.create(model='delta_llm',
                               path=path)
        return (True)

    found_llms = [modle['name'] for modle in llms['models']]
    return (found_llms, False)


def simplechat(prompt: str):

    llm = Ollama(model='delta_llm')

    _prompt = ChatPromptTemplate.from_messages([
        ('system', 'your name is delta-chat-bot and you are helping people to find the best phone that fits there needs and your response should not exceeds 100 word'),
        ('user', '{userInput}')
    ])

    chain = _prompt | llm | StrOutputParser()

    print(f'i recived {prompt=}')
    return chain.stream(prompt)


if __name__ == "__main__":
    # for chunk in simplechat('hi'):
    #     print(chunk, end='', flush=True)
    llm_init()
