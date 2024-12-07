def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

print("Caesar Cipher Program")
while True:
    choice = input("\n1: Encrypt\n2: Decrypt\n3: Exit\nChoose an option: ")
    if choice == '3': break
    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: ")) * (1 if choice == '1' else -1)
    print("Result:", caesar_cipher(text, shift))
