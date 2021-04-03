
# Rabbits and Recurrence Relations

# fibonacci sequence : 1,2,3,5,8,13..

# ^problem - find fibonacci sequence till 10th term

#seq = [0,1,1]
# def fib(a : int , b : int, term) -> int:
#     global seq
#     result = a + b
#     #print(result)
#     seq.append(result)
#     if len(seq) <= term:
#         fib(b, result, term)

#     else:
#         return result
#fib(1,1,22)


def fib_pythonic(number):
    # taken from rebelcoder
    old, new = 1,1
    for _ in range(number - 1):
        new, old = old, old+new
    return new




def rabbits(months, offsprings):
    parent, child = 1,1
    for _ in range(months - 1):
        child, parent = parent, parent+(child*offsprings)
    return child


test = rabbits(29,3)

print(test)

