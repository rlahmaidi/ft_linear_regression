# not needed for now , just keeping them here in case

# def denormalize_price(price):
#     mean, std = get_mean_std("meanStd.csv")
#     print("the mean and std", mean, std)
#     reel_price = price * std + mean
#     return reel_price
# def denormalize_parametres(theta0, theta1):
#     theta1 = theta1 * (np.std(price) / np.std(mileage))
#     theta0 = np.mean(price) - theta1 * np.mean(mileage)


# def get_mean_std(file_name):
#     try:
#         with open(file_name, 'r') as csvfile:
#             csvreader = csv.reader(csvfile, delimiter=' ')
#             rows = next(csvreader)
#             mean_std = rows[0].split(',')
#             # print("is theats a list her", type(thetas))
#     except:
#         return 0,0
#     return float(mean_std[0]), float(mean_std[1])

# saving mean and std if needed
    # with open('meanStd.csv', 'w', newline= '') as csvfile:
    #     mean_std = csv.writer(csvfile)
    #     mean_std.writerow([price_mean, price_deviation])