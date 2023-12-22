class Solution(object):
    def fizzBuzz(self, n):
        array = list(range(1, n+1))
        for i in range (len(array)):
            if array[i] % 15 == 0:
                array[i] = "FizzBuzz"
            elif array[i] % 3 == 0:
                array[i] = "Fizz"
            elif array[i] % 5 == 0:
                array[i] = "Buzz"
        array = [str(num) for num in array]
        return array
        