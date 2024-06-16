# Запросить данные с помощью библиотеки requests из API и вывести их в консоль.

import requests
response = requests.get('https://www.youtube.com')
print(response.text)

# Считать данные из файла с помощью библиотеки pandas

import pandas as pd
df = pd.read_csv('data2.txt', delimiter='\t')

# Создать массив чисел с помощью библиотеки numpy

import numpy as np
arr = np.arange(10)
print(arr)

# Визуализировать данные с помощью библиотеки matplotlib

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [25, 32, 34, 20, 25]
plt.plot(x, y)
plt.show()

#  Обработать изображение с помощью библиотеки pillow

from PIL import Image
img = Image.open('img3.11112844x1600.jpg')
cropped = img.crop((0, 0, 100, 200))
cropped.save('img3.cropped_11112844x1600.jpg')
img.show()