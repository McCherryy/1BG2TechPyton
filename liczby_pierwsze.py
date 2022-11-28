# sprawdzenie czy liczba jest pierwsza 
# n = int(input())
# for i in range(2, n):
#     if n % i ==0:
#         print("liczba jest puierwsza")
#         exit(0)
# print("liczba nie jest pierwsza")

# generowanie liczb pierwszych w przedziale p, q

# p = int(input())
# q = int(input())

# for j in range(p, q+1):
#     flaga = True
#     for i in range(2, j):
#         if j % i == 0:
#             flaga = False
#             break
#     if flaga == True:
#         print(i, end=" ")

# generowanie liczb pierwszych (pierwsze n liczb pierwszych)

# n = int(input("podaj ile chcesz liczb pierwszych"))

# k = 2
# ilosc = 0
# while 1:
#     flaga = True
#     for i in range(2, k):
#         if k % i == 0:
#             flaga = False
#             break
#     if flaga == True:
#         print(k, end=" ")
#         ilosc = ilosc + 1
#     if ilosc == n:
#         break
#     k = k + 1
