
class Nodo:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        # Punto 17: agregar un nodo al final
        nuevo = Nodo(codigo, descripcion)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza

        while actual is not None:
            print(actual.codigo, actual.descripcion)
            actual = actual.siguiente


class Pila:
    def __init__(self):
        self.items = []

    # Reto individual: comprobar si la pila está vacía
    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        # Punto 18: agregar un elemento a la cima
        self.items.append(elemento)

    def desapilar(self):
        # Retirar y devolver el último elemento
        if len(self.items) == 0:
            return None

        return self.items.pop()


class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        # Punto 19: agregar un elemento al final
        self.items.append(elemento)

    def desencolar(self):
        # Retirar y devolver el primer elemento
        if len(self.items) == 0:
            return None

        return self.items.pop(0)


# ==========================================
# PRUEBAS
# ==========================================

# Punto 17:
print("===== LISTA ENLAZADA =====")

lista = ListaEnlazada()

lista.agregar("M01", "Agua")
lista.agregar("M02", "Suelo")
lista.agregar("M03", "Aire")

lista.mostrar()


# Punto 18
print("\n===== PILA =====")

pila = Pila()

print("¿La pila está vacía?", pila.esta_vacia())

pila.apilar("M01: Agua")
pila.apilar("M02: Suelo")
pila.apilar("M03: Aire")

print("¿La pila está vacía?", pila.esta_vacia())

print("Elemento retirado:", pila.desapilar())
print("Elemento retirado:", pila.desapilar())
print("Elemento retirado:", pila.desapilar())

print("¿La pila está vacía?", pila.esta_vacia())


# Punto 19: cola
print("\n===== COLA =====")

cola = Cola()

cola.encolar("M01: Agua")
cola.encolar("M02: Suelo")
cola.encolar("M03: Aire")

print("Elemento retirado:", cola.desencolar())
print("Elemento retirado:", cola.desencolar())
print("Elemento retirado:", cola.desencolar())

print("Cola vacía:", cola.desencolar())
