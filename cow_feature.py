import pandas as pd

cow_data = pd.read_csv('D:\Coding\python\Cow.csv')
cow_data = cow_data.drop(cow_data.columns[0], axis=1)
# Xóa các hàng mà tất cả các ô đều mang giá trị NaN
print(cow_data)
