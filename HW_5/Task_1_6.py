# for i in range(2, 7, 4):
#     for j in range(2, 11):
#         print(f'{i} X {j} = {i*j}\t{i+1} X {j} = {(i+1)*j}\t{i+2} X {j} = {(i+2) * j}\t{i+3} X {j} = {(i+3) * j}')
#     print()

mult = (f'{i} X {j} = {i*j}' for i in range(2, 11)