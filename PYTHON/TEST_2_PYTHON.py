def new_atm(n, k, l):

    l_start = [[a, 1] for a in l]

    for i in range(1, k + 1):
        max_ind = l_start.index(max(l_start))
        x = l_start[max_ind][1]
        l_start[max_ind][0] = round(l[max_ind] / (x + 1), 2)
        l_start[max_ind][1] += 1

    l_finish = []

    for num, count in l_start:
        for i in range(count):
            if num * 10 % 10 > 0:
                l_finish.append(num)
            else:
                l_finish.append(int(num))

    return l_finish


n, k = [int(i) for i in input("Введите n, k через пробел\n").split()]
l = [int(input("Введите расстояние\n")) for i in range(n)]

print(new_atm(n, k, l))
