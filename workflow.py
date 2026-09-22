from config import client, MODEL, COURSE_FEES, banner

banner("Rule-Based Workflow")

for course, fee in COURSE_FEES.items():
    print(f"{course}: ₹{fee}")

print()

question = "What is the total fee for CS101 and AI202 after a 10% scholarship?"

print("User:", question)

total = COURSE_FEES["CS101"] + COURSE_FEES["AI202"]
discount = total * 0.10
final_fee = total - discount

print(f"Total before scholarship: ₹{total}")
print(f"Scholarship: ₹{discount}")
print(f"Final fee: ₹{final_fee}")