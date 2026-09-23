from config import client, MODEL


QUESTIONS = [
    "Three courses cost ₹12,000, ₹18,000 and ₹15,000. "
    "A 15% scholarship is given. The remaining amount is paid "
    "in 4 equal instalments. How much is each instalment?",

    "There are 18 computers in a lab. Each computer is used by "
    "2 students in the morning and 3 students in the afternoon. "
    "How many student sittings are there in total?",

    "Ravi is taller than Kumar. Kumar is taller than Arun. "
    "Priya is shorter than Arun. Who is the tallest and who is the shortest?"
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