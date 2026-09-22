from config import client, MODEL, QUESTIONS, banner

banner("Simple Chatbot")

for question in QUESTIONS:
    print("User:", question)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": question}
        ],
    )

    answer = response.choices[0].message.content.strip()
    print("Bot:", answer)
    print()