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


DIRECT_PROMPT = (
    "You are a helpful assistant. Give only the final answer. "
    "Do not explain."
)


COT_PROMPT = (
    "You are a helpful assistant. Solve the problem step by step. "
    "Number each step and show the calculation in that step. "
    "After the steps, write the last line exactly as: "
    "Final Answer: <answer>"
)


def ask(question, prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": question}
        ],
        temperature=0
    )

    return response.choices[0].message.content


for i, question in enumerate(QUESTIONS, start=1):

    print("=" * 60)
    print(f"QUESTION {i}")
    print("=" * 60)

    print(question)
    print()

    print("WITHOUT CHAIN-OF-THOUGHT:")

    direct_answer = ask(question, DIRECT_PROMPT)

    print(direct_answer)
    print()

    print("WITH CHAIN-OF-THOUGHT:")

    cot_answer = ask(question, COT_PROMPT)

    print(cot_answer)
    print()
    