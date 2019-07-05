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
def arr_split(input_data, index1, index2):
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
        mean_list[j] = float("{0:.2f}".format(a))
        j += 1
    return mean_list


def color_bar(index):
    color_matrix = []


def scater_graph(input_data, centrals, k_value):
    data_type = []
    x_val, y_val = [], []
    center_x, center_y = [], []
    colors = ['#37AB65', '#3DF735', '#AD6D70', '#EC2504', '#8C0B90', '#C0E4FF', '#27B502', '#7C60A8', '#CF95D7',
              '#F6CC1D']
    i = 0
    while i < k_value:
        data_type.append(classifier(input_data, i))
        i += 1
    # data_type1 = classifier(input_data, 0)
    # data_type2 = classifier(input_data, 1)
    # data_type3 = classifier(input_data, 2)
    i = 0
    while i < k_value:
        temp_x, temp_y = arr_split(data_type[i], 0, 1)
        x_val.append(temp_x)
        y_val.append(temp_y)
        i += 1
    # x1_val, y1_val = arr_split(data_type1, 0, 1)
    # x2_val, y2_val = arr_split(data_type2, 0, 1)
    # x3_val, y3_val = arr_split(data_type3, 0, 1)
    i = 0
    while i < k_value:
        center_x.append(float(centrals[i][0]))
        center_y.append(float(centrals[i][1]))
        i += 1
    # center1x, center1y = float(centrals[0][0]), float(centrals[0][1])
    # center2x, center2y = float(centrals[1][0]), float(centrals[1][1])
    # center3x, center3y = float(centrals[2][0]), float(centrals[2][1])
    plt.subplot(1, 2, 1)
    i = 0
    while i < k_value:
        plt.scatter(x_val[i], y_val[i], edgecolors=colors[i])
        plt.scatter(center_x[i], center_y[i], edgecolors=colors[i], linewidths=5)
        i += 1
    # plt.scatter(x1_val, y1_val, edgecolors='b')
    # plt.scatter(x2_val, y2_val, edgecolors='r')
    # plt.scatter(x3_val, y3_val, edgecolors='c')
    # plt.scatter(center1x, center1y, edgecolors='b', linewidths=5)
    # plt.scatter(center2x, center2y, edgecolors='r', linewidths=5)
    # plt.scatter(center3x, center3y, edgecolors='c', linewidths=5)
    # second scatter graph
    x_val.clear()
    y_val.clear()
    i = 0
    while i < k_value:
        temp_x, temp_y = arr_split(data_type[i], 2, 3)
        x_val.append(temp_x)
        y_val.append(temp_y)
        i += 1
    # x1_val, y1_val = arr_split(data_type1, 2, 3)
    # x2_val, y2_val = arr_split(data_type2, 2, 3)
    # x3_val, y3_val = arr_split(data_type3, 2, 3)
    center_x.clear()
    center_y.clear()
    i = 0
    while i < k_value:
        center_x.append(float(centrals[i][2]))
        center_y.append(float(centrals[i][3]))
        i += 1
    # center1x, center1y = float(centrals[0][2]), float(centrals[0][3])
    # center2x, center2y = float(centrals[1][2]), float(centrals[1][3])
    # center3x, center3y = float(centrals[2][2]), float(centrals[2][3])
    plt.subplot(1, 2, 2)
    i = 0
    while i < k_value:
        plt.scatter(x_val[i], y_val[i], edgecolors=colors[i])
        plt.scatter(center_x[i], center_y[i], edgecolors=colors[i], linewidths=5)
        i += 1
    # plt.scatter(x1_val, y1_val, edgecolors='b')
    # plt.scatter(x2_val, y2_val, edgecolors='r')
    # plt.scatter(x3_val, y3_val, edgecolors='c')
    # plt.scatter(center1x, center1y, edgecolors='b', linewidths=5)
    # plt.scatter(center2x, center2y, edgecolors='r', linewidths=5)
    # plt.scatter(center3x, center3y, edgecolors='c', linewidths=5)
    plt.show()
    plt.close()


# to calulate center change amount
def center_change_amount(old_centrals, new_centrals, dimension):
    i, change = 0, 0
    while i < len(old_centrals):
        j = 0
        while j < dimension:
            change += abs(float(new_centrals[i][j]) - float(old_centrals[i][j]))
            j += 1
        i += 1
    return change


# iterate k-means calculations and plot scatter graph
def iterate(new_list, old_list, centrals, k_val):
    new_centrals = []
    local_data, centers = [], []
    i = 0
    while i < k_val:
        local_data.append(classifier(new_list, i))
        i += 1
    # data1 = classifier(new_list, 0)
    # data2 = classifier(new_list, 1)
    # data3 = classifier(new_list, 2)
    # print(centrals)
    i = 0
    while i < k_val:
        centers = meanof_data(local_data[i], 4, centrals[i])
        centers.append(i)
        new_centrals.append(centers)
        i+=1
    # center1 = meanof_data(data1, 4, centrals[0])
    # center1.append(0)
    # center2 = meanof_data(data2, 4, centrals[1])
    # center2.append(1)
    # center3 = meanof_data(data3, 4, centrals[2])
    # center3.append(2)
    # centrals.clear()
    # new_centrals.append(center1)
    # new_centrals.append(center2)
    # new_centrals.append(center3)
    # print(new_centrals)
    ret_list = k_means(old_list, new_centrals, 2)
    scater_graph(ret_list, new_centrals, k_val)
    # print(central_points)
    return ret_list, new_centrals, center_change_amount(centrals, new_centrals, 4)


if __name__ == '__main__':
    data = read_data("iris.data")
    read_data = parse_arr(data)
    # setosa = data[:50]
    # versicolor = data[50:100]
    # virginia = data[100:150]

    # true for random values, false for random data selection
    k_value = 4
    central_points = central_create(min_val=0, max_val=8, k_value=k_value, dimension=4, input_data=read_data,
                                    case=False)
    result_list = k_means(read_data, central_points, 2)  # result list type [data,central_point]
    scater_graph(result_list, central_points, k_value)
    # print(central_points)
    change_amount, treshold = 90, 0.1
    while change_amount > treshold:
        result_list, central_points, change_amount = iterate(result_list, read_data, central_points, k_value)
        print(change_amount)
