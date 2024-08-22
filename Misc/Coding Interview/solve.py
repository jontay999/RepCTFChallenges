lines = []
row = []
for i in range(1,10001):
    row.append(i*10273)
    if i % 10 == 0:
        lines.append(row[:])
        row.clear()
        lines.append([1])

    
with open('input.txt', 'w') as f:
    f.writelines(lines)