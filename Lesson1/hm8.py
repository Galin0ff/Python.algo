'''8. Определить, является ли год, который ввел пользователем, високосным или
невисокосным.
-- год, номер которого кратен 400, — високосный;
-- остальные годы, номер которых кратен 100, — невисокосные;
-- остальные годы, номер которых кратен 4, — високосные.'''

year = int(input('Введите год: '))

if year % 400 == 0:
    print(f"Год {year} високосный")
elif year % 100 == 0 and year % 400 != 0:
    print(f"Год {year} невисокосный")
elif year % 4 == 0:
    print(f"Год {year} високосный")
else:
    print(f"Год {year} невисокосный")