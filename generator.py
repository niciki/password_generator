import random, string
count, length = int(input()), int(input())
l = length
for i in range(count):
    s = []
    length = l
    l1 = random.randint(1, length - 2)
    length -= l1
    l2 = random.randint(1, length - 1)
    length -= l2
    l3 = length
    for i in range(l1):
        s.append(random.choice(list(set(string.ascii_uppercase) - {'O', 'I'})))
    for i in range(l2):
        s.append(random.choice(list(set(string.ascii_lowercase) - {'o', 'l'}))) 
    for i in range(l3):
        s.append(str(random.choice([2, 3, 4, 5, 6, 7, 8, 9])))
    random.shuffle(s)
    print(''.join(s))
