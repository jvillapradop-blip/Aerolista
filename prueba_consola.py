from lista_pasajeros import ListaPasajeros
from pasajero import Pasajero

lista = ListaPasajeros()
lista.ingresar(Pasajero(1005, "Diana", "0923456789", 22, "3C"))
lista.ingresar(Pasajero(1002, "Ana", "0912345678", 28, "1A"))
lista.ingresar(Pasajero(1009, "Luis", "0945678901", 35, "7D"))
lista.ingresar(Pasajero(1004, "Beto", "0934567890", 16, "7E"))

print("Lista vacia:", lista.esta_vacia())
print("Longitud:", lista.longitud())
print("Listado completo:")
for pasajero in lista.listar():
    print(" ", pasajero)

print("Buscar 1009:", lista.buscar(1009))
print("Buscar 9999:", lista.buscar(9999))
print("Buscar asiento 1A:", lista.buscar_por_asiento("1A"))
print("Buscar cedula 0934567890:", lista.buscar_por_cedula("0934567890"))

modificado = lista.modificar(1009, "Luis A.", 36, "11A")
print("Modificar 1009:", modificado)
print("Despues de modificar:", lista.buscar(1009))

eliminado = lista.eliminar(1005)
print("Eliminado 1005:", eliminado)
print("Nueva longitud:", lista.longitud())

print("Clase Ejecutiva:")
for pasajero in lista.filtrar_por_clase("Ejecutiva"):
    print(" ", pasajero)
