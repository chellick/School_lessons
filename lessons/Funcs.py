from PIL import Image
import numpy as np


def pairwise(iterable):
    a = iter(iterable)
    if len(iterable) % 2 == 1:
        a = iter(iterable + [None])
    return zip(a, a)

# l = [1, 2, 3, 4]
# for x, y in pairwise(l):
#    print(x, y)


def del_empty_rows(array):
    del_on_y = []
    for i in range(len(array)):
        if sum(array[i]) == 0:
            # differ for reas if we got > 1 rows fpr delling:
            # 0000 -> i = 0.       after del i == 0:
            # 0100 -> i = 1                             0100 -> i = 0
            # 0000 -> i = 2            -->              0000 -> i = 1 <- (1 = i - len(del_on_y - 1) = 2 - 1)
            del_on_y.append(i - len(del_on_y))
    for i in range(len(del_on_y)):
        array = np.delete(array, (del_on_y[i]), axis=0)
    return array



def get_upleft_index(mat, finding_value):
    left_ind_none = (99999999999999999999999, 999999999999999999999999999)
    left_ind = left_ind_none
    for i in range(len(mat)):
        if finding_value in mat[i]:
            left_ind = (i, (np.where(mat[i] == finding_value)[0][0]))
            break
    if left_ind == left_ind_none:
        return None
    return left_ind
    left_ind = int(left_ind[0]), int(left_ind[1])  # x, y


mat = np.array([
    [5, 2, 2, 0],
    [0, 2, 4, 0],
    [0, 9, 3, 0],
    [2, 1, 0, 5]
])
# print(get_upleft_index(mat, 5))


def concatenate_images(image1, image0, side=None, step=0):
    from PIL import Image
    width, height, = image0.size
    width1, height1 = image1.size
    width, height = max(width, width1), max(height, height1)
    if side == 'up':
        new_image = Image.new('RGBA', (width, height * 2), (0, 0, 0, 0))
        new_image.paste(image0, (0, height - step), image0)
        new_image.paste(image1, (0, 0), image1)
        return new_image, (0, height - step)
    if side == 'down':
        new_image = Image.new('RGBA', (width, height * 2), (0, 0, 0, 0))
        new_image.paste(image0, (0, 0), image0)
        new_image.paste(image1, (0, height - step), image1)
        return new_image, (0, height - step)
    if side == 'left':
        new_image = Image.new('RGBA', (width * 2, height), (0, 0, 0, 0))
        new_image.paste(image0, (width - step, 0), image0)
        new_image.paste(image1, (0, 0), image1)
        return new_image, (width - step, 0)
    if side == 'right':
        new_image = Image.new('RGBA', (width * 2, height), (0, 0, 0, 0))
        new_image.paste(image0, (0, 0), image0)
        new_image.paste(image1, (width - step, 0), image1)
        return new_image, (width - step, 0)


# image1, image2 = Image.open('src/image/Image.png'), Image.open('src/image/dog.png')
# concatenate_images(image1, image2, right=1)



matrix1 = np.array(([1, 0, 1],
                  [1, 0, 1],
                  [1, 1, 1]))
matrix2 = np.array(([1, 1],
                  [-1, 1],
                  [-1, 1]))
matrix2 += 1
zeroes = np.zeros((len(matrix2), 1))


def zeroing_matrix(matrix1, matrix2):
    f = 0
    if len(matrix2[0]) > len(matrix1[0]):
        matrix1, matrix2 = matrix2, matrix1
        f = 1
    zeroes = np.zeros((len(matrix2), (len(matrix1[0]) - len(matrix2[0]))))
    zeroed_matrix = np.append(matrix2, zeroes, axis=1)
    if f:
        return zeroed_matrix, matrix1
    return matrix1, zeroed_matrix


matrix1, matrix2 = zeroing_matrix(matrix1, matrix2)


def differ_width_matrix_conc(matrix1, matrix2):
    return np.concatenate((zeroing_matrix(matrix1, matrix2)))


def concatenate_matrixes(obj1, obj2):
    # table1, table2 = obj1.main_matrix, obj2.main_matrix
    table1, table2 = obj1, obj2
    table1, table2 = zeroing_matrix(table1, table2)
    # print(type(table1))
    width1, height1, = len(table1), len(table1[0])
    width2 = len(table2)
    # print('width1, width2 in concatenate_matrixes:', width1, width2)
    overlay = False
    step = 0
    while not overlay and step < height1:
        step += 1
        summary_step = step * 2 # because its 2 rows from 2 matrixes
        ind_of_row1 = height1 - step # down row from up matrix
        ind_of_row2 = step - 1 # up row from down matrix
        for x in range(width1):
            val1 = table1[ind_of_row1][x]
            val2 = table2[ind_of_row2][x]
            if val1 > 0 and val2 > 0: # it seems overlaying
                overlay = True
                step -= 1
                break

                # start summation rows

    matrix_intersection = np.array([])
    # print('final step:', step == 0)
    if step == 0:
        return np.concatenate((table1, table2))
    for i in range(step):
        ind1 = height1 - step + i
        ind2 = i
        # print(11111111111, table1[ind1], table2[ind2])
        rez_row = np.array([table1[ind1] + table2[ind2]])
        # print('rez row', rez_row)
        if len(matrix_intersection) == 0:
            matrix_intersection = rez_row
        else:
            # print('m', matrix_intersection, 'r', rez_row)
            matrix_intersection = np.concatenate((matrix_intersection, rez_row))
    up_part = table1[:(height1 - step)]
    middle_part = matrix_intersection
    down_part = table2[step:]
    # print(up_part)
    # print(middle_part)
    # print(down_part)

    result_matrix = np.concatenate((up_part, middle_part, down_part))
    return result_matrix




print('INPUT:')
a = (concatenate_matrixes(matrix2, matrix1))
print("FIRST MATRIX:")
print(matrix2)
print("SECOND MATRIX:")
print(matrix1)
print('RESULT:')
print(a)
