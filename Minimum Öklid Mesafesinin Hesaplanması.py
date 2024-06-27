import math

# Noktaların tanımlanması
points = [(0, 0), (3, 4), (5, 12), (8, 15)]

# Öklid mesafesi için fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

# Minimum mesafenin bulunması
min_distance = min(distances)
print("Minimum mesafe:", min_distance)