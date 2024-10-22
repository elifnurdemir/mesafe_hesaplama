import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Noktaların tanımlanması
points = [(1, 2), (4, 6), (7, 8), (2, 3)]  # Buraya dilediğiniz kadar nokta ekleyebilirsiniz.

# Mesafeleri saklamak için boş bir liste
distances = []

# Her nokta çifti arasındaki mesafeyi hesaplayıp distances listesine ekleme
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# En küçük mesafeyi bulma
min_distance = min(distances)

# Sonuçları yazdırma
print("Her iki nokta çifti arasındaki mesafeler:", distances)
print("En kısa mesafe:", min_distance)
