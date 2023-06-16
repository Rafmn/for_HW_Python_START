# Напишите функцию для транспонирования матрицы

def trans_matrix(a_matrix):
    tr_matrix = []
    for i in range(len(a_matrix[0])):
        # ls = []
        # for j in range(len(a_matrix)):
        #     ls.append(a_matrix[j][i])
        ls = [a_matrix[j][i] for j in range(len(a_matrix))]
        tr_matrix.append(ls)
    return(tr_matrix)


n = int(input('Количество строк в матрице: '))

matrix = []
for i in range(n):
    l = list(map(int, input(f'Введите числа через пробел в строке {i+1}: ').split()))
    matrix.append(l)

print('Исходная матрица:', *matrix, sep='\n')
print()
print('Транспонированная матрица:', *trans_matrix(matrix), sep='\n')
