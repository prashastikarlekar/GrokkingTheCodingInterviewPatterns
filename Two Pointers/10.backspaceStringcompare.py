# https://leetcode.com/problems/backspace-string-compare/

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

def compareString(x):
    stack = []
    for i in x:
        if i != '#':
            stack.append(i)
        elif stack:
            stack.pop()
    return "".join(stack)


if __name__ == "__main__":
    s = "ab##"
    t = "c#d#"
    print(compareString(s) == compareString(t))
