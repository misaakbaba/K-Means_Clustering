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
    i = 0
    while i < k_value:
        temp_x, temp_y = arr_split(data_type[i], 0, 1)
        x_val.append(temp_x)
        y_val.append(temp_y)
        i += 1
    i = 0
    while i < k_value:
        center_x.append(float(centrals[i][0]))
        center_y.append(float(centrals[i][1]))
        i += 1
    plt.subplot(1, 2, 1)
    i = 0
    while i < k_value:
        plt.scatter(x_val[i], y_val[i], edgecolors=colors[i])
        plt.scatter(center_x[i], center_y[i], edgecolors=colors[i], linewidths=5)
        i += 1
    # second scatter graph
    x_val.clear()
    y_val.clear()
    i = 0
    while i < k_value:
        temp_x, temp_y = arr_split(data_type[i], 2, 3)
        x_val.append(temp_x)
        y_val.append(temp_y)
        i += 1
    center_x.clear()
    center_y.clear()
    i = 0
    while i < k_value:
        center_x.append(float(centrals[i][2]))
        center_y.append(float(centrals[i][3]))
        i += 1
    plt.subplot(1, 2, 2)
    i = 0
    while i < k_value:
        plt.scatter(x_val[i], y_val[i], edgecolors=colors[i])
        plt.scatter(center_x[i], center_y[i], edgecolors=colors[i], linewidths=5)
        i += 1
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
    i = 0
    while i < k_val:
        centers = meanof_data(local_data[i], 4, centrals[i])
        centers.append(i)
        new_centrals.append(centers)
        i += 1
    ret_list = k_means(old_list, new_centrals, 2)
    scater_graph(ret_list, new_centrals, k_val)
    return ret_list, new_centrals, center_change_amount(centrals, new_centrals, 4)


if __name__ == '__main__':
    data = read_data("iris.data")
    read_data = parse_arr(data)
    # setosa = data[:50]
    # versicolor = data[50:100]
    # virginia = data[100:150]

    # true for random values, false for random data selection
    k_value = 5
    central_points = central_create(min_val=0, max_val=8, k_value=k_value, dimension=4, input_data=read_data,
                                    case=False)
    result_list = k_means(read_data, central_points, 2)  # result list type [data,central_point]
    scater_graph(result_list, central_points, k_value)
    change_amount, treshold = 90, 0.1
    while change_amount > treshold:
        result_list, central_points, change_amount = iterate(result_list, read_data, central_points, k_value)
        print(change_amount)
