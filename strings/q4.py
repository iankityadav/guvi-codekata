s = input()
d = {}
for i in s:
    d[i] = d.get(i,0) + 1

ans = ''    
for i in d:
    if d[i] > 1:
        continue
    ans +=i
print(ans)        