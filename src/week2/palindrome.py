class Palindrome:
    # function to check string is
    # palindrome or not
    def isPalindrome(s):

        # Using predefined function to
        # reverse to string print(s)
        rev = ''.join(reversed(s))

        # Checking if both string are
        # equal or not
        if (s == rev):
            return True
        return False

    # main function
    s = input(str("Enter a word and I will determine whether or not it is a Palindrome: "))
    ans = isPalindrome(s)

    if (ans):
        print("That is a Palindrome")
    else:
        print("That is not a Palindrome")