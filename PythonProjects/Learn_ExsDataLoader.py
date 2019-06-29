import  pandas as pd
import os
import datetime
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 2000)
melboure_file_path = "/Resources/CSV/train.csv"
train_data = pd.read_csv(os.getcwd()+melboure_file_path)
print(int(train_data.describe()["Age"].max()))


###home_data = pd.read_csv(iowa_file_path)
###home_data.describe()
###What is the average lot size (rounded to nearest integer)?
##avg_lot_size = round(home_data["LotArea"].mean())
# As of today, how old is the newest home (current year - the date in which it was built)
##newest_home_age = 2019-home_data["YearBuilt"].max()