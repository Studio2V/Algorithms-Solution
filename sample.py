import math
import num2words

'''
Common
'''


def findPrime(a):
    z = math.ceil(math.sqrt(a))
    if z == 2 and z == 3:
        return 1
    for s in range(z, 1, -1):
        if a % s == 0:
            return 0
    return 1


def dividetotalarray(number, divisor):
    lis = list()
    for x in number:
        lis.append(int(x / divisor) if (x % divisor == 0) else x)
    return lis[1::]


def multipleofnumber(number):
    x = 1
    for m in str(number):
        x *= int(m)
    return x


def numbertowordgen(number):
    x = num2words.num2words(number).replace("-", "").replace(" ", "")
    return len(x)


def collatzsequence(number):
    count = 0
    while number != 1:
        if number % 2:
            number = 3 * number + 1
        else:
            number /= 2
        count += 1
    return count


def numberofdivisors(number):
    count = 0
    for i in range(1, (int)(math.sqrt(number)) + 1):
        if (number % i == 0):
            if (number / i == i):
                count + 1
            else:
                count += 2
    return count


def sumdivisors(number):
    rangeN = math.ceil(math.sqrt(number))
    count = 0
    for x in range(1, rangeN + 1):
        if number % x == 0:
            count += (x + (number / x if x != 1 else 0))
    return int(count)


def amicableStatus(number):
    sumofnumber = sumdivisors(number)
    sumofnumber1 = sumdivisors(sumofnumber)
    print(number, sumofnumber1, sumofnumber)
    if number == sumofnumber1 and sumofnumber != sumofnumber1:
        return sumofnumber, sumofnumber1
    else:
        return 0


def wordtoasciicount(word):
    digitadd = 0
    for x in word:
        if str.isalpha(x):
            digitadd += ord(x) - (64 if str.isupper(x) else 96)
    return digitadd


'''
multiples of 3 and 5 below 1000
'''


def sol1():
    a = list(range(0, 1000, 3)).__add__(list(range(0, 1000, 5)))
    print(sum(list(set(a))))


'''
sum of even fibonacci sequence < 4000000
'''


def sol2():
    a = 1
    b = 2
    c = 2
    z = c
    while c <= 4000000:
        c = a + b
        z = z + (c if (c % 2) else 1)
        a = b
        b = c
        print(c, z)


'''find the largest factor'''


def sol3():
    a = 600851475143
    k = math.ceil(math.sqrt(a))
    for z in range(int(k), 0, -1):
        if a % z == 0:
            if findPrime(z):
                print(z)
                break


'''
largest palindrome product of three numbers
'''


def sol4():
    coll = list()
    for a in range(999, 100, -1):
        for b in range(999, 100, -1):
            z = str(a * b)
            if (z == z[::-1]):
                coll.append(int(z))
    coll.sort()
    print(coll[-1])


'''
to find the number divisible by 1-20 even numbers
'''


def sol5():
    a = list(range(2, 20, 2))
    f = list()
    for x in range(0, 5):
        a = list(dividetotalarray(a, a[0]))
        f.append(a[0])
        if a.__len__() <= 1:
            break
    print(f)


'''
sum of square and square of sum
'''


def sol6(a):
    f = a * ((a + 1) * (2 * a + 1)) / 6
    x = (a * (a + 1) / 2)
    x *= x
    print(x - f)


'''
find 10001st number
'''


def sol7():
    count = 2
    init = 0
    while 1:
        if findPrime(count):
            init += 1
            print(count)
        if init == 10002:
            print(count)
            break
        count += 1


'''largest number in adjacent digit '''


def sol8():
    a = ("73167176531330624919225119674426574742355349194934"
         "96983520312774506326239578318016984801869478851843"
         "85861560789112949495459501737958331952853208805511"
         "12540698747158523863050715693290963295227443043557"
         "66896648950445244523161731856403098711121722383113"
         "62229893423380308135336276614282806444486645238749"
         "30358907296290491560440772390713810515859307960866"
         "70172427121883998797908792274921901699720888093776"
         "65727333001053367881220235421809751254540594752243"
         "52584907711670556013604839586446706324415722155397"
         "53697817977846174064955149290862569321978468622482"
         "83972241375657056057490261407972968652414535100474"
         "82166370484403199890008895243450658541227588666881"
         "16427171479924442928230863465674813919123162824586"
         "17866458359124566529476545682848912883142607690042"
         "24219022671055626321111109370544217506941658960408"
         "07198403850962455444362981230987879927244284909188"
         "84580156166097919133875499200524063689912560717606"
         "05886116467109405077541002256983155200055935729725"
         "71636269561882670428252483600823257530420752963450")

    z = len(a)
    digit = 0
    prod = 0
    for f in range(0, z - 12, 1):
        number = a[f:f + 13]
        '''print(number)'''
        numb = multipleofnumber(number)
        if (numb > prod):
            prod = numb
            digit = number
            print(prod, digit)


'''int to words'''


def sol9(a):
    count = 0
    for x in range(1, a):
        count += numbertowordgen(x)
        print(count)


'''Longest Colletze sequence 524 837799'''


def sol10():
    count = 0
    digit = 0
    for x in range(1000000, 1000001):
        seq = collatzsequence(x)
        if (seq > count):
            count = seq
            digit = x
        print(x, seq)
    print(count, digit)


'''Pythogeron triples'''


def sol11(result):
    x = 0
    for i in range(1, int(result / 3) + 1):
        for j in range(i, int(result / 2) + 1):
            k = result - i - j
            if i * i + j * j == k * k and i + j + k == result:
                print(i, j, k, i * j * k)


'''highly divisible triangular number'''


def sol12(number):
    i = 1
    count = 0
    while 1:
        count += i
        i += 1
        result = numberofdivisors(count)
        if result > number:
            print(result, count, i)
            break


'''No of lattice function'''


def sol13(lattice):
    return print(math.factorial(2 * lattice) / math.pow(math.factorial(lattice), 2))


'''Finding Amicable number'''


def sol14(rangeN):
    amicablelist = list()
    for x in range(1, int(rangeN)):
        if amicablelist.__contains__(x):
            continue
        f = amicableStatus(x)
        if f != 0:
            amicablelist.append(f[0])
            amicablelist.append(f[1])
    print(" ".join(map(lambda x: str(x), amicablelist)))
    print(" ".join(map(lambda x: str(x), set(amicablelist))))
    print(sum(amicablelist))


'''Find Rank of names'''


def sol15():
    a = open("p022_names.txt", "r")
    nameslist = list(a.read().split(","))
    nameslist.sort()
    namesasciilist = map(lambda x, y: x * y, map(wordtoasciicount, nameslist), range(1, len(nameslist) + 1))
    print(sum(namesasciilist))


'''Distict Power '''


def sol16(rangea, rangeb):
    powerlist = list()
    for a in range(2, rangea + 1):
        for b in range(2, rangeb + 1):
            powerlist.append(int(math.pow(a, b)))
    print(len(set(powerlist)))


'''Spiral number generation'''


def sol17(rangeSpiral):
    rangeSpiral=rangeSpiral+1 if rangeSpiral%2==0 else rangeSpiral
    totalsum=0
    counter = 1
    skipper=0
    squareCounter = 1
    squaregen = 1
    while 1:
        print(counter)
        totalsum+=counter
        if counter == squareCounter:
            skipper+=2
            squaregen+=2
            squareCounter = int(math.pow(squaregen, 2))
        if counter >= math.pow(rangeSpiral, 2):
            break
        counter += skipper
    print(totalsum)


sol17(1001)
