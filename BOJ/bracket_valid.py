import sys
from collections import deque
arr = sys.stdin.readline().split()

input_list = list()
in_list = ['{', '<', '[', '(']

def valid_configure():
    for value in arr:
        if value in in_list:
            input_list.append(value)
        else:
            if not input_list:
                return False
            else:
                in_value = input_list.pop()
                if in_value == '{' and value != '}':
                    return False
                elif in_value == '[' and value != ']':
                    return False
                elif in_value == '<' and value != '>':
                    return False
                elif in_value == '(' and value != ')':
                    return False
    return True
print(valid_configure())