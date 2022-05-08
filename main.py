# 9.1 UNIT CONVERTER

km = float(input("Please write the decimal number like this: 1.0 "))


def unit_convert(km):
    mile = km * 0.621371192
    print(f"{mile} miles")


unit_convert(km)


# 9.2 FIZZBUZZ

def fizz_buzz(number):
    for num in range(1, number + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)


input_number = int(input("Write number between 1 and 100: "))
fizz_buzz(input_number)

"""
def single_fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return num


# num = int(input("Please put in number between 1 and 100: "))
# print(single_fizz_buzz(10))

assert single_fizz_buzz(5) == "buzz"
assert single_fizz_buzz(3) == "fizz"
assert single_fizz_buzz(15) == "fizzbuzz"

"""

# 9.3 MAKE STRING LOWERCASE

sentence = input("Write words here please: ")

print(sentence.lower())
