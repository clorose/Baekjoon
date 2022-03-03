import sys
def push(x):
    stack.append(x)
def pop():
    if(not stack):
        return -1
    else:
        return stack.pop()
def size():
    return len(stack)
def empty():
    if(not stack):
        return 1
    else:
        return 0
def top():
    if(not stack):
        return -1
    else:
        return stack[-1]
N = int(input())
stack = list()

for i in range(N):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "push":
        push(command[1])
    elif command[0] == "pop":
        print(pop())
    elif command[0] == "size":
        print(size())
    elif command[0] == "empty":
        print(empty())
    elif command[0] == "top":
        print(top())
