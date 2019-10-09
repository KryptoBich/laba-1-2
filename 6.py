a = int(input("Enter a:"))
if a < 0 or a > 60:
    print('write normaly num')
else:
    if 0 < a < 60 and a % 5 == 4 or a % 5 == 0:
        print('red light')
    else:
        print('green light')
