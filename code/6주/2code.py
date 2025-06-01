word = "Hello"
print(word.upper())   # HELLO
print(word.lower())   # hello

msg = "  Hi there!  "
print(msg.strip())    # Hi there!

fruit = "banana"
print(fruit.replace("banana", "apple"))  # apple

data = "a,b,c"
print(data.split(","))  # ['a', 'b', 'c']

words = ['a', 'b', 'c']
print("-".join(words))  # a-b-c

filename = "report.pdf"
print(filename.startswith("rep"))  # True
print(filename.endswith(".pdf"))   # True

sentence = "hello world"
print(sentence.find("world"))  # 6

print("abc".isalpha())   # True
print("123".isdigit())   # True
print("abc123".isalpha())  # False

txt = "Python123"
print(txt.isalpha())  # False (문자 + 숫자니까)
print(txt.isdigit())  # False
print("1234".isdigit())  # True
print("hello".isalpha())  # True

