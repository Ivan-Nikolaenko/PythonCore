# x = int(input())
# if x >= 0 and x <= 9:
#    print('значение взодит от 0 до 9 включительно')
# else:
#     print("Net")

# x = int(input())
# if x==1:
#     print('1. Введение в Python')
# elif x==2:
#     print('2. Строки и списки')
# elif x == 3:
#     print('3. Условные операторы')
# elif x == 4:
#     print ('4. Циклы')
# elif x == 5:
#     print('5. Словари, кортежи и множества')
# elif x == 6:
#     print('6. Выход')

# a, b, c = list(map(int, input().split()))
# if a <= b and a <= c:
#     print(a)
# elif b <= a and b <= c:
#     print(b)
# else:
#     print(c)
# x = float(input())
# if x <= 60:
#     print('1')
# elif 60 < x <= 64:
#     print('2')
# elif 64 < x <= 69:
#     print('3')
# else:
#     print('4')
# x = float(input())
# if x ==1:
#     print('понедельник')
# elif x==2:
#     print('вторник')
# elif x==3:
#     print('среда')
# elif x==4:
#     print('четверг')
# elif x==5:
#     print('пятница')
# elif x==6:
#     print('суббота')
# else:
#     print('воскресенье')

x = float(input())
if x in [1, 3, 5, 7, 8, 10, 12]:
    print('31')
elif x in [4, 6, 9, 11]:
    print('30')
elif x in [2]:
    print('28')
# 1, 3, 5, 7, 8, 10, 12 месяцы - 31 день
# 4, 6, 9, 11 - 30
# 2 - 28
