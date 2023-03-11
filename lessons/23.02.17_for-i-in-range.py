# lst  = map(int, ['10', '2', '3'])
# print(sum(lst))


def s_map(f, lst):
    res = []
    for x in lst:
        res.append(f(x))
    return res

def r_map(f, lst):
    for x in lst:
        yield f(x)

def r_range(n, b=None, c = 1):
    i = 0
    if b is None:
        while i <= n:
            yield i
            i += c
    else:
        i += n
        while i <= b:
            yield i
            i += c


for r in r_range(5, 10, 2):
    print(r)


