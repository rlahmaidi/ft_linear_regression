import csv
import numpy as np

def read_csv(file_name):
    # with open(file_name) as csv_file:
    #     csv_read=csv.reader(csv_file, delimiter=',')
    #     for el in csv_read:
    #         print(el)
    # file = open(file_name)
    # csv_read = csv.reader(file,delimiter=',')
    # lst = list(csv_read)
    # print(len(lst))
    # file.close()
    # return csv_read
    arr = np.genfromtxt(file_name, delimiter=',')
    return arr

def scale_features(mileage, price):
    mileage_mean = np.sum(mileage) / len(mileage)
    print("the mean mileage is:", mileage_mean)
    price_mean = np.sum(price) / len(price)
    mileage_deviation = (np.sum((mileage - mileage_mean)**2) / len(mileage))**(1/2)
    print("the milleage deviation is", mileage_deviation)
    price_deviation = (np.sum(price - price_mean) / len(price))**(1/2)
    mileage_normalazied = (mileage - mileage_mean) / mileage_deviation
    print(len(mileage_normalazied))
    # print("milleage normalized", mileage_normalazied)
    price_normalazied = (price - price_mean) / price_deviation
    # print("len of price_normalized", len(price_normalazied))
    # print("type of price normalized is", type(price_normalazied))
    # print("price normalized is")
    # print(price_normalazied)
    # print("milleage normalized type is ")
    # print(mileage_normalazied.dtype)
    return np.round(mileage_normalazied), np.round(price_normalazied)

def calculate_loss(estimate_price, price):
    loss = np.sum(abs(estimate_price - price)) / len(price)
    return loss

def estimate_price(mileage, theta0, theta1):
    # estimated_prices = []
    # for el in mileage:
    #     estimated_prices.append(theta1 * el + theta0)
    # return np.array(estimated_prices)
    e_p = (mileage * theta1) + theta0
    e_p = np.round(e_p, 4)
    print(e_p)
    return e_p

def claculate_thetas(mileage, price):
    theta0 = 0
    theta1 = 0
    max_iteration = 1000
    nb_iteration = 0
    learning_rate = 0.1
    while(nb_iteration < max_iteration):

        estimated_prices = estimate_price(mileage, theta0, theta1)
        # print("estimate prices returned is", estimated_prices)
        if nb_iteration == 3:
            break
        loss = calculate_loss(estimated_prices, price)
        # print(estimated_prices)
        if loss < 10**(-5):
            break
        theta0 = (learning_rate /len(price)) * np.sum(estimated_prices - price)
        theta1 = (learning_rate /len(price)) * np.sum((estimated_prices - price) * price)
        nb_iteration += 1
    return theta0, theta1

if __name__ == "__main__":
    data = read_csv("../data.csv")
    #extract prices and mileage
    mileage = data[1:,0:1]
    price = data[1:, 1:2]
    #scale the features
    mileage_normalized, price_normalized = scale_features(mileage,price)
    # print(mileage_normalized.dtype)
    # mileage_normalized = np.round(mileage_normalized, 4)
    # price_normalized = np.round(price_normalized, 4)
    # print(mileage_normalized)
    # print(price_normalized)
    theta0, theta1 = claculate_thetas(mileage_normalized, price_normalized)
    print("value of theta0 and theta1 are:", theta0, theta1)
