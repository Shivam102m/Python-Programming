#Write a Python function that takes in a list of numbers and returns the sum of the squares of all the numbers in the list.
def sum_of_squares(numbers):
    """
    Returns the sum of the squares of all the numbers in the given list.
    """
    return sum([num**2 for num in numbers])
