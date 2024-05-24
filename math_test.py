import math

def euclideanDistance(point1, point2):
  """
  İki nokta arasındaki Öklid mesafesini hesaplar.

  Args:
    point1: (x1, y1) şeklinde bir demet olan ilk nokta.
    point2: (x2, y2) şeklinde bir demet olan ikinci nokta.

  Returns:
    İki nokta arasındaki Öklid mesafesi.
  """
  x1, y1 = point1
  x2, y2 = point2
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def main():
  # Noktaları tanımlayın
  points = [(1, 2), (4, 6), (3, 0), (5, 7)]

  # Mesafeleri hesaplayın
  distances = []
  for i in range(len(points)):
    for j in range(i + 1, len(points)):
      distance = euclideanDistance(points[i], points[j])
      distances.append(distance)

  # Minimum mesafeyi bulun
  minDistance = min(distances)

  # Minimum mesafeyi yazdırın
  print("Minimum mesafe:", minDistance)

if __name__ == "__main__":
  main()