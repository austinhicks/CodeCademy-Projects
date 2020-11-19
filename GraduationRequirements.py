# Testing Nested Functions in graduation_reqs
# 11/18/2020

# Define the nested functions:

# Check the credits
def check_creds(x):
    if (x >= 120):
        return True

# Check the GPA
def check_gpa(x):
    if (x >= 2.0):
        return True

def graduation_reqs(gpa, credits):
    # GPA >= 2.0 AND Credits >= 120
    if check_gpa(gpa) and check_creds(credits):
        return 'You meet the requirements to graduate!'
    # GPA >= 2.0 AND Credits < 120
    if check_gpa(gpa) and not check_creds(credits):
        return 'You do not have enough credits to graduate.'
    # GPA < 2.0 AND Credits >= 120
    if not check_gpa(gpa) and check_creds(credits):
        return 'Your GPA is not high enough to graduate.'
    # GPA < 2.0 AND Credits < 120
    if not check_gpa(gpa) and not check_creds(credits):
        return 'You do not meet either requirement to graduate!'


# Test with print/function calls

print(graduation_reqs(2.0, 120))
print(graduation_reqs(2.0, 119))
print(graduation_reqs(1.7, 120))
print(graduation_reqs(1.0, 10))