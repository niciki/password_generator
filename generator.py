import random, string
count, length = int(input()), int(input())
l = length
for i in range(count):
    s = set()
    l1, l2, l3 = [0 for i in range(3)]
    while l3 == 0 or l3 > l * 2 / 5:
        length = l
        l1 = random.randint(length // 8, length - int(length * 2 /3))
        length -= l1
        l2 = random.randint(length // 4, length // 2)
        length -= l2
        l3 = length
    for i in range(l1):
        if i <= len(list(set(string.ascii_uppercase) - {'O', 'I'})):
            q = random.choice(list(set(string.ascii_uppercase) - {'O', 'I'}))
            while q in s:
                q = random.choice(list(set(string.ascii_uppercase) - {'O', 'I'}))
            s.add(q)
        else:
            s.add(random.choice(list(set(string.ascii_uppercase) - {'O', 'I'})))
    for i in range(l2):
        if i <= len(list(set(string.ascii_lowercase) - {'o', 'l'})):
            q = random.choice(list(set(string.ascii_lowercase) - {'o', 'l'}))
            while q in s:
                q = random.choice(list(set(string.ascii_lowercase) - {'o', 'l'}))
            s.add(q)
        else:
            s.add(random.choice(list(set(string.ascii_lowercase) - {'o', 'l'})))
    for i in range(l3):
        if i <= 7:
            q = str(random.choice([2, 3, 4, 5, 6, 7, 8, 9]))
            while q in s:
                q = str(random.choice([2, 3, 4, 5, 6, 7, 8, 9]))
            s.add(q)
        else:
            s.append(str(random.choice([2, 3, 4, 5, 6, 7, 8, 9])))
    s = list(s)
    random.shuffle(s)
    print(''.join(s))
