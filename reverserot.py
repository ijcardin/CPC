
characterList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','.']

while True:
    encryptedMessage = ''
    userInput = input()
    if userInput == '0':
        break

    rotation, string = userInput.split()

    # reversal
    reversedstring = ''.join(reversed(string))


    # rotation
    for char in reversedstring:
        newIndex = (characterList.index(char) + int(rotation)) % 28
        encryptedMessage += characterList[newIndex]

    print(encryptedMessage)


