def rec_product(a, b, result = 0):
    if b == 0:
        return result;
    elif b>0:
        result += a
        b -= 1
        return rec_product(a,b,result)
    elif b<0:
        result -= a
        b += 1
        return rec_product(a,b,result)

rec_product(2,3)