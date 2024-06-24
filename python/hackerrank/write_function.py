def is_leap(year):
    leap = "False"

    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = "True 1"
            else:
                leap = "False 1"
        else:
            leap = "True 2"
    return leap


year = int(input())
print(is_leap(year))