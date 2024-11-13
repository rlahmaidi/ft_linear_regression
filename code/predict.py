import csv
import numpy as np
import sys

def get_thetas(file_name):
    try:
        with open(file_name, 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=' ')
            rows = next(csvreader)
            thetas = rows[0].split(',')
    except:
        thetas = [0,0]
        print("seems like the model isn't trained yet,\
              default parametres will be used")
    return float(thetas[0]), float(thetas[1])

def estimat_price(mileage, theta0, theta1):
    e_p = (mileage * theta1) + theta0
    return e_p


if __name__ == "__main__":
    mileage = input("enter a milleage")
    try:
        mileage = int(mileage)
    except:
        try:
            mileage = float(mileage)
        except:
            print("the mileage should be integer of float")
            sys.exit()
    theta0, theta1 = get_thetas("thetas.csv")
    est_price = estimat_price(mileage, theta0, theta1)
    print("the estimated price of a car with "+
          str(mileage) + " mileage is: " + str(int(est_price)))