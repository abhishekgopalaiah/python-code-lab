def is_valid(s: str) -> bool:
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


if __name__ == '__main__':
    print(is_valid("({[]})"))  # Output: True
