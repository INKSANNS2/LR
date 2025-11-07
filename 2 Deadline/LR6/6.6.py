def is_palindrome(text):
    clean_text = text.lower().replace(" ", "")
    return clean_text == clean_text[::-1]
print(is_palindrome("А роза упала на лапу Азора"))