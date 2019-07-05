from math import sqrt
from operator import itemgetter
from random import uniform, randint


def read_data(path):
    file = open(path, "r")
    data = []
    for x in file:
        data.append(x)
    file.close()
    return data


def print_arr(arr):
    for x in arr:
        print(x)


def split_data(data, test_size, numberof_species):
    species_size = int(len(data) / numberof_species)
    split_train, split_test = [], []
    for i in range(numberof_species):
        train_data = data[i * species_size:((i + 1) * species_size - test_size)]
        test_data = data[(i + 1) * species_size - test_size:(i + 1) * species_size]
        split_train += train_data
        split_test += test_data
    return split_train, split_test


def parse_arr(data):
    ret_list = []
    for i in data:
        temp = i.split(',')
        # j = 0
        # while j < len(temp) - 1:
        #     temp[j] = float(temp[j])
        #     j += 1
        ret_list.append(temp)

    return ret_list


def distance_calc(test, train, p):
    distance_list = []
    dist = 0
    for i in train:
        k = 0
        while k < len(test) - 1:
            dist += abs(float(i[k]) - float(test[k])) ** p
            k += 1
        if p == 2:
            dist = sqrt(dist)
        distance_list.append([i[-1], dist])
        dist = 0
        distance_list.sort(key=itemgetter(1), reverse=False)
    return distance_list


def most_frequent(input_list):
    species_list = []
    for i in input_list:
        species_list.append(i[0])
    return max(set(species_list), key=species_list.count)


def knn(train, test, k_value, p_value):
    result = []
    for i in test:
        # distance_list = distance_calc(i, train, p_value)
        distance_list = distance_calc(i, train, p_value)
        nearest = distance_list[:k_value]
        # distance_list.sort(key=lambda x: x.distance, reverse=False)
        # nearest = distance_list[:k_value]
        common = most_frequent(nearest)
        result.append([i[-1], common])
    return result


def success_rate(input_list):
    count = 0
    for i in input_list:
        if i[0] == i[1]:
            count += 1
    return count / len(input_list)


def predict_result(result_list, test_size):
    base_matrix = ["Iris-setosa\n", "Iris-versicolor\n", "Iris-virginica\n"]
    temp = [0, 0, 0]
    conf_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    count, i = 0, 0
    while i < len(base_matrix):
        arr = result_list[i * test_size:(i + 1) * test_size]
        for j in arr:
            if j[0] == j[1]:
                count += 1
            else:
                index = base_matrix.index(j[1])
                temp[index] += 1
        # print(result_list[test_size * i].name + "true success times is" + str(count))
        conf_matrix[i] = temp
        conf_matrix[i][i] = count
        count = 0
        temp = [0, 0, 0]
        i += 1
    return conf_matrix


# for random central points case parameter must have true,
# otherwise points created from one of data
def central_create(min_val, max_val, k_value, dimension, input_data, case):
    central = []
    i = 0
    while i < k_value:  # create central points k times
        point = []
        if case:  # random point creation
            for j in range(dimension):
                a = uniform(min_val, max_val)
                point.append(float("{0:.2f}".format(a)))
            point.append(i)
        else:  # create point from dataset
            index = randint(0, len(input_data))
            point = input_data[index]
            point = point[:-1]  # remove its label
            point.append(i)  # add central point label
        central.append(point)  # add it into the central inner list
        i += 1
    return central


def k_means(input_data, central_points, p_value):
    result = []
    for i in input_data:
        distance = distance_calc(test=i, train=central_points, p=p_value)
        result.append([i, distance[0][0]])
    return result
