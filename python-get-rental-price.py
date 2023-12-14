# Get rental price
short_term_cost = 50  # days 1-3
medium_term_cost = 40  # days 4-7
long_term_cost = 30  # days 8-...


def get_rental_price(number_of_days: int) -> float:
    if number_of_days >= 8:
        price = ((number_of_days - 7) * 30) + (4 * 40) + (3 * 50)
    elif number_of_days >= 4:
        price = ((number_of_days - 3) * 40) + (3 * 50)
    else:
        price = number_of_days * 50
    return price


print(f"Rental price = {get_rental_price(9)}$")
