from collections import Counter

from config import client, MODEL
from cot_compare import QUESTIONS, COT_PROMPT


RUNS = 5
TEMPERATURE = 0.8


def final_answer(text):
    for line in text.splitlines():
        if line.strip().lower().startswith("final answer:"):
            return line.split(":", 1)[1].strip()

    return text.strip()


def run_many(question):
    answers = []

    for i in range(RUNS):
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": COT_PROMPT},
                {"role": "user", "content": question}
            ],
            temperature=TEMPERATURE
        )

        answer = final_answer(response.choices[0].message.content)
        answers.append(answer)

        print(f"Run {i + 1}: {answer}")

    return answers


for i, question in enumerate(QUESTIONS, start=1):
    print("=" * 60)
    print(f"QUESTION {i}")
    print("=" * 60)
    print(question)
    print()

    answers = run_many(question)

    counts = Counter(answers)
    majority_answer, majority_count = counts.most_common(1)[0]

    print()
    print("Answers seen:")
    for answer, count in counts.items():
        print(f"{answer} -> {count} time(s)")

    print()
    print("Majority Answer:", majority_answer)
    print("Majority Count:", majority_count)
    print()