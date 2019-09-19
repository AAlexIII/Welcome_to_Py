s = "У лукоморья 123 дуб зеленый 456"

print(s.rindex('я'))  # 1)
print(s.count("у"))  # 2)
print(s.upper() if not s.isalpha() else '')  # 3 номер
print(s.lower() if len(s) > 4 else '')  # 4)
s = "О" + s[1:]
print(s)  # 5)
