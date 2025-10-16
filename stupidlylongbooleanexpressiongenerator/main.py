from random import choice, randint, randrange

def genlist():
    list_ = []
    result = "["
    for i in range(randint(1, 7)):
        list_.append(choice(bools))
    for i in list_:
        result += str(i) + ", "
    return result[:-2] + "]"


def gennum():
    list_ = []
    result = "("
    for i in range(randint(1, 7)):
        list_.append(choice([str(randint(1, 500)),
        str(randint(1, 500)) + choice([" * ", " + ", " / ", " // ", " % ", " - ", " ** "]) + str(randint(1, 500))]))
        list_.append(choice(numcomparitives))
    list_.append(str(randint(1, 500)))
    for i in list_:
        result += i + " "
    return result[:-1] + ")"

def genexp(size):
    out = []
    numberguard = False
    incheck = False
    formatout = ""
    for i in range(size):
        if i % 2 == 1:
            compchoice = (choice(comparatives))
            if compchoice == "is" or compchoice == "is not":
                numberguard = True
                try:
                    if out[-2] != "in":
                        out[-1] = choice(boolnonum)
                except:
                    out[-1] = choice(boolnonum)
            elif compchoice == "in":
                incheck = True
            out.append(compchoice)
        else:
            if numberguard:
                boolchoice = choice(boolnonum)
                numberguard = False
            elif incheck:
                boolchoice = genlist()
                incheck = False
            else:
                boolchoice = choice(bools)
            out.append(boolchoice)
    for i in out:
        formatout += " " + str(i)
    return formatout[1:]

def genexp2(size):
    out2 = []
    numberguard2 = False
    incheck2 = False
    formatout2 = ""
    for i in range(size):
        if i % 2 == 1:
            compchoice2 = (choice(comparatives))
            if compchoice2 == "is" or compchoice2 == "is not":
                numberguard2 = True
                try:
                    if out2[-2] != "in":
                        out2[-1] = choice(boolnonum)
                except:
                    out2[-1] = choice(boolnonum)
            elif compchoice2 == "in":
                incheck2 = True
            out2.append(compchoice2)
        else:
            if numberguard2:
                boolchoice2 = choice(boolnonum)
                numberguard2 = False
            elif incheck2:
                boolchoice2 = genlist()
                incheck2 = False
            else:
                boolchoice2 = choice(bools)
            out2.append(boolchoice2)
    for i in out2:
        formatout2 += " " + str(i)
    return formatout2[1:]

class Num:
    def __str__(self):
        return gennum()


class FurtherExpression:
    def __str__(self):
        ret = ("(" + str(genexp2(randrange(3, 11, 2))) + ")")
        return ret

num = Num()
exp = FurtherExpression()
comparatives = ["and", "or", "is", "is not", "==", "!=", "in"]
numcomparitives = ["==", "!=", ">=", "<=", ">", ">"]
bools = ["True", "False", "(not True)", "(not False)", "1", "0", "(not 1)", "(not 0)", num, exp, exp]
boolnonum = ["True", "False", "(not True)", "(not False)", "(not 1)", "(not 0)", num, exp, exp]
result = False
with open("expression.py", "w") as w:
  w.write("boolean = " +  "(" + genexp(1001) + ") " + choice(["or", "and"]) + choice([" True"," False"]))