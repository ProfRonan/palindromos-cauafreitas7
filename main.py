"""Main functions"""
import re

def is_palindrome(string: str) -> bool:
    """Check if string is palindrome."""
    string = string.lower()
    string = re.sub(r'[^\w\s]','',string)
    string = (string.replace("", ""))

    newstr = ""
    for i in range(len(string)-1, -1, -1):
        newstr = newstr + string[i]
    if newstr == string:
        return True
    else:
        return False
    
if __name__ == "__main__":
    n = str (input('N: '))
    print(is_palindrome(n))    
