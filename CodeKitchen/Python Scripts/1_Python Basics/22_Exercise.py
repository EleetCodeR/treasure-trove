# divisible by 3 - fizz , by 5 - Buzz , by both - fizzbuzz, any other - return same input.

# def Fizz_Buzz(number):
#     number = int(number)
#     if number % 3 == 0 and number % 5 == 0:
#         result = "FizzBuzz"
#     elif number % 5 == 0:
#         result = "Buzz"
#     elif number % 3 == 0:
#         result = "Fizz"
#     else:
#         result = number
#     return result


# print(Fizz_Buzz(9))

# NOTE: Better code of above logic would be:

def Fizz_Buzz(number):
    if (number % 3 == 0)and(number % 5 == 0):
        return "FizzBuzz"
    if number % 3 == 0:
        return "Frizz"
    if number % 5 == 0:
        return "Buzz"
    return number


print(Fizz_Buzz(9))
