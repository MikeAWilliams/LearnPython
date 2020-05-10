def IsMultipleOf(num, multiple):
    return 0 == num % multiple

def IsMultipleOfThree(num):
    return IsMultipleOf(num, 3)

def IsMultipleOfFive(num):
    return IsMultipleOf(num, 5)

def FizzBuzz(num):
    if IsMultipleOfThree(num) and IsMultipleOfFive(num):
        return "fizzbuzz"
    if IsMultipleOfThree(num):
        return "fizz"
    if IsMultipleOfFive(num):
        return "buzz"
    return str(num)