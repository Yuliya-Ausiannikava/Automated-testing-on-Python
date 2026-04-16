def palindrome(num):
    """
    Checks if a number is a palindrome
    :param num: integer
    :return: boolean
    """
    num = str(num)
    if num == num[::-1]:
        return True
    return False


assert palindrome(121) is True
assert palindrome(1001) is True
assert palindrome(10) is False
assert palindrome(0) is True
assert palindrome(-121) is False
