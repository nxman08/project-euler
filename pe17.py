def nn(a):  
    o = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    te = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    t = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if a == 1000:
        return len("onethousand")

    s = ""

    if a >= 100:
        s += o[a // 100] + "hundred"
        a %= 100
        if a > 0:
            s += "and"

    if a == 10 or (10 < a < 20):  
        s += te[a - 10]
        return len(s)  

    if a >= 20:
        s += t[a // 10]
        a %= 10

    if a > 0:
        s += o[a]

    return len(s)

s = sum(nn(i) for i in range(1, 1000)) + nn(1000)

print(s)  
