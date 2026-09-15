from vehiculo import Vehiculo

v1 = Vehiculo("KXPR84", 2019)
v2 = Vehiculo("JKLM12", 2016)

v1.ingresar()

print(v1.patente, v1.en_taller)
print(v2.patente, v2.en_taller)
