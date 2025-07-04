def solve(boys: list, girls: list):
    result =  ""# в эту строку сохраните полученные пары или сообщение "Кто-то может остаться без пары!"
    res = []
    if len(boys) == len(girls): # проверьте, что длины списков одинаковы
        for b, s in zip(sorted(boys),sorted(girls)): # отсортируйте пары, объедините при помощи zip и распакуйте в цикле
            res.append(f'{b} и {s}')
        result = ', '.join(res)
    else:
        result = "Кто-то может остаться без пары!"
    return result



