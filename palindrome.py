def is_palindrome(s):
    # Remove any non-alphanumeric characters and convert to lowercase for uniform comparison
    s = ''.join(e for e in s if e.isalnum()).lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]


print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False
print(is_palindrome("racecar"))  # Output: True
