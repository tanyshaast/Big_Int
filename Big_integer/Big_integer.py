#!/usr/bin/python3.4m
import sys
import Big_integer

error1 = '\nUsage: (python) (file_name) (input_file1) (operand(+,-,\"*\",/,^,%)) (input_file2) (output_file)'
error2= "       \n[-b] [ [-mod module_file_name]]"
error3= "       \n[-b] : Optional key. If set, then data will read from binary files"
error4= "       \n[-mod] (modulus_file_name): Optional key. If set, then \"^\" operation will used with modulus"
error5= "       \n(modulus_file_name) is required parametr, if set key [-mod]\n\n"
x = Big_integer()
y = Big_integer()
z = Big_integer()
if len(sys.argv)==1:
	print(error1)
	print(error2)
	print(error3)
	print(error4)
	print(error5)
	sys.exit(1)
if len(sys.argv) < 4:
	print("Error: so few arguments")
	sys.exit(1)
if len(sys.argv) > 7:
	print("Error: so many arguments")
	sys.exit(1)
if len(sys.argv) == 4:
	x.ReadFromTextFile(sys.argv[0])
	y.ReadFromTextFile(sys.argv[2])
	binaryFlag=false
	moduleFlag=false
if len(sys.argv) == 5 and sys.argv[4]=="-b":
	x.ReadFromBin(sys.argv[0])
	y.ReadFromBin(sys.argv[2])
	binaryFlag = true
	moduleFlag = false
if len(sys.argv) == 5 and sys.argv[4]=="-mod":
	print("Error: Not found module_file_name")
	sys.exit(1)
if len(sys.argv) == 6 and sys.argv[4]=="-mod":
	m = Big_integer()
	m.ReadFromTextFile(sys.argv[5])
	binaryFlag = false
	moduleFlag = true
if len(sys.argv) == 7:
	m = Big_integer()
	x.ReadFromBin(sys.argv[0])
	y.ReadFromBin(sys.argv[2])
	m.ReadFromBin(sys.argv[6])
	binaryFlag=true
	moduleFlag=true
if sys.argv[1]=="+":
	z=x+y
if sys.argv[1]=="-":
	z=x-y
if sys.argv[1]=="*":
	z=x*y
if sys.argv[1]=="/":
	z=x/y
if sys.argv[1]=="^":
	if moduleFlag:
		z=(x^y)%m
	else:
		z=x^y
if sys.argv[1]=="%":
	z=x%y
if binaryFlag:
	z.WriteToBin(sys,argv[3])
else:
	z.WriteToTextFile(sys.argv[3])
