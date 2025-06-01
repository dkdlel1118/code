def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha() and char.isascii():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        elif '가' <= char <= '힣':
            base = ord('가')
            num_hangul = 11172
            result += chr((ord(char) - base + shift) % num_hangul + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

mode = input("모드 선택 (e: 암호화 / d: 복호화): ")
shift = int(input("밀어낼 숫자를 입력하세요: "))

if mode == 'e':
    message = input("암호화할 문장을 입력하세요: ")
    encrypted = encrypt(message, shift)
    print("암호화된 결과:", encrypted)

    # 결과를 파일로 저장
    file = open("encrypted.txt", "w", encoding="utf-8")
    file.write(encrypted)
    file.close()
    print("encrypted.txt 파일에 저장되었습니다.")

elif mode == 'd':
    # 파일에서 암호문 읽기
    file = open("encrypted.txt", "r", encoding="utf-8")
    encrypted = file.read()
    file.close()

    decrypted = decrypt(encrypted, shift)
    print("파일에서 읽은 암호문:", encrypted)
    print("복호화된 결과:", decrypted)
else:
    print("잘못된 모드입니다.")


