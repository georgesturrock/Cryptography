#  Exercise 1
#  initialize variables
p2e = ''
shift = 0
ct = ''
letter = ''
asciiCode = 0
letterRes = ''
ex = 0

#  Request input for phrase to encode and shift value
p2e = raw_input("Enter Phrase:")
shift = raw_input("Enter Shift Number:")
ex = raw_input("Enter Exercise Number (1 or 2):")

shift = int(shift)
ex = int(ex)

#  Exercise 1.2
if ex == 1:
    for letter in p2e:
        if letter.isalpha():
            if letter.islower():
                ct += 'x'
            else:
                ct += 'X'
        else:
            ct += letter
    print('Exercise 1.2')
    print(ct)

#  Exercise 1.3
#  encode phrase and wrap if necessary
if ex == 2:
    for letter in p2e:
        if letter.isalpha():
            asciiCode = ord(letter)
            asciiCode = asciiCode + shift
            if letter.islower():
                if asciiCode > 122:
                    asciiCode = asciiCode - 26
                    ct += chr(asciiCode)
                else:
                    ct += chr(asciiCode)
            else:
                if asciiCode > 90:
                    asciiCode = asciiCode - 26
                    ct += chr(asciiCode)
                else:
                    ct += chr(asciiCode)
        else:
            ct += letter
    print('Exercise 1.3')
    print(ct)


