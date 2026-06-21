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
def Moment():
  while True:
    try:
      M=float(input("Enter moment  (Nmm): "))
      break
    except ValueError:
      print("Enter an numerical value")
  return M
def Neutral_Axis():
  while True:
    try:
      Y=float(input("Enter Neutral Axis distance (mm): "))
      break
    except ValueError:
      print("Enter an numerical value")
  return Y
def MOI():
  while True:
    try:
      I=float(input("Enter Moment of Inertia (mm4): "))
      if (I<=0):
        print("Enter an positive value")
        continue
      break
    except ValueError:
      print("Enter an numerical value")
  return I
def stress(F,A):
  sigma=F/A
  if (F<0):
    print(f"Axial stress: {sigma:.2f} MPa (Compressive)")
  elif(F>0):
    print(f"Axial stress: {sigma:.2f} MPa (Tensile)")
  else:
    print("No force Applied")
  return sigma
def Bending_Stress(M, y, I):
  BS=M*y/I
  if (BS<0):
    print(f"Bending stress: {BS:.2f} MPa (Compressive)")
  elif(BS>0):
    print(f"Bending stress: {BS:.2f} MPa (Tensile)")
  else:
    print("No Moment Applied")
  return BS
F=Force()
A=Area()
stress(F,A)

M=Moment()
y=Neutral_Axis()
I=MOI()
Bending_Stress(M,y,I)



