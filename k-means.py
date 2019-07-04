from Utils import *
import matplotlib.pyplot as plt


# divide data due to its central point
def classifier(input_list, type):
    return_list = []
    for i in input_list:
        if i[1] == type:
            return_list.append(i[0])
    return return_list


# create new array from particular matrix index
def arr_concat(input_data, index1, index2):
    result1, result2 = [], []
    for i in input_data:
        result1.append(float(i[index1]))
        result2.append(float(i[index2]))
    return result1, result2


def meanof_data(input_data, dimension, center_value):
    mean_list = []
    for i in range(dimension):
        mean_list.append(0)
    for i in input_data:
        j = 0
        while j < dimension:
            mean_list[j] += float(i[j])
            j += 1
    numberof_item = len(input_data)
    if numberof_item == 0:
        return center_value
    j = 0
    while j < dimension:
        a = (mean_list[j] / numberof_item)
        mean_list[j] = "{0:.2f}".format(a)
        # mean_list[j] = (mean_list[j] / numberof_item)
        j += 1
    return mean_list


def scater_graph(input_data, central_points):
    data_type1 = classifier(result_list, 0)
    data_type2 = classifier(result_list, 1)
    data_type3 = classifier(result_list, 2)
    x1_val, y1_val = arr_concat(data_type1, 0, 1)
    x2_val, y2_val = arr_concat(data_type2, 0, 1)
    x3_val, y3_val = arr_concat(data_type3, 0, 1)
    center1x, center1y = float(central_points[0][0]), float(central_points[0][1])
    center2x, center2y = float(central_points[1][0]), float(central_points[1][1])
    center3x, center3y = float(central_points[2][0]), float(central_points[2][1])
    plt.subplot(1, 2, 1)
    plt.scatter(x1_val, y1_val, edgecolors='b')
    plt.scatter(x2_val, y2_val, edgecolors='r')
    plt.scatter(x3_val, y3_val, edgecolors='c')
    plt.scatter(center1x, center1y, edgecolors='b', linewidths=5)
    plt.scatter(center2x, center2y, edgecolors='r', linewidths=5)
    plt.scatter(center3x, center3y, edgecolors='c', linewidths=5)
    # second scatter graph
    x1_val, y1_val = arr_concat(data_type1, 2, 3)
    x2_val, y2_val = arr_concat(data_type2, 2, 3)
    x3_val, y3_val = arr_concat(data_type3, 2, 3)
    center1x, center1y = float(central_points[0][2]), float(central_points[0][3])
    center2x, center2y = float(central_points[1][2]), float(central_points[1][3])
    center3x, center3y = float(central_points[2][2]), float(central_points[2][3])
    plt.subplot(1, 2, 2)
    plt.scatter(x1_val, y1_val, edgecolors='b')
    plt.scatter(x2_val, y2_val, edgecolors='r')
    plt.scatter(x3_val, y3_val, edgecolors='c')
    plt.scatter(center1x, center1y, edgecolors='b', linewidths=5)
    plt.scatter(center2x, center2y, edgecolors='r', linewidths=5)
    plt.scatter(center3x, center3y, edgecolors='c', linewidths=5)
    plt.show()
    plt.close()


def iterate(input_list, centrals):
    data1 = classifier(input_list, 0)
    data2 = classifier(input_list, 1)
    data3 = classifier(input_list, 2)
    # print(centrals)
    center1 = meanof_data(data1, 4, centrals[0])
    center1.append(0)
    center2 = meanof_data(data2, 4, centrals[1])
    center2.append(1)
    center3 = meanof_data(data3, 4, centrals[2])
    center3.append(2)
    centrals.clear()
    centrals.append(center1)
    centrals.append(center2)
    centrals.append(center3)
    # print(centrals)
    result_list = k_means(data, centrals, 2)
    scater_graph(result_list, centrals)
    print(central_points)
    return result_list



if __name__ == '__main__':
    data = read_data("iris.data")
    data = parse_arr(data)
    # setosa = data[:50]
    # versicolor = data[50:100]
    # virginia = data[100:150]
    central_points = central_create(min_val=0, max_val=5, k_value=3, dimension=4, input_data=data, case=False)
    result_list = k_means(data, central_points, 2)  # result list type [data,central_point]
    scater_graph(result_list, central_points)
    # print(central_points)
    result_list = iterate(result_list, central_points)
    result_list = iterate(result_list, central_points)
    result_list = iterate(result_list, central_points)
    result_list = iterate(result_list, central_points)
