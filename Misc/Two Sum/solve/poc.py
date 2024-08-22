lines = []
row = []
prime = 10273 
# 20753 also not bad
for i in range(1,10000-40):
    row.append(str(i*10273))
    if i % 10 == 0:
        lines.append('1')
        lines.append(' '.join(row))
        row.clear()
        
lines.append('2')
print(len(lines))
with open('input.txt', 'w') as f:
    f.write('\n'.join(lines))

