
start = ord("a")-1
nColumns = 3
nRows = 3
Base = []

for i in range(nRows+1):
    Rows = []
    for j in range(nColumns+1):
        if i == 0:
            if j == 0:
                value = "*"
            else:
                value = str(j)
        else:
            if j == 0:
                value = chr(start+i)
            else:
                value = "x"
        Rows.append(str(value))
    Base.append(Rows)


for i in Base:
    print(" ".join(i))
