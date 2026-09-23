import sys

sys.path.append(r"..\day1_task")


def calculate_bill(units):
    if units <= 100:
        return units * 2
    elif units <= 200:
        return (100 * 2) + ((units - 100) * 3)
    else:
        return (100 * 2) + (100 * 3) + ((units - 200) * 5)


QUESTION = (
    "A household consumes 250 units of electricity. "
    "Calculate the electricity bill using the given slab rates."
)

print("Question:")
print(QUESTION)
print()

print("Step 1 - Identify the electricity units")
units = 250
print("Observation: Units consumed =", units)

print()
print("Step 2 - Calculate the first 100 units")

first_slab = 100 * 2
print("Calculation: 100 * ₹2")
print("Observation: ₹", first_slab)

print()
print("Step 3 - Calculate the next 100 units")

second_slab = 100 * 3
print("Calculation: 100 * ₹3")
print("Observation: ₹", second_slab)

print()
print("Step 4 - Calculate the remaining 50 units")

third_slab = 50 * 5
print("Calculation: 50 * ₹5")
print("Observation: ₹", third_slab)

print()
print("Step 5 - Calculate total bill")

total_bill = calculate_bill(units)

print("Calculation: ₹200 + ₹300 + ₹250")
print("Observation: ₹", total_bill)

print()
print("Final Answer:")
print(f"The electricity bill for {units} units is ₹{total_bill}.")