import numpy as np

a = np.array([[1.2, 5.2, 6.3], [4, 5, 6], [44.2, 2.4, 5.6]])
b = np.array([[2, 3, 1], [2, 3, 1], [2, 3, 1]])
c = np.random.rand(1, 5)
d = a.copy()[:, ::-1]
print("A", a)
print("D", d)
print(c)
print(a.ndim)#количество измерений в массиве
print(a.dtype)#тип данных в массиве
a_1 = np.array([3,56,5,64,78,2])
print(a_1.ndim)#количество измерений в массиве
print(a_1.dtype)#тип данных в массиве
print('У массива', a.shape,'строк и столбцов' )
print(a + 3)
print(c*2)
print(a // b)


from PIL import Image, ImageFilter

filename = "906.jpg"
with Image.open(filename) as image:
    image.load()
rotated_image = image.rotate(30)
rotated_image.show()
cmyk_image= image.convert("CMYK")
gray_image= image.convert("L")
cmyk_image.show()
gray_image.show()


red, green, blue = image.split()
zeroed_band = red.point(lambda _: 0)

red_merge = Image.merge("RGB", (red, zeroed_band, zeroed_band))
green_merge = Image.merge("RGB", (zeroed_band, green, zeroed_band))
blue_merge = Image.merge("RGB", (zeroed_band, zeroed_band, blue))

red_merge.show()
green_merge.show()
blue_merge.show()

blur_image = image.filter(ImageFilter.BLUR)
blur_image.show()

resized_image = image.resize((400, 200))
resized_image.save('resized_image.jpg')
resized_image.show()
print("Изменения фото сохранены.")


import requests

url = 'https://httpbin.org/post'
data = {'имя': 'Роза', 'возраст': 75}

r = requests.post(url, data=data)
print("-" * 15)
print(r.status_code) #  статус
print("+" * 15)
print(r.headers) # заголовок
print("+" * 15)
print(r.json()) # ответ(в виде JSON)
print("+" * 15)


r = requests.put(url, data=data)
if r.status_code == 200:
    print("Пользователь  обновлен!")
else:
    print("Ошибка:", r.status_code)
print("*" * 15)
