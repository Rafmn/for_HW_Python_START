# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

def profit(dict_com):
    # prof_list = []
    # for v in dict_com.values():
    #     prof_list.append(sum(v))
    prof_list = map(sum, dict_com.values())

    return all(x>=0 for x in prof_list)
    # prof_list = all(x>=0 for x in map(sum, dict_com.values()))
    # return prof_list


dict_companies = dict(company_1=[45, -4, 56, 67, -3], comp_2=[56, -56, 34, 9],\
     comps_3=[-54, -34, 67, -32], commmpp_4=[45, -2, 78, -2])


print(profit(dict_companies))

# В одну строку
print(all(x>=0 for x in map(sum, dict_companies.values())))
