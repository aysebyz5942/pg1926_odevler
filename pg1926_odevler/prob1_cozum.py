
a = 0

while a < 99 :
    a += 1
    if a % 3 == 0:
        print("fiiz", end=" ")
        if a%5==0:
            print("fizzbuzz", end=" ")
    elif a%5==0:
        print("buzz", end=" ")
        if a%3==0:
            print("fizzbuzzz", end=" ")
    else :
        print(a, end=" ")