from sys import argv


def check_match(s):
    stack = []
    for e in s:
        if not stack or e == '{':
            stack.append(e)
        else:
            if stack[-1] == '{':
                stack.pop()
            else:
                stack.append(e)

    return not stack

if __name__ == '__main__':
    l = len(argv)
    if l == 1:
        print('Error: no data input')
    else:
        print(check_match(argv[1]))
