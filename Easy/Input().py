a, b = map(int, input().split())
c = str(input())
d = c.split("+")

sum = 0
dif = 0

for i in d:
    if "-" in i:
        dif_split = i.split("-")
        for j, part in enumerate(dif_split):
            if part.strip() == "":
                continue
            if "**" in part:
                af = part.split("**")
                if "*" in af[0]:
                    coef, var = af[0].split("*")
                    temp1 = int(coef.strip()) * (a ** int(af[1].strip()))
                elif "x" in af[0]:
                    temp1 = a ** int(af[1].strip())
                else:
                    temp1 = int(af[0].strip()) ** int(af[1].strip())
                if j == 0:
                    dif += temp1
                else:
                    dif -= temp1
            elif "x" in part:
                if j == 0:
                    dif += a
                else:
                    dif -= a
            else:
                if j == 0:
                    dif += int(part.strip())
                else:
                    dif -= int(part.strip())
    else:
        if "**" in i:
            af = i.split("**")
            if "*" in af[0]:
                coef, var = af[0].split("*")
                temp1 = int(coef.strip()) * (a ** int(af[1].strip()))
            elif "x" in af[0]:
                temp1 = a ** int(af[1].strip())
            else:
                temp1 = int(af[0].strip()) ** int(af[1].strip())
            sum += temp1
        elif "x" in i:
            sum += a
        else:
            sum += int(i.strip())

if sum + dif == b:
    print(True)
else:
    print(False)
