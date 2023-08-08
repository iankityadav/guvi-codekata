key = set(list('aeiou'))
for i in input():
    if i.lower() in key:
        continue
    print(i,end='')