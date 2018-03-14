#  Exercise 2
#  initialize variables
p2d = ''
shift = 0
ct = ''
letter = ''
asciiCode = 0

#  Request input for phrase to encode and shift value
p2d = raw_input("Enter Phrase:")

shift = range(26)

#  decode phrase from wall
for r in shift:
    ct = ''
    for letter in p2d:
        if letter.isalpha():
            asciiCode = ord(letter)
            asciiCode = asciiCode - r
            if letter.islower():
                if asciiCode < 97:
                    asciiCode = asciiCode + 26
                    ct += chr(asciiCode)
                else:
                    ct += chr(asciiCode)
            else:
                if asciiCode < 65:
                    asciiCode = asciiCode + 26
                    ct += chr(asciiCode)
                else:
                    ct += chr(asciiCode)
        else:
            ct += letter
    print(r)
    print(ct)

