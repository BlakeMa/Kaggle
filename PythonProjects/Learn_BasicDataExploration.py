import pandas as pd
import os
import datetime
def csvFileReader(filePath):
    melboure_data = pd.read_csv(filePath)
    melboure_data.describe(include='all')
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 2000)
    print(melboure_data.describe())
    ###print(melboure_data)
    df = pd.DataFrame(data=melboure_data)
    print(melboure_data['Price'].describe().mean())
melboure_file_path = "/Resources/CSV/melb_data.csv"
print(os.getcwd()+melboure_file_path)
csvFileReader(os.getcwd()+melboure_file_path)
print(datetime.datetime.now().year)
