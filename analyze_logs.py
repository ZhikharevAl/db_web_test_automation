import sys
import openai
import os


def get_chatgpt_analysis(test_logs):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "sdet",
                "content": f"Тесты упали. Вот логи:\n{test_logs}\n"
                f"Что могло пойти не так и какие шаги для устранения проблемы?",
            },
        ],
    )
    return response.choices[0].message["content"].strip()


if __name__ == "__main__":
    test_logs = sys.argv[1]
    analysis = get_chatgpt_analysis(test_logs)
    print("ChatGPT Analysis:")
    print(analysis)
