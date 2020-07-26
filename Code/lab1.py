# Lab1

def convert (x, base):
    if not isinstance(x, int):
        return -1
    if not isinstance(base, int):
        return -2
    if x < 0:
        return -3
    if base < 2:
        return -4
    
    coef = []
    while x != 0:
        coef.insert(0, x % base)
        x = x // base
    return coef if len(coef) > 0 else [0]

def hexstring(x):
    if not isinstance(x, int):
        return -1
    if x < 0:
        return -2
    
    hex_string = "0x"
    chars = { 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F' }
    coef = convert(x, 16)
    for num in coef:
        if num < 10:
            hex_string += str(num)
        else:
            hex_string += chars[num]    
    
    return hex_string

def decodedate(data):
    """ Keep data unchanged """
    month = (data & 0xF0000000) >> 28 # 4-bits month
    month += 1
    day = (data & 0x0F800000) >> 23 # 5-bits day
    day += 1  
    year = (data & 0x007FFFFF) >> 0 # 23-bits day
    result = (str(day), str(month), str(year))
    return '.'.join(result)
def encodedate (day, month, year):
    if 1 > day or day > 31:
        return -1
    if 1 > month or month > 12:
        return -1
    if 0 > year or year > 2**23-1:
        return -1    
    
    result = 0
    result = (result & 0xF07FFFFF) | ((day-1) << 23)
    result = (result & 0x0FFFFFFF) | ((month-1) << 28)
    result = (result & 0xFFFFFFFF) | (year << 0)
    
    #return ((day-1) << 23) | ((month-1) << 28) | (year << 0)
    return result

def test():
    print(convert(1234, 10))
    print(convert(1234, 16))
    print(convert(0b10110001 >> 3,2))
    print(hexstring(1234))
    print(decodedate(1107298273))
    print(encodedate(5,5,2017))
test()