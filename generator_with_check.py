import random, string
count, length = int(input()), int(input())
l = length
for i in range(count):
    set_of_chars_of_password = set()
    list_of_chars_of_password = []
    length_uppercase, length_lowercase, length_integers = [0 for i in range(3)]
    while length_integers == 0 or length_integers > l * 2 / 5:
        length = l
        length_uppercase = random.randint(length // 8, length - int(length * 2 /3))
        length -= length_uppercase
        length_lowercase = random.randint(length // 4, length // 2)
        length -= length_lowercase
        length_integers = length
    for i in range(length_uppercase):
        if i < len(list(set(string.ascii_uppercase) - {'O', 'I'})):
            q = random.choice(list(set(string.ascii_uppercase) - {'O', 'I'}))
            while q in set_of_chars_of_password:
                q = random.choice(list(set(string.ascii_uppercase) - {'O', 'I'}))
            set_of_chars_of_password.add(q)
        else:
            list_of_chars_of_password.append(random.choice(list(set(string.ascii_uppercase) - {'O', 'I'})))
    for i in range(length_lowercase):
        if i < len(list(set(string.ascii_lowercase) - {'o', 'l'})):
            q = random.choice(list(set(string.ascii_lowercase) - {'o', 'l'}))
            while q in set_of_chars_of_password:
                q = random.choice(list(set(string.ascii_lowercase) - {'o', 'l'}))
            set_of_chars_of_password.add(q)
        else:
            list_of_chars_of_password.append(random.choice(list(set(string.ascii_lowercase) - {'o', 'l'})))
    for i in range(length_integers):
        if i < 7:
            q = str(random.choice([2, 3, 4, 5, 6, 7, 8, 9]))
            while q in set_of_chars_of_password:
                q = str(random.choice([2, 3, 4, 5, 6, 7, 8, 9]))
            set_of_chars_of_password.add(q)
        else:
            list_of_chars_of_password.append(str(random.choice([2, 3, 4, 5, 6, 7, 8, 9])))
    list_of_chars_of_password += list(set_of_chars_of_password)
    random.shuffle(list_of_chars_of_password)
    string_of_chars_of_password = ''.join(list_of_chars_of_password)
    substrings_of_string = set()
    for i1 in range(3, len(string_of_chars_of_password) - 1):
        for j in range(len(string_of_chars_of_password) - 1):
            for q in range(j + i1, len(string_of_chars_of_password)):
                substrings_of_string.add(string_of_chars_of_password[j:q])
    substrings_of_string = list(substrings_of_string)
    flag = False
    english_dictionary = enchant.Dict("en_US")
    for i1 in substrings_of_string:
        if english_dictionary.check(i1):
            flag = english_dictionary.check(i1)
    if flag:
        i -= 1
    else:
        print(string_of_chars_of_password)
