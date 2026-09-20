def transpose(mat: list[list[float | int]]) -> list[list]:
    '''
    Поменять строки и столбцы местами. Пустая матрица [] → [].
    Если матрица «рваная» (строки разной длины) — ValueError.
    '''
    if len(mat) == 0:
        return []
    cnt = mat[0]
    final_list = []
    for i in mat:
        if len(i) != len(cnt):
            raise ValueError('рваная матрица')
    return [list(i) for i in zip(*mat)]

def row_sums(mat: list[list[float | int]]) -> list[float]:
    '''
    Сумма по каждой строке. Требуется прямоугольность 
    '''
    final_list = []
    cnt = mat[0]
    for i in mat:
        if len(i)!=len(cnt):
              raise ValueError('рваная матрица')
        final_list.append(sum(i))
    return final_list


def col_sums(mat: list[list[float | int]]) -> list[float]:
    '''
    Сумма по каждому столбцу. Требуется прямоугольность.
    '''
    final_list = [i*0 for i in range(len(mat[0]))]
    cnt = mat[0]
    for i in mat:
        if len(i)!=len(cnt):
            raise ValueError('рваная матрица')
        for j in range(len(i)):
            final_list[j]+=i[j]
    return final_list

print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
# print(transpose([[1, 2], [3]]))

print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
# print(row_sums([[1, 2], [3]]))

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
# print(col_sums([[1, 2], [3]]))
