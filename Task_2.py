#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
N = int(input("Введите число N: "))
result = 1
for i in range(1, N+1):
    result = result * i
    print(result, end = ' ')