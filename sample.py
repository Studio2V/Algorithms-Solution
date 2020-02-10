import math
import num2words
import time

# region Helpers
''' Common Helper Reusable Methods'''

'''checks whether prime or not 0 => true , 1=> false'''


def findPrime(a):
    if a == 1:
        return 0
    if a == 2 and a == 3:
        return 1
    z = math.ceil(math.sqrt(a))
    for s in range(z, 1, -1):
        if a % s == 0:
            return 0
    return 1


'''Divide total array with given number and return list'''


def dividetotalarray(number, divisor):
    lis = list()
    for x in number:
        lis.append(int(x / divisor) if (x % divisor == 0) else x)
    return lis[1::]


'''Returns multiples of a number'''


def multipleofnumber(number):
    x = 1
    for m in str(number):
        x *= int(m)
    return x


'''Returns numbers  inwords without - and spaces '''


def numbertowordgen(number):
    x = num2words.num2words(number).replace("-", "").replace(" ", "")
    return len(x)


'''Returns the collatz sequence of a number'''


def collatzsequence(number):
    count = 0
    while number != 1:
        if number % 2:
            number = 3 * number + 1
        else:
            number /= 2
        count += 1
    return count


'''Returns the number of divisors of a given number'''


def numberofdivisors(number):
    count = 0
    for i in range(1, (int)(math.sqrt(number)) + 1):
        if (number % i == 0):
            if (number / i == i):
                count + 1
            else:
                count += 2
    return count


'''Returns the sum of divisors of a given number'''


def sumdivisors(number):
    rangeN = math.ceil(math.sqrt(number))
    count = 0
    for x in range(1, rangeN + 1):
        if number % x == 0:
            count += (x + (number / x if x != 1 else 0))
    return int(count)


'''Checks whether a number is amicable or not 0=> False and number and amicalbe number => True'''


def amicableStatus(number):
    sumofnumber = sumdivisors(number)
    sumofnumber1 = sumdivisors(sumofnumber)
    print(number, sumofnumber1, sumofnumber)
    if number == sumofnumber1 and sumofnumber != sumofnumber1:
        return sumofnumber, sumofnumber1
    else:
        return 0


'''Returns the sum of ascii of word *accept only alpha, *starts from 1-26 '''


def wordtoasciicount(word):
    digitadd = 0
    for x in word:
        if str.isalpha(x):
            digitadd += ord(x) - (64 if str.isupper(x) else 96)
    return digitadd


# endregion

# region Solution
'''multiples of 3 and 5 below 1000 problem 01'''


def sol01():
    a = list(range(0, 1000, 3)).__add__(list(range(0, 1000, 5)))
    print(sum(list(set(a))))


'''sum of even fibonacci sequence < 4000000 problem 02'''


def sol02():
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


'''find the largest factor problem 03'''


def sol03():
    a = 600851475143
    k = math.ceil(math.sqrt(a))
    for z in range(int(k), 0, -1):
        if a % z == 0:
            if findPrime(z):
                print(z)
                break


'''largest palindrome product of three numbers problem 04'''


def sol04():
    coll = list()
    for a in range(999, 100, -1):
        for b in range(999, 100, -1):
            z = str(a * b)
            if z == z[::-1]:
                coll.append(int(z))
    coll.sort()
    print(coll[-1])


'''to find the number divisible by 1-20 even numbers problem05'''


def sol05():
    a = list(range(2, 20, 2))
    f = list()
    for x in range(0, 5):
        a = list(dividetotalarray(a, a[0]))
        f.append(a[0])
        if a.__len__() <= 1:
            break
    print(f)


'''sum of square and square of difference problem 06'''


def sol06(a):
    f = a * ((a + 1) * (2 * a + 1)) / 6
    x = (a * (a + 1) / 2)
    x *= x
    print(x - f)


'''find 10001st prime problem 07'''


def sol07():
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


'''Pythogeron triples problem 09'''


def sol09(result):
    x = 0
    for i in range(1, int(result / 3) + 1):
        for j in range(i, int(result / 2) + 1):
            k = result - i - j
            if i * i + j * j == k * k and i + j + k == result:
                print(i, j, k, i * j * k)


'''highly divisible triangular number problem 12'''


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


'''largest number in adjacent digit  problem13'''


def sol13():
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


'''Longest Collatz sequence 524 837799  problem 14'''


def sol14():
    count = 0
    digit = 0
    for x in range(1000000, 1000001):
        seq = collatzsequence(x)
        if (seq > count):
            count = seq
            digit = x
        print(x, seq)
    print(count, digit)


'''No of lattice function problem 15'''


def sol15(lattice):
    return print(math.factorial(2 * lattice) / math.pow(math.factorial(lattice), 2))


'''int to words problem 17'''


def sol17(a):
    count = 0
    for x in range(1, a):
        count += numbertowordgen(x)
        print(count)


'''Finding Amicable number solution 21'''


def sol21(rangeN):
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


'''Find Rank of names problem 22'''


def sol22():
    a = open("p022_names.txt", "r")
    nameslist = list(a.read().split(","))
    nameslist.sort()
    namesasciilist = map(lambda x, y: x * y, map(wordtoasciicount, nameslist), range(1, len(nameslist) + 1))
    print(sum(namesasciilist))


'''Spiral number generation problem28'''


def sol28(rangeSpiral):
    rangeSpiral = rangeSpiral + 1 if rangeSpiral % 2 == 0 else rangeSpiral
    totalsum = 0
    counter = 1
    skipper = 0
    squareCounter = 1
    squaregen = 1
    while 1:
        print(counter)
        totalsum += counter
        if counter == squareCounter:
            skipper += 2
            squaregen += 2
            squareCounter = int(math.pow(squaregen, 2))
        if counter >= math.pow(rangeSpiral, 2):
            break
        counter += skipper
    print(totalsum)


'''Distinct Power problem29 '''


def sol29(rangea, rangeb):
    powerlist = list()
    for a in range(2, rangea + 1):
        for b in range(2, rangeb + 1):
            powerlist.append(int(math.pow(a, b)))
    print(len(set(powerlist)))


'''Consecutive prime  problem 50'''


def sol50():
    print(time.time())
    counter = 2
    loopcalculator = 0
    a = list([2, 3])
    while 1:
        status = 1
        checkupto = math.ceil(math.sqrt(counter))
        for x in a:
            loopcalculator += 1
            if x > checkupto:
                break
            if counter in a or counter % x == 0:
                status = 0
                break

        if status == 1:
            a.append(counter)
        counter += 1
        if sum(a) > 1000000:
            print(" ".join(map(lambda x: str(x), a)))
            print(loopcalculator)
            print(sum(a) - a[-1])
            break
    print(time.time())

# endregion
