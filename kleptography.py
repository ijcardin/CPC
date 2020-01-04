
characterList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

n, m = map(int, input().split())
end = input()
cipherText = input()


plaintext = list(' '*(m-n) + end)
for i in range(m - 1, n - 1, -1):
    plaintext[i - n] = chr(ord('a') + (26 + ord(cipherText[i]) - ord(plaintext[i])) % 26)

print(''.join(plaintext))