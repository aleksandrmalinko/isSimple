import math
import random
import time

x1 = 19540818305052663929
x2 = 4182626256901165713180947335409849194453
x3 = 565674746577950549441720540453387249813
x4 = 40319329928699692919180302866991670347533839708463260094733186934134923674660447
kar1 = 32809426840359564991177172754241
kar2 = 2810864562635368426005268142616001


def jacobi(a, num):
    if a == 0:
        return 0
    if a == 1:
        return 1
    if math.gcd(a, num) != 1:
        return 0
    else:
        if (a % 2) == 0:
            return jacobi(a//2, num)*(pow(-1, (num*num-1)//8))
        else:
            return jacobi(num % a, a)*(pow(-1, ((a-1)*(num-1))//4))


def is_simple1(num, repeat):
    base_count = 0
    rnd2 = 0
    for i in range(repeat):
        rnd = random.randint(2, num - 2)
        rnd2 = rnd
        if math.gcd(rnd, num) != 1:
            #print("Not simple, gcd!=1 ", "Base: ", rnd)
            return False

        if pow(rnd, (num - 1), num) != 1:
            #print("Not simple, pow!=1", "Base: ", rnd)
            return False
        if base_count < 5:
            #print("Probably simple with base: ", rnd)
            base_count += 1

    #print("Probably simple with error probability: ", pow((1 / 2), repeat), "Base: ", rnd2)
    return True


def is_simple2(num, repeat):
    base_count = 0
    rnd = 0
    for i in range(repeat):
        rnd = random.randint(2, num - 2)
        if math.gcd(num, rnd) != 1:
            #print("Not a simple, gcd!=1", "Base: ", rnd)
            return False
        x = pow(rnd, (num-1) // 2, num)
        y = jacobi(rnd, num)
        if y == -1:
            y = num - 1
        if x != y:
            #print("Not a simple, a^(num-1)/2!=jacoby(a/num) (mod num)", "Base: ", rnd)
            return False
        if base_count < 5:
            #print("Probably simple with base: ", rnd)
            base_count += 1

    #print("Probably simple with error probability: ", pow((1 / 2), repeat), "Base: ", rnd)
    return True


def is_simple3(num, repeat):
    base_count = 0
    if num == 0 or num == 1 or num == 4 or num == 6 or num == 8 or num == 9:
        return False

    if num == 2 or num == 3 or num == 5 or num == 7:
        return True
    s = 0
    d = num - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2 ** s * d == num - 1)

    def trial_composite(a):
        if pow(a, d, num) == 1 or pow(a, d, num) == num - 1:
            return False
        for j in range(s):
            if pow(a, 2 ** j * d, num) == num - 1:
                return False
        #print("Not simple, no condition is met", "Base: ", a)
        return True
    rnd = 0
    for i in range(repeat):
        #rnd = random.randrange(2, num-2)
        rnd = 24
        if trial_composite(rnd):
            return False  # непростое
        if base_count < 5:
            #print("Probably simple with base: ", rnd)
            base_count += 1
    #print("Is simple with error probability: ", pow(1/4, repeat), "Base: ", rnd)
    return True  # вероятно простое


# start_time = time.perf_counter()
# for i in range(1000):
#     if is_simple1(kar2, 1):
#         print("error", i)
# print("working time =", time.perf_counter() - start_time, "\n")
#for i in range(100):
if is_simple3(25, 1):
    print("error")