import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("c:/Work/repo/math-code/vrp/img/Viena.jfif")

fig, ax = plt.subplots()

plt.imshow(
    img,
    extent=[0, 10, 0, 100],   # межі координат
    aspect='auto',
    zorder=0
)

# Ваш графік поверх фону
plt.plot([1, 3, 5, 7, 9], [10, 20, 40, 60, 80], zorder=1)

plt.show()
