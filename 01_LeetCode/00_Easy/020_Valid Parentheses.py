def is_valid(s: str) -> bool:
    stack = []
    hash_map = {')': '(', ']': '[', '}': '{'}

    # Loop through each character in the string
    for char in s:
        if char in hash_map:

            if stack and stack[-1] == hash_map[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return not stack


a = "]()]()"
print(is_valid(a))
