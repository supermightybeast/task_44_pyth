#Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
#Ваша задача перевести его в one hot вид. 
#Сделать без встроенных ф-ций, например,get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

# Создаем пустой DataFrame, в котором будут храниться столбцы one-hot кодировки
one_hot_data = pd.DataFrame()

# Получаем уникальные значения из столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

# Для каждого уникального значения создаем новый столбец в one-hot DataFrame
for value in unique_values:
    # Создаем столбец с именем, соответствующим уникальному значению
    one_hot_data[value] = (data['whoAmI'] == value).astype(int)

one_hot_data.head()
print(data)
print(one_hot_data)