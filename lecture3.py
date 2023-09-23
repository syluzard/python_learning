print("Input your string: ", end="")
s = input()
print("Is it a palindrome? ", end="")
print( s.replace('.', '').replace(',', '').replace('?', '').replace('!', '').replace(' ', '').replace('\'', '').lower() == s[::-1].replace('.', '').replace(',', '').replace('?', '').replace('!', '').replace(' ', '').replace('\'', '').lower() )
