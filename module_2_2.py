first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
thirt = int(input('Введите третье число: '))

if first == second and first ==thirt:
    print(3)

elif first == thirt != second or first == second != thirt or second == thirt != first:
    print(2)

elif first != thirt != second:
    print(0)
