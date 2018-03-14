#  Exercise 2
#  initialize variables
p2e = ''
shift = 0
ct = ''
letter = ''
asciiCode = 0

#  Request input for phrase to encode and shift value
p2e = raw_input("Enter Phrase:")
shift = raw_input("Enter Shift Number:")

shift = int(shift)

#  encode phrase and wrap if necessary
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
print('Exercise 2')
print(ct)


