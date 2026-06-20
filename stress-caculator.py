def Force():
  while True:
    try:
      F=float(input("Enter force (N): "))
      break
    except ValueError:
      print("Enter an numerical value")
  return F
def Area():
  while True:
    try:
      A=float(input("Enter area (mm²): "))
      if (A<=0):
        print("Enter an positive value")
        continue
      break
    except ValueError:
      print("Enter an numerical value")
  return A

def stress(F,A):
  sigma=F/A
  if (F<0):
    print(f"Axial stress: {sigma:.2f} MPa (Compressive)")
  elif(F>0):
    print(f"Axial stress: {sigma:.2f} MPa (Tensile)")
  else:
    print("No force Applied")
  return sigma

F=Force()
A=Area()
stress(F,A)



