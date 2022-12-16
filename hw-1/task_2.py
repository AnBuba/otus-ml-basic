def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        text_result = "YOU SHALL PASS"
    else:
        text_result = "YOU SHALL NOT PASS"
    return text_result

assert leap_year(5) == 'YOU SHALL NOT PASS'