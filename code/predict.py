import csv

def get_thetas(file_name):
    # a protection is still nedded here to replace thetas with 0
    try:
        with open(file_name, 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=' ')
            rows = next(csvreader)
            thetas = rows[0].split(',')
            # print("is theats a list her", type(thetas))
    except:
        thetas = [0,0]
    return float(thetas[0]), float(thetas[1])
def get_mean_std(file_name):
    try:
        with open(file_name, 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=' ')
            rows = next(csvreader)
            mean_std = rows[0].split(',')
            # print("is theats a list her", type(thetas))
    except:
        return 0,0
    return float(mean_std[0]), float(mean_std[1])

def denormalize_price(price):
    mean, std = get_mean_std("meanStd.csv")
    print("the mean and std", mean, std)
    reel_price = price * std + mean
    return reel_price

def estimat_price(mileage, theta0, theta1):
    e_p = (mileage * theta1) + theta0
    print("price before denormalization is ", e_p)
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
    theta0, theta1 = get_thetas("thetas.csv")

    est_price = estimat_price(mileage, theta0, theta1)
    print("thetas values are:",theta0, theta1)
    print("the estimated price is:",est_price)