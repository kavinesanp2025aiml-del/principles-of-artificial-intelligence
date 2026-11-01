from itertools import permutations

# Crypt-Arithmetic: SEND + MORE = MONEY

letters = 'SENDMORY'

digits = range(10)

for p in permutations(digits, len(letters)):

    d = dict(zip(letters, p))

    # First letters cannot be zero
    if d['S'] == 0 or d['M'] == 0:
        continue

    SEND = (d['S']*1000 + d['E']*100 +
            d['N']*10 + d['D'])

    MORE = (d['M']*1000 + d['O']*100 +
            d['R']*10 + d['E'])

    MONEY = (d['M']*10000 + d['O']*1000 +
             d['N']*100 + d['E']*10 + d['Y'])

    if SEND + MORE == MONEY:

        print("Solution Found!")
        print("SEND =", SEND)
        print("MORE =", MORE)
        print("MONEY =", MONEY)

        print("\nLetter Assignments:")
        for letter in letters:
            print(letter, "=", d[letter])

        break
