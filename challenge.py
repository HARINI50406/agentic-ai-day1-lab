from config import client, MODEL, COURSE_FEES, banner

banner("Challenge")

question = input("Ask a course-fee question: ")

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": """You are a course-fee assistant.
Available courses and fees:
CS101 = ₹12000
AI202 = ₹18000
DS303 = ₹15000

Answer clearly and show calculations when needed."""
        },
        {
            "role": "user",
            "content": question
        }
    ],
)

print("Answer:", response.choices[0].message.content.strip())