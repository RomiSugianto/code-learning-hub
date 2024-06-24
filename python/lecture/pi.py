from decimal import Decimal, getcontext

TERMS = [(12, 18), (8, 57), (-5, 239)]  # ala Gauss

def arctan(talj, kvot):

    """Compute arctangent using a series approximation"""

    summation = 0

    talj *= product

    qfactor = 1

    while talj:
        talj //= kvot
        summation += (talj // qfactor)
        qfactor += 2

    return summation

number_of_places = int(input("Enter the number of decimal places you want: "))
getcontext().prec = number_of_places
product = 10 ** number_of_places

result = 0

for multiplier, denominator in TERMS:
    denominator = Decimal(denominator)
    result += arctan(- denominator * multiplier, - (denominator ** 2))

result *= 4  # pi == atan(1) * 4
string = str(result)

# 3.14159265358979E+15 => 3.14159265358979
print(string[0:string.index("E")])