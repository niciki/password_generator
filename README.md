# Simple password generator(generator.py)
A simple generator of a given number of passwords of a certain length, necessarily including at least one lowercase, one uppercase letter and one digit, but about no more than a 1/3 - 2/5 of total amount of characters of password, without ambiguous characters ('0', 'O', '1', etc.), which will complicate the selection of a password with a simple brute force. The distribution of the number of letters and numbers is carried out in an arbitrary way using the random library. In this case, the program uses all the characters from the given number series as long as there is such a possibility, and then the distribution of characters occurs in an arbitrary way.
# Password generator(generator_with_check.py)
A more advanced version of the generator, which, in addition to all the functions of the previous one, also prohibits the accidental possibility of guessing part of the password using a dictionary (it is prohibited to use existing English words or their combinations in the password). Before starting the program, you must first load the library used to check substrings for compliance with any word in the English language with command:
`pip install pyenchant`
