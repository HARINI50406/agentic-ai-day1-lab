from config import COURSE_FEES


def get_fee(course):
    return COURSE_FEES.get(course.upper(), "Course not found")


def compare_fees(course1, course2):
    fee1 = COURSE_FEES.get(course1.upper())
    fee2 = COURSE_FEES.get(course2.upper())

    if fee1 is None or fee2 is None:
        return "Course not found"

    difference = abs(fee1 - fee2)

    if fee1 > fee2:
        return f"{course1} is more expensive by ₹{difference}"
    elif fee2 > fee1:
        return f"{course2} is more expensive by ₹{difference}"
    else:
        return "Both courses have the same fee"


def scholarship_fee(course1, course2, percentage):
    fee1 = COURSE_FEES.get(course1.upper(), 0)
    fee2 = COURSE_FEES.get(course2.upper(), 0)

    total = fee1 + fee2
    discount = total * percentage / 100
    final_fee = total - discount

    return final_fee