from cmath import sqrt

s = 0
u = 0
v = 0
a = 0
t = 0
finds = False
findu = False
findv = False
finda = False
findt = False
strue = False
utrue = False
vtrue = False
atrue = False
ttrue = False



whichvalue = input("Which value are you finding? ")
if whichvalue.lower() == ("s"):
	finds = True
if whichvalue.lower () == ("u"):
	findu = True
if whichvalue.lower () == ("v"):
	findv = True
if whichvalue.lower () == ("a"):
	finda = True
if whichvalue.lower () == ("t"):
	findt = True
if finds == True:
	isu = input("Is there a Inital Velocity Value? Y/N ")
	if isu.lower () == ("y"):
		u = float(input("Insert value for U: "))
		utrue = True
	isv = input("Is there a Final Velocity Value? Y/N ")
	if isv.lower () == ("y"):
		v = float(input("Insert value for V: "))
		vtrue = True
	isa = input("Is there a Acceleration Value? Y/N ")
	if isa.lower () == ("y"):
		a = float(input("Insert Value for A: "))
		atrue = True
	ist = input("Is there a Time Value? Y/N ")
	if ist.lower () == ("y"):
		ttrue = True
		t = float(input("Insert Value for T: "))
if findu == True:
	iss = input("Is there a Displacement Value? Y/N ")
	if iss.lower () == ("y"):
		s = float(input("Insert value for S: "))
		strue = True
	isv = input("Is there a Final Velocity Value? Y/N ")
	if isv.lower () == ("y"):
		v = float(input("Insert value for V: "))
		vtrue = True
	isa = input("Is there a Acceleration Value? Y/N ")
	if isa.lower () == ("y"):
		a = float(input("Insert Value for A: "))
		atrue = True
	ist = input("Is there a Time Value? Y/N ")
	if ist.lower () == ("y"):
		ttrue = True
		t = float(input("Insert Value for T: "))
if findv == True:
	iss = input("Is there a Displacement Value? Y/N ")
	if iss.lower () == ("y"):
		s = float(input("Insert value for S: "))
		strue = True
	isu = input("Is there a Inital Velocity Value? Y/N ")
	if isu.lower () == ("y"):
		u = float(input("Insert value for U: "))
		utrue = True
	isa = input("Is there a Acceleration Value? Y/N ")
	if isa.lower () == ("y"):
		a = float(input("Insert Value for A: "))
		atrue = True
	ist = input("Is there a Time Value? Y/N ")
	if ist.lower () == ("y"):
		ttrue = True
		t = float(input("Insert Value for T: "))
if finda == True:
	iss = input("Is there a Displacement Value? Y/N ")
	if iss.lower () == ("y"):
		s = float(input("Insert value for S: "))
		strue = True
	isu = input("Is there a Inital Velocity Value? Y/N ")
	if isu.lower () == ("y"):
		u = float(input("Insert value for U: "))
		utrue = True
	isv = input("Is there a Final Velocity Value? Y/N ")
	if isv.lower () == ("y"):
		v = float(input("Insert value for V: "))
		vtrue = True
	ist = input("Is there a Time Value? Y/N ")
	if ist.lower () == ("y"):
		ttrue = True
		t = float(input("Insert Value for T: "))
if findt == True:
	iss = input("Is there a Displacement Value? Y/N ")
	if iss.lower () == ("y"):
		s = float(input("Insert value for S: "))
		strue = True
	isu = input("Is there a Inital Velocity Value? Y/N ")
	if isu.lower () == ("y"):
		u = float(input("Insert value for U: "))
		utrue = True
	isv = input("Is there a Final Velocity Value? Y/N ")
	if isv.lower () == ("y"):
		v = float(input("Insert value for V: "))
		vtrue = True
	isa = input("Is there a Acceleration Value? Y/N ")
	if isa.lower () == ("y"):
		a = float(input("Insert Value for A: "))
		atrue = True

if findu == True and atrue == True and vtrue == True and ttrue == True:
	u = v - a*t
	print("u = ",u)
if findv == True and atrue == True and utrue == True and ttrue == True:
	v = u + a*t
	print("v = ",v)
if finda == True and vtrue == True and utrue == True and ttrue == True:
	a = v-u/t
	print("a = ",a)
if findt == True and vtrue == True and utrue == True and atrue == True:
	t = v-u/a
	print("t = ",t)
if finds == True and utrue == True and vtrue == True and ttrue == True:
	s = (u+v/2)*t
	print("s = ",s)
if findu == True and strue == True and vtrue == True and ttrue == True:
	u = 2*s - v *t
	print("u = ",u)
if findv == True and strue == True and utrue == True and ttrue == True:
	v = 2*s/t - u
	print("v = ", v)
if findt == True and strue == True and utrue == True and vtrue == True:
	t = 2*s/u+v
	print("t = ", t)
if finds == True and utrue == True and ttrue == True and atrue == True:
	s = u*t + 0.5*a*t**2
	print("s = ",s)
if findu == True and strue == True and ttrue == True and atrue == True:
	u = s/t-0.5*a*t
	print("u = ", u)
if finda == True and strue == True and utrue == True and ttrue == True:
	a = 2(s-u*t)/(t**2)
	print("a = ",a)
if findt == True and strue == True and utrue == True and atrue == True:
	t = sqrt(s/u+0.5*a)
	print("t = ",t)
if finds == True and utrue == True and vtrue == True and atrue == True:
	s = v**2-u**2/2*a
	print("s = ",s)
if findu == True and strue == True and vtrue == True and atrue == True:
	u = sqrt(v**2-2*a*s)
	print("u = ",u)
if findv == True and strue == True and utrue == True and atrue == True:
	v = sqrt(u**2+2*a*s)
	print("v = ",v)
if finda == True and strue == True and utrue == True and vtrue == True:
	a = v**2-u**2/2*s
	print("a = ",a)
