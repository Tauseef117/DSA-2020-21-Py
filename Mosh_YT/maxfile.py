#class Find:
def max(numbers):
        large = numbers[0]
        for i in numbers:
            if i > large:
                large = i
        return large