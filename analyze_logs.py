import openai
import sys
import os


def get_chatgpt_analysis(test_logs):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Тесты упали. Вот логи:\n{test_logs}\nЧто могло пойти не так и какие шаги для устранения проблемы?",
        max_tokens=150,
    )
    return response.choices[0].text.strip()


if __name__ == "__main__":
    # Получаем логи тестов из аргументов командной строки
    test_logs = sys.argv[1]

    analysis = get_chatgpt_analysis(test_logs)
    print("ChatGPT Analysis:")
    print(analysis)
