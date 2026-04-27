n,m = map(int, input().split())
grid = [input().split() for _ in range(n)]

r = 0
for i in grid:
    id = 0
    for j in i:
        if j == "*":
            try:
                if not grid[r + 1][id] == "*":
                    grid[r + 1][id] = "x"
            except:pass
        id += 1
    r += 1

r = 0
for i in grid:
    id = 0
    for j in i:
        if j == "*":
            try:
                if grid[r + 1][id] == "x":
                    grid[r + 1][id] = "*"
            except:pass
        id += 1
    r += 1
    
for r in grid:
    print(' '.join(str(cell) for cell in r))