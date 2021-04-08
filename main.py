from VNH5019 import VNH5019

motor_1 = VNH5019(0, 1, 2, True)
motor_2 = VNH5019(3, 4, 5, False)

print(motor_1.cs_read())
