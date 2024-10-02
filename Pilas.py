import matplotlib.pyplot as plt
from collections import deque

class PilaConGrafico:
    def __init__(self):
        self.pila = deque()

    # Método para añadir un elemento a la pila (push) y visualizarlo
    def apilar(self, elemento):
        self.pila.append(elemento)
        self.mostrar_pila("Apilar: " + str(elemento))

    # Método para quitar el último elemento de la pila (pop) y visualizarlo
    def desapilar(self):
        if not self.esta_vacia():
            elemento = self.pila.pop()
            self.mostrar_pila("Desapilar: " + str(elemento))
            return elemento
        else:
            print("La pila está vacía")
            return None

    # Método para ver el último elemento de la pila sin quitarlo (peek)
    def ver_cima(self):
        if not self.esta_vacia():
            return self.pila[-1]
        else:
            return None

    # Método para comprobar si la pila está vacía
    def esta_vacia(self):
        return len(self.pila) == 0

    # Método para visualizar la pila con gráficos
    def mostrar_pila(self, operacion):
        plt.figure(figsize=(5, 6))
        plt.bar(range(len(self.pila)), self.pila, color='lightblue')
        plt.xticks(range(len(self.pila)), [f"Elemento {i+1}" for i in range(len(self.pila))])
        plt.title(operacion)
        plt.xlabel("Posición en la pila")
        plt.ylabel("Valor")
        plt.ylim(0, max(self.pila) + 1 if self.pila else 1)
        plt.show()
mi_pila_grafica = PilaConGrafico()
mi_pila_grafica.apilar(5)  # Añadimos 5 a la pila
mi_pila_grafica.apilar(10) # Añadimos 10 a la pila
mi_pila_grafica.apilar(15) # Añadimos 15 a la pila

mi_pila_grafica.desapilar() # Quitamos el último elemento
mi_pila_grafica.apilar(20)  # Añadimos 20 a la pila
