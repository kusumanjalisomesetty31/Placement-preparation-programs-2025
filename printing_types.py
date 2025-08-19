def check_type(num_str):
    digits = list(map(int, num_str))
    is_ascending = all(digits[i] <= digits[i+1] for i in range(len(digits)-1))
    is_descending = all(digits[i] >= digits[i+1] for i in range(len(digits)-1))
    has_repeats = len(set(digits)) != len(digits)

    # Type 1: Ascending with repeats
    if is_ascending and has_repeats and (len(set(digits)) != 1):
        return "Type1"
    # Type 2: Descending with repeats
    elif is_descending and has_repeats and (len(set(digits)) != 1) :
        return "Type2"
    # Type 3: Single repeating digit (all same digit)
    elif len(set(digits)) == 1:
        return "Type3"
    # Type 4: Ascending without repeats
    elif is_ascending and not has_repeats:
        return "Type4"
    # Type 5: Descending without repeats
    elif is_descending and not has_repeats:
        return "Type5"
    # Type 6: None of the above
    else:
        return "Type6"


# Main program
n = int(input("Enter number of elements: "))
numbers = [input(f"Enter number {i+1}: ") for i in range(n)]

# Store types in array
types = [check_type(num) for num in numbers]

# Print them space-separated (no list, no quotes)
print("\nOutput:")
print(" ".join(types))