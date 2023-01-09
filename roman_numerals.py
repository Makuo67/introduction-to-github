def roman(string):
    """Create a dictionary of the numerals with their values"""
    numerals = { "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
                "G": 5000,
                "H": 10000}
    """Get the string numeral
    Check if it's in the numerals dictionary and append the value to a list, otherwise return Invalid numeral"""
    value_list = []
    for letter in string:
        letter = letter.upper()
        if letter not in numerals:
            raise ValueError("Invalid numeral")

        else:
            num_value = numerals[letter]
            value_list.append(num_value)

    """Iterate through the list, if a number is less than the next following number, change it to negative
    Return a new list of the values"""
    next_index = 1
    new_list = []

    for i in value_list:
        if next_index >= len(value_list):
            new_list.append(value_list[-1])
            break

        if i < value_list[next_index]:
            new_list.append(-i)
            next_index += 1
        else:
            new_list.append(i)

            next_index += 1

    """Sum the list"""
    Sum  = sum(new_list)
    return Sum
print(roman("xl"))

