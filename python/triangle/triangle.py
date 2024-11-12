def equilateral(sides):
    a, b, c = sorted(sides)
    if equal(a,b,c) and a == b == c:
        return True
    else:
        return False


def isosceles(sides):
    a, b, c = sorted(sides)
    if equal(a,b,c) and a == b or a == c or b == c:
        return True
    else:
        return False


def scalene(sides):
    a, b, c = sorted(sides)
    if equal(a,b,c) and a != b != c:
        return True
    else:
        return False


def equal(a,b,c):
    if 0 in (a,b,c) or c >= a + b:
        return False
    else:
        return True
