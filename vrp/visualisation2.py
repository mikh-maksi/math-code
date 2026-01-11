import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.image as mpimg

# перенести координати до відсотків


img = mpimg.imread("c:/Work/repo/math-code/vrp/img/Viena.jfif")

# Вхідні дані
data = [
    {"Name": "Lassallestraße 1, 1020 Wien", "Let": "A", "Service_time": 5, "Lat": 48.222338, "Lon": 16.397722},
    {"Name": "Mariahilfer Straße 101, 1060 Wien", "Let": "B", "Service_time": 5, "Lat": 48.19528, "Lon": 16.33746},
    {"Name": "Landstraßer Hauptstraße 50, 1030 Wien", "Let": "C", "Service_time": 5, "Lat": 48.196056, "Lon": 16.396312},
    {"Name": "Währinger Straße 120, 1180 Wien", "Let": "D", "Service_time": 5, "Lat": 48.230005, "Lon": 16.343063}
]

# fig, ax = plt.subplots()



# Ваш графік поверх фону
# ax.plot([1, 3, 5, 7, 9], [10, 20, 40, 60, 80], zorder=1)



# Перетворення в DataFrame
df = pd.DataFrame(data)

# Створення графіку
plt.figure(figsize=(6, 6))
plt.imshow(
    img,
    extent=[0, 10, 0, 100],   # межі координат
    aspect='auto',
    zorder=0
)
plt.scatter(df["Lon"], df["Lat"], color="blue", s=50)

# Підписи точок
for _, row in df.iterrows():
    plt.annotate(row["Let"], (row["Lon"], row["Lat"]), xytext=(3, 3), textcoords="offset points")

plt.title("Візуалізація точок у Відні")
plt.xlabel("Довгота")
plt.ylabel("Широта")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

# Показ графіку
plt.show()