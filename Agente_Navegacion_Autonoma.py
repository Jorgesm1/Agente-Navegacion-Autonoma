import heapq
import time

# Definir el entorno (laberinto)
class Laberinto:
    def __init__(self, tamano, paredes, meta):
        self.tamano = tamano
        self.paredes = paredes
        self.meta = meta

    def es_pared(self, x, y):
        return (x, y) in self.paredes

    def mostrar(self, agente, camino):
        for y in range(self.tamano):
            for x in range(self.tamano):
                if (x, y) == (agente.x, agente.y):
                    print("A", end=" ")
                elif (x, y) == self.meta:
                    print("G", end=" ")
                elif (x, y) in self.paredes:
                    print("#", end=" ")
                elif (x, y) in camino:
                    print("*", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()

# Definir el agente de navegación
class Agente:
    def __init__(self, laberinto, x, y):
        self.laberinto = laberinto
        self.x = x
        self.y = y

    def encontrar_camino(self):
        movimientos = [(0, -1), (0, 1), (1, 0), (-1, 0)]  # Norte, Sur, Este, Oeste
        heap = [(0, self.x, self.y, [])]  # (costo, x, y, camino)
        visitados = set()

        while heap:
            costo, x, y, camino = heapq.heappop(heap)
            if (x, y) == self.laberinto.meta:
                return camino + [(x, y)]
            if (x, y) in visitados:
                continue
            visitados.add((x, y))
            for dx, dy in movimientos:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.laberinto.tamano and 0 <= ny < self.laberinto.tamano:
                    if not self.laberinto.es_pared(nx, ny):
                        heapq.heappush(heap, (costo + 1, nx, ny, camino + [(x, y)]))
        return []

# Configurar el laberinto y ejecutar el agente
def main():
    tamano = 5
    paredes = {(1, 1), (1, 2), (3, 3), (2, 3)}
    meta = (4, 4)
    laberinto = Laberinto(tamano, paredes, meta)
    agente = Agente(laberinto, 0, 0)
    
    camino = agente.encontrar_camino()
    for posicion in camino:
        agente.x, agente.y = posicion
        laberinto.mostrar(agente, camino)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
