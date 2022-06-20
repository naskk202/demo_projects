a = 7200
hh = a // 3600
mm = (a % 3600) // 60
ss = (a % 3600) % 60
print(hh, mm, ss)