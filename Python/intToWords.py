def numToString(x):
    if x < 0:
        return "negative " + numToString(abs(x))
    elif x == 0:
        return "zero"
    elif len(str(x)) > 105:
        return "Error: Domain out of range"
    return numToWordsBig(x).strip()

def intToString9(x):
    tempString = "one  two  threefour five six  seveneightnine ten  "
    return tempString[5 * (x - 1): 5 * x].strip()

def intToString99(x):
    if x == 0:
        return ""
    if x < 10:
        return intToString9(x)
    if x % 10 == 0:
        tempString = "ten    twenty thirty fourty fifty  sixty  seventyeighty ninety "
        return tempString[7 * (x / 10 - 1): 7 * (x / 10)].strip()
    if x < 16:
        tempString = "eleven  twelve  thirteenfourteenfifteen "
        return tempString[8 * (x % 10 - 1): 8 * (x % 10)].strip()
    if x < 20:
        string = "teen"
        if x % 10 == 8:
            string = "een"
        return intToString9(x % 10) + string
    return intToString99(x - x % 10) + "-" + intToString99(x % 10)

def intToString999(x):
    if x == 0:
        return ""
    if x < 100:
        return intToString99(x)
    return intToString9(x / 100) + " hundred " + intToString99(x % 100)

def numToWordsBig(x):
    return numToWordsHelper2(x, 0)

def getGroup(x):
    if x == 0:
        return ""
    tempString = "thousand    million     billion     trillion    quadrillion quintillion sextillion  octillion   nonillion   decillion   undecillion duodecilliontredecillion"
    if x < 14:
        return tempString[12 * (x - 1): 12 * x].strip()
    if x == 14:
        return "quattuoredecillion"
    if x < 24:
        tempString = "quindecillion    sexdecillion    septendecillionoctodecillion   novemdecillion  vigintillion    unvigintillion  duovigintillion trevigintillion "
        return tempString[16 * (x - 15): 16 * (x - 14)].strip()
    if x == 24:
        return "quattuorvigintillion"
    if x < 34:
        tempString = "quinvigintillion  sexvigintillion   septenvigintillionoctovigintillion  novemvigintillion trigintillion     untrigintillion   duotrigintillion  tretrigintillion  "
        return tempString[18 * (x - 25): 18 * (x - 24)].strip()

def numToWordsHelper(x, group):
    if x == 0:
        return ""
    return numToWordsHelper(x / 1000, group + 1) + intToString999(x % 1000) + " " + getGroup(group) + " "

def numToWordsHelper2(x, group):
    ans = ""
    while x > 0:
        ans = intToString999(x % 1000) + " " + getGroup(group) + " " + ans
        x = x / 1000
        group = group + 1
    return ans
