def reverse_words(s: str) -> str:
    words = s.split()
    words = [word[::-1] for word in words]
    return ' '.join(words)


s1 = "Mr Ding"
print(reverse_words(s1))