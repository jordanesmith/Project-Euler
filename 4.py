'''project euler task 4'''

list_of_numbers = []
for i in range(100,999):
    j = i
    while j < 999:
        list_of_numbers.append(i*j)
        j += 1

set_of_numbers = set(list_of_numbers)
palindrome_list = []

for three_digit_number in set_of_numbers:
    string_of_digit = str(three_digit_number)
    if string_of_digit[0] == string_of_digit[-1]:
        if string_of_digit[1] == string_of_digit[-2]:
            if string_of_digit[2] == string_of_digit[-3]:
                palindrome_list.append(string_of_digit)
            elif len(string_of_digit) == 5:
                palindrome_list.append(string_of_digit)

palindrome_list.sort(key=int)
print(palindrome_list[-1])