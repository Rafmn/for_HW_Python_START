list_one = ['Katya', 34500, '10.25%']
list_two = ['Vera', 56000, '10.15%']
list_three = ['Lyaisan', 40500, '9.45%']


def my_dict(a_list):
    per = float(a_list[2][:-1])
    name = a_list[0]
    a_prem = a_list[1] * per * 0.01
    return name, a_prem


a_dict = {k: p for k, p in map(my_dict, [list_one, list_two, list_three])}
print(a_dict)
