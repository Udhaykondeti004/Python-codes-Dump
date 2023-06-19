n = int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(n+65-j),end=" ")
    print()

print()

for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(n+65-i),end=" ")
    print()

