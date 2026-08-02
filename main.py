
from ollama import chat
from ollama import ChatResponse


AI_MODEL = 'deepseek-r1:1.5b'
PROMPT = "Why is the sky blue?"


def main():

    response: ChatResponse = chat(model=AI_MODEL, messages=[
    {
        'role': 'user',
        'content': PROMPT,
    },
    ])

    print(response.message.content)

if __name__ == "__main__":

    main()
