n=int(input())

k=5

number_of_zeros=0

while n>=5:

    n//=5
    number_of_zeros+=n

print(number_of_zeros)