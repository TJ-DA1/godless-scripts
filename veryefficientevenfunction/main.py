with open("even.py", "w") as r:
    r.write(f"def iseven(x):\n\tmatch x:\n")
    for i in range(10000000):
        if i % 2 == 0:
            r.write(f"\t\tcase {i}:\n\t\t\treturn True\n")
        else:
            r.write(f"\t\tcase {i}:\n\t\t\treturn False\n")
