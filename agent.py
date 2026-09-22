from config import client, MODEL, COURSE_FEES, banner
from tools import get_fee, compare_fees, scholarship_fee

banner("AI Agent")

question = input("Ask a question: ")

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": """You are a helpful course-fee assistant.
Use the available course information to answer questions.
Course fees:
CS101 = ₹12000
AI202 = ₹18000
DS303 = ₹15000
"""
        },
        {"role": "user", "content": question}
    ],
)

print("Agent:", response.choices[0].message.content.strip())