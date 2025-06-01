def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# 사용자 입력
mode = input("모드 선택 (e: 암호화 / d: 복호화): ")
message = input("문장을 입력하세요: ")
shift = int(input("얼마나 밀까요? (예: 3): "))

if mode == 'e':
    encrypted = encrypt(message, shift)
    print("암호화된 결과:", encrypted)
elif mode == 'd':
    decrypted = decrypt(message, shift)
    print("복호화된 결과:", decrypted)
else:
    print("잘못된 모드입니다.")
