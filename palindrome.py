def ispalindrome(s):
    try:
        if isinstance(s,str):
            a = s[0::]
            b = s[::-1]
            if a==b:
                print('given value is palindrome')
            else:
                print('not a palindrome')
         else:
            raise ValueError('Data Type not supported')
