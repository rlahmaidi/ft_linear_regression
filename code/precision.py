import numpy as np
from linear_regression import estimate_price
from predict import get_thetas
from linear_regression import read_csv



def calculate_precision(mileage, price):
    """Calculate R-squared score"""
    theta0, theta1 = get_thetas("thetas.csv")
    predictions = estimate_price(mileage, theta0, theta1)
    ss_res = np.sum((price - predictions) ** 2)
    ss_tot = np.sum((price - np.mean(price)) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    return r2


if __name__ == "__main__":
    data = read_csv("./data.csv")
    mileage = data[1:,0:1]
    price = data[1:, 1:2]
    r2 = calculate_precision(mileage, price)
    print("the precision of our model calculated "+
          "using R-squared score is:", r2)
