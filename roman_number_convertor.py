
#this app convert interger to roman numbers

from collections import OrderedDict


def conv_to_roman(n):

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_n(n):
        for r in roman.keys():
            x, y = divmod(n, r)
            yield roman[r] * x
            n -= (r * x)
            if n > 0:
                roman_n(n)
            else:
                break

    return "".join([a for a in roman_n(n)])


n = input('Enter the number you want to convert in roman: ')
print (conv_to_roman(int(n)))
