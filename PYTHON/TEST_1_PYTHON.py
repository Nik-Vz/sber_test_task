import re


def good_number(txt):
    n_list = re.findall(r"\b\d{2,4}\\\d{2,5}\b", txt)
    good_number_list = []

    for n in n_list:
        a, b = n.split("\\")
        good_number_list.append("\\".join((a.rjust(4, "0"), b.rjust(5, "0"))))

    return  good_number_list


txt = input("Введите строку текста\n")
print(good_number(txt))