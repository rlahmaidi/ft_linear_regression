import csv
import numpy as np
import sys
import matplotlib.pyplot as plt

def read_csv(file_name):
    try:
        arr = np.genfromtxt(file_name, delimiter=',')
    except:
        print("a csv file containing the training data " +
        "should be present at current folder")
        sys.exit()
    return arr

def scale_features(mileage, price):
    mileage_mean = np.sum(mileage) / len(mileage)
    price_mean = np.sum(price) / len(price)
    mileage_deviation = (np.sum((mileage - mileage_mean)**2) / len(mileage))**(1/2)
    price_deviation = (np.sum((price - price_mean)**2) / len(price))**(1/2)
    mileage_normalazied = (mileage - mileage_mean) / mileage_deviation
    price_normalazied = (price - price_mean) / price_deviation
    return mileage_normalazied, price_normalazied

def calculate_loss(estimate_price, price):
    loss = np.sum(abs(estimate_price - price)) / len(price)
    return loss

def estimate_price(mileage, theta0, theta1):
    e_p = (mileage * theta1) + theta0
    e_p = np.round(e_p, 8)
    return e_p

def claculate_thetas(mileage, price):
    theta0 = 0
    theta1 = 0
    max_iteration = 1000
    nb_iteration = 0
    learning_rate = 0.01
    m = len(price)
    while(nb_iteration < max_iteration):

        estimated_prices = estimate_price(mileage, theta0, theta1)
        # print("estimate prices returned is", estimated_prices)
        loss = calculate_loss(estimated_prices, price)
        # print(estimated_prices)
        if loss < 10**(-5):
            break
        #caluculate gradient
        tmp_theta0 = learning_rate *(1/m) * np.sum(estimated_prices - price)
        tmp_theta1 = learning_rate*(1/m) * np.sum((estimated_prices - price) * mileage)
        #update thetas(parametres)
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
        nb_iteration += 1
    return theta0, theta1

def plot_data(price, mileage, theta0, theta1):
    #plot the data points scattered
    plt.scatter(mileage, price)
    #plot the regression line
    xpoints = np.linspace(np.min(mileage), np.max(mileage), 100)
    ypoints = estimate_price(xpoints, theta0, theta1)
    plt.plot(xpoints, ypoints)

    plt.show()
if __name__ == "__main__":
    data = read_csv("./data.csv")
    #extract prices and mileage
    mileage = data[1:,0:1]
    price = data[1:, 1:2]
    #scale the features
    mileage_normalized, price_normalized = scale_features(mileage,price)
    #calculate parametres
    theta0, theta1 = claculate_thetas(mileage_normalized, price_normalized)
    #denormalize parametres
    theta1 = theta1 * (np.std(price) / np.std(mileage))
    theta0 = np.mean(price) - theta1 * np.mean(mileage)
    with open('thetas.csv', 'w', newline= '') as csvfile:
        thetas = csv.writer(csvfile)
        thetas.writerow([theta0, theta1])
    #########################Bonus############
    #plotting the data
    plot_data(price, mileage, theta0, theta1)
