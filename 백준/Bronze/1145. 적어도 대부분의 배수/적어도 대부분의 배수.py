n = list(map(int, input().split()))
multiple = min(n)
while True:
    cnt = 0
    for i in range (5):
        if multiple%n[i] == 0:
            cnt+=1
    if cnt>2:
        print(multiple)
        break
    multiple+=1