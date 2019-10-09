a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
D = ((b**2) - 4 * a * c)
if a < 0:
    print('please wrtite normaly a')
else:
    if D > 0:
        print('We have 2 solution')
    elif D == 0:
        print('We have 1 solution')
    elif D < 0:
        print('We have 2 solution')
