"""
This is the code to complete the "Sequence" task.
"""

def solution(sequence):
    def increase(list):
        """
        This function checks if the numbers are increasing.
        arg list: list of numbers
        return: boolean
        """
        for i in range(len(list) - 1):
            if list[i] >= list[i + 1]:
                return False
        return True

    # Checking a list after excluding one element
    for item in range(len(sequence) - 1):
        if sequence[item] >= sequence[item + 1]:
            without_item = sequence[:item] + sequence[item + 1:]
            without_item_next = sequence[:item + 1] + sequence[item + 2:]
            # We pass the lists obtained after removing one element as an argument to the function "increase"
            if increase(without_item_next) or increase(without_item):
                return True
            return False
    return True

assert solution([1, 2, 3]) == True
assert solution([1, 2, 1, 2]) == False
assert solution([1, 3, 2, 1]) == False
assert solution([1, 2, 3, 4, 5, 3, 5, 6]) == False
assert solution([40, 50, 60, 10, 20, 30]) == False
