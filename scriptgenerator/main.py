from random import choice, randint, randrange
open('text.py', 'w').close()
text = open("text.py", "a")
name1 = ["", "number_", "string_", "expression_", "boolean_", "object_"]
name2 = ["generator", "calculator", "compare", "parser", "deleter", "handler"]
name3 = ["", "_new", "_deprecated", "_two", "_func", "_old", "_better", "_function"]
variables = ["x", "y", "num", "string", "data", "result", "numlist", "text"]
comparatives = ["and", "or", "is", "is not", "==", "!=", "in"]
numcomparitives = ["==", "!=", ">=", "<=", ">", ">"]
iters = ["i", "j", "k", "m", "n", "r"]



indentnum = 0
max = 100
maxselec = 5
maxindent = 15

out = []

out.append(f'''numlist = {randint(0,10)}
string = {randint(0,10)}
text = {randint(0,10)}
result = {randint(0,10)}
data = {randint(0,10)}
num = {randint(0,10)}
x = {randint(0,10)}
y = {randint(0,10)}
''')

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

def genlist():
    list_ = []
    result = "["
    for i in range(randint(1, 7)):
        list_.append(choice(bools))
    for i in list_:
        result += str(i) + ", "
    return result[:-2] + "]"


class Num:
    def __str__(self):
        return gennum()


class Expression:
    def __str__(self):
        ret = ("(" + str(genexp(randrange(3, 11, 2))) + ")")
        return ret

num = Num()
exp = Expression()

bools = ["True", "False", "(not True)", "(not False)", "1", "0", "(not 1)", "(not 0)", num, exp, exp]
boolnonum = ["True", "False", "(not True)", "(not False)", "(not 1)", "(not 0)", num, exp, exp]

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
defined = []

def gendef():
    global indentnum
    valid = list(variables)
    parameters = ""
    globallist = []
    validvar = []
    for i in range(randint(1,4)):
        param = choice(valid)
        valid.remove(param)
        validvar.append(param)
    paramnum = len(validvar)
    for i in validvar:
        parameters += i + ", "

    name = ("\t" * indentnum) + "def " + (ref := choice(name1) + choice(name2) + choice(name3)) + "(" + parameters[:-2] + "):" + "\n"
    tempcount = 0
    while ref in (defined[i][0] for i in range(len(defined))):
        name = ("\t" * indentnum) + "def " + (ref := choice(name1) + choice(name2) + choice(name3)) + "(" + parameters[:-2] + "):" + "\n"
        tempcount += 1
        if tempcount > len(defined):
            for i in range(len(defined) - 1):
                if defined[i][0] == ref:
                    numparam = defined[i][1]
                    valid = list(variables)
                    parameters = ""
                    globallist = []
                    validvar = []
                    for j in range(numparam):
                        param = choice(valid)
                        valid.remove(param)
                        validvar.append(param)
                    paramnum = len(validvar)
                    for k in validvar:
                        parameters += k + ", "
                    defined.pop(i)
    out.append(name)

    indentnum += 1
    genline(2, True, validvar)
    indentnum -= 1

    defined.append([ref, paramnum])

def geniter(validvar = variables):
    global maxselec
    global indentnum
    iterer = choice(iters)
    forname = (("\t" * indentnum) + f"for {iterer} in range(int(" + str(choice([choice(validvar), randint(1,20)])) + ")):\n")
    out.append(forname)
    indentnum += 1
    genline(maxselec, True, validvar + [iterer])
    indentnum -= 1

def genselec(validvar = variables):
    global maxselec
    global indentnum
    ifname = ("\t" * indentnum) + "if " + genexp(3) + ":" + "\n"
    out.append(ifname)
    indentnum += 1
    genline(maxselec, True, validvar)
    indentnum -= 1
    for i in range(randint(0,1)):
        elsename = ("\t" * indentnum) + "elif " + genexp(3)+ ":" + "\n"
        out.append(elsename)
        indentnum += 1
        genline(maxselec, True, validvar)
        indentnum -= 1
    elsename = ("\t" * indentnum) + "else" + ":" + "\n"
    out.append(elsename)
    indentnum += 1
    genline(maxselec, True, validvar)
    indentnum -= 1

def genline(max, selec, validvar):
    global maxindent
    for i in range(randint(1,max)):
        ltype = randint(1,7)
        match ltype:
            case 1:
                var = choice(validvar)
                line = ("\t" * indentnum) + var + choice([" *= ", " += ", " /= ", " //= ", " %= ", " -= "]) + str(randint(1, 20)) + "\n"
            case 2:
                if len(defined) > 0:
                    func = choice(defined)
                    params = ""
                    for i in range(func[1]):
                        params += choice(validvar) + ", "
                    line = ("\t" * indentnum) + func[0] + "(" + params[:-2] + ")" + "\n"
                else:
                    line = ("\t" * indentnum) + "pass" + "\n"
            case 3:
                if indentnum < maxindent:
                    genselec(validvar)
                    line = ""
                else:
                    line = ("\t" * indentnum) + "pass\n"
            case 4:
                if not selec:
                    gendef()
                    line = ""
                else:
                    var = choice(validvar)
                    line = ("\t" * indentnum) + var + choice([" *= ", " += ", " /= ", " //= ", " %= ", " -= "]) + str(randint(1, 20)) + "\n"

            case 5:
                line = ("\t" * indentnum) + "print(" + choice(validvar) + ")\n"
            case 6:
                line = ("\t" * indentnum) + choice(validvar) + "=" + str(randint(1, 50)) + "\n"
            case 7:
                geniter(validvar)
                line = ""
        out.append(line)


genline(max, False, variables)

print(out)
for i in out:
    text.write(i)