year = int(input())
distinct_year = False
while not distinct_year:
    year += 1
    year = str(year)
    char = len(year)
    year_d = len(set(year))
    if char == year_d:
        print(year)
        distinct_year = True
    year = int(year)






year = int(input())
distinct_year = False
while not distinct_year:
    year += 1
    year = str(year)
    q = ""
    w = ""
    e = ""
    r = ""
    for a in range(len(year)):
        if a == 0:
            q = year[a]
        if a == 1:
            w = year[a]
        if a == 2:
            e = year[a]
        if a == 3:
            r = year[a]
    if q != w and q != e and q != r:
        if w != e and w != r:
            if e != r:
                print(year)
                distinct_year = True
    year = int(year)
