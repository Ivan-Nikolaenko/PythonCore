# a1, a2, a3 = map(int, input().split())
# lst=[a1,a2,a3]
# print(lst)
#
# str1 = map(str, input().split())
# print('Москва' in str1)
# Можно еще так :
# cities = input().split()
# print('Москва' in cities)
# или вообще в одну строку :
# print('Москва' in input().split())
#
# cities = input().split()
# print(cities[-1])

# marks = list(map(int, input().split()))
# average = sum(marks) / len(marks)
# print(average.__round__(1))

# name = str(input())
# autor = str(input())
# stranic = int(input())
# price = float(input())
# book=[name,autor,stranic,price*2]
# del book [2]
# book[1]='Пушкин'
# print(book)
# Как можно было :
# book = [input(), input(),int(input()), float(input())]
# del book[2]
# book[1] = 'Пушкин'
# book[2] *= 2
# print(book)

# chisla = list(map(int, input().split()))
# lst =sorted(sorted(chisla),reverse=True)
# print(*lst)
# lst = list(map(str, input().split()))
# cities = ["Москва", "Тверь", "Вологда"]
# print(*lst+cities)

# c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
# print(c[1::2])
# m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
# print(m[2:7])

# m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
# reversed_m = m[::-1]
# print(reversed_m[5:10])
# chisla = map(int, input().split())
# cities = ["Москва", "Казань", "Ярославль"]
# cities.insert(1,"Ульяновск")
# print(*cities)
# lst = list(input())
# lst.remove("+")
# lst.remove("7")
# lst.insert(0,'8')
# lst.remove("-")
# lst.remove("-")
# print("".join(lst))
lst = list(map(str, input().split()))
lst.sort()
lst.pop(0)
print(lst)
