if __name__ == '__main__':
    n = int(input())

l = []
for i in range(1, n+1):
    l.append(i)

print(*l, sep='')
