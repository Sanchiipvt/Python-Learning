weight = float(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"Weight is Kg is: {converted} kgs")
else:
    converted = weight / 0.45
    print(f"Weight is Kg is: {converted} pounds")
