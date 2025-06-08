import re

text = input()
result = re.sub(r'(\d+)년', r'\1', text)
print(result)
