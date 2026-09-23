import sys

sys.path.append(r"..\lab day 1")

from config import client, MODEL, COURSE_FEES
from tools import get_fee, scholarship_fee


QUESTION = (
    "Which is cheaper: CS101 and AI202 with a 10% scholarship, "
    "or all three courses with a 25% scholarship? By how much?"
)

print("Question:")
print(QUESTION)
print()

# Step 1: Get course fees
print("Step 1 - Get course fees")

cs101 = get_fee("CS101")
print("Observation: CS101 =", cs101)

ai202 = get_fee("AI202")
print("Observation: AI202 =", ai202)

ds303 = get_fee("DS303")
print("Observation: DS303 =", ds303)

# Step 2: Calculate first option
print()
print("Step 2 - Calculate first option")

first_option = (cs101 + ai202) * 0.90
print("Calculation: (12000 + 18000) * 0.90")
print("Observation:", first_option)

# Step 3: Calculate second option
print()
print("Step 3 - Calculate second option")

second_option = (cs101 + ai202 + ds303) * 0.75
print("Calculation: (12000 + 18000 + 15000) * 0.75")
print("Observation:", second_option)

# Step 4: Compare
print()
print("Step 4 - Compare the two options")

difference = second_option - first_option
print("Calculation:", second_option, "-", first_option)
print("Observation:", difference)

print()
print("Final Answer:")
print(
    f"CS101 + AI202 with a 10% scholarship costs ₹{first_option:.2f}."
)
print(
    f"All three courses with a 25% scholarship costs ₹{second_option:.2f}."
)
print(
    f"The first option is cheaper by ₹{difference:.2f}."
)