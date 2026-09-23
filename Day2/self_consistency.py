from collections import Counter

from config import client, MODEL


QUESTIONS = [
    "A household consumes 150 units of electricity. "
    "The first 100 units cost ₹2 per unit and the next units cost "
    "₹3 per unit. Calculate the total electricity bill.",

    "A household consumes 220 units of electricity. "
    "The first 100 units cost ₹2 per unit, the next 100 units cost "
    "₹3 per unit, and units above 200 cost ₹5 per unit. "
    "Calculate the total electricity bill.",

    "A household consumes 300 units of electricity. "
    "The first 100 units cost ₹2 per unit, the next 100 units cost "
    "₹3 per unit, and units above 200 cost ₹5 per unit. "
    "Calculate the total electricity bill."
]


COT_PROMPT = (
    "You are a helpful assistant. Solve the problem step by step. "
    "Number each step and show the calculation in that step. "
    "After the steps, write the last line exactly as: "
    "Final Answer: <answer>"
)


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

        answer = final_answer(
            response.choices[0].message.content
        )

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
    