def is_palindrome(word):
    cleaned = ''.join(c.lower() for c in word if c.isalnum())
    return cleaned == cleaned[::-1]
