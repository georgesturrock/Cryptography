import crypt

#define function to find the encrypted password.
def findpass(cryptpass, dictname):
    salt = cryptpass[0:2]
    dictfile = open(dictname, 'r')
    for word in dictfile.readlines():
        word = word.strip('\n')
        cryptword = crypt.crypt(word, salt)
        if (cryptword == cryptpass):
            print 'Password = '+word+'\n'
            return

    print 'Password Not Found'
    return

#Main function to iterate through encrypted passwords and pass values to 'findpass' to attempt to crack the password
def main():
    passwordfile = open('HW3passwords_2_2.txt', 'r')
    for line in passwordfile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            cryptpass = line.split(':')[1].strip(' ')
            print('Finding password for:', user, cryptpass)
            findpass(cryptpass, 'HW3dictionary_2_2.txt')

if __name__ == '__main__':
    main()
