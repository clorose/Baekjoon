passenger = 0
max_passenger = 0

for i in range(1, 10):
    train_out, train_in = map(int, input().split())
    passenger += train_in - train_out
    if passenger > max_passenger:
        max_passenger = passenger
print(max_passenger)