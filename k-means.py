from Utils import *
import matplotlib.pyplot as plt
from collections import Counter


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


def scater_graph(input_data, centrals, k_val, label):
    data_type = []
    x_val, y_val = [], []
    center_x, center_y = [], []
    colors = ['b', 'g', 'c', 'r', 'm', 'y', 'k', 'w']
    i = 0
    while i < k_val:
        data_type.append(classifier(input_data, i))
        i += 1
    i = 0
    while i < k_val:
        temp_x, temp_y = arr_split(data_type[i], 0, 1)
        x_val.append(temp_x)
        y_val.append(temp_y)
        i += 1
    i = 0
    while i < k_val:
        center_x.append(float(centrals[i][0]))
        center_y.append(float(centrals[i][1]))
        i += 1
    plt.subplot(1, 2, 1)
    i = 0
    while i < k_val:
        plt.scatter(x_val[i], y_val[i], edgecolors=colors[i])
        plt.scatter(center_x[i], center_y[i], edgecolors=colors[i], linewidths=5)
        i += 1
    plt.title(label)
    plt.xlabel("SepalLenght")
    plt.ylabel("Sepalwidth")
    # second scatter graph
    x_val.clear()
    y_val.clear()
    i = 0
    while i < k_val:
        temp_x, temp_y = arr_split(data_type[i], 2, 3)
        x_val.append(temp_x)
        y_val.append(temp_y)
        i += 1
    center_x.clear()
    center_y.clear()
    i = 0
    while i < k_val:
        center_x.append(float(centrals[i][2]))
        center_y.append(float(centrals[i][3]))
        i += 1
    plt.subplot(1, 2, 2)
    i = 0
    while i < k_val:
        plt.scatter(x_val[i], y_val[i], edgecolors=colors[i])
        # plt.legend(str(i))
        plt.scatter(center_x[i], center_y[i], edgecolors=colors[i], linewidths=5)
        # plt.legend("l2")
        i += 1
    plt.title(label)
    plt.xlabel("PetalLength")
    plt.ylabel("PetalWidth")
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
def iterate(new_list, old_list, centrals, k_val, label):
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
    scater_graph(ret_list, new_centrals, k_val, label)
    return ret_list, new_centrals, center_change_amount(centrals, new_centrals, 4)


def success_rate(result_data, k_val):
    data_types, central_data, common_type = [], [], []
    i = 0
    while i < k_val:
        data_types.append(classifier(result_data, i))
        i += 1
    for i in data_types:
        common_val = []
        for j in i:
            common_val.append(j[-1])
        central_data.append(common_val)
    for i in central_data:
        words_to_count = (word for word in i if word[:1].isupper())
        c = Counter(words_to_count)
        temp = c.most_common(1)
        # common_type.append(temp[0])
        print(temp)
    return common_type


def data_plot(setosa, versicolor, virginia):
    x1_val, y1_val = arr_split(setosa, 0, 1)
    x2_val, y2_val = arr_split(versicolor, 0, 1)
    x3_val, y3_val = arr_split(virginia, 0, 1)
    plt.subplot(1, 2, 1)
    plt.scatter(x1_val, y1_val, edgecolors='b')
    plt.scatter(x2_val, y2_val, edgecolors='g')
    plt.scatter(x3_val, y3_val, edgecolors='c')
    plt.title("initial condition")
    plt.xlabel("SepalLenght")
    plt.ylabel("Sepalwidth")
    x1_val, y1_val = arr_split(setosa, 2, 3)
    x2_val, y2_val = arr_split(versicolor, 2, 3)
    x3_val, y3_val = arr_split(virginia, 2, 3)
    plt.subplot(1, 2, 2)
    plt.scatter(x1_val, y1_val, edgecolors='b')
    plt.scatter(x2_val, y2_val, edgecolors='g')
    plt.scatter(x3_val, y3_val, edgecolors='c')
    plt.xlabel("PetalLength")
    plt.ylabel("PetalWidth")
    plt.title("initial condition")
    plt.show()
    plt.close()


if __name__ == '__main__':
    data = read_data("iris.data")
    read_data = parse_arr(data)
    setosa = read_data[:50]
    versicolor = read_data[50:100]
    virginia = read_data[100:150]
    # true for random values, false for random data selection
    k_value = 3
    central_points = central_create(min_val=0, max_val=8, k_value=k_value, dimension=4, input_data=read_data,
                                    case=False)
    result_list = k_means(read_data, central_points, 2)  # result list type [data,central_point]
    scater_graph(result_list, central_points, k_value, "iteration 1")
    change_amount, treshold, i = 90, 0.8, 2
    while change_amount > treshold:
        result_list, central_points, change_amount = iterate(result_list, read_data, central_points, k_value, "iteration "+str(i))
        print("central point change amount" + str(change_amount))
        i += 1
    success_rate(result_list, k_value)
    print(central_points)
    data_plot(setosa, versicolor, virginia)
