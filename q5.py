import math

def circleAreaCoverage(ri, r2):
  if not (isinstance(r1, int) and isinstance(r2, int)):
    return "Radii must be integers."
  if r1 <= 0 or r2 <= 0:
    return "Radii must be positive."
  area1 = math.pi * r1**2
  area2 = math.pi * r2**2

  smaller = min(area1, area2)
  larger = max(area1, area2)

  percentage = (smaller / larger) * 100
  return percentage

print(circleAreaCoverage(3,5))

