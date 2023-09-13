#Importar librerias
import sys
import time
from heapq import heappop, heappush #Funciones de pilas y colas

#Una clase para almacenar un nodo de heap
class Node:
  def __init__(self,vertex,weight=0):
    self.vertex = vertex
    self.weight = weight
  #Anule la funcion _lt_() para hacer que la clase "Node" funcione con un min-heap
  def __lt__(self, other):
    return self.weight < other.weight
  
#Una clase para representar un objeto graph
class Graph:
  def __init__(self, edge, n):
    #Asigna memoria para la lista de adyacencia
    self.adjList = [[] for _ in range(n)]

    #Agrega bordes al graph dirigido
    for(source, dest, weight) in edges:
      self.adjList[source].append((dest, weight))

def get_route(prev,i,route):
  if i>=0:
    get_route(prev,prev[i],route)
    route.append(i)

#Ejecutar el algoritmo de dijkstra en un graph dado
def findShortestPaths(graph, source, n):
  #Crea un y empuja el nodo de origen con una distancia de 0
  pq = []
  heappush(pq, Node(source))
  #Establece la distancia inicial desde la fuente a 'v' como infinito
  dist = [sys.maxsize] * n
  #Distancia de la fuente a si mismo es cero
  dist[source] = 0
  #Lista # para rastrear vertices para los cuales ya se encontró el costo mínimo
  done = [False] * n
  done[source] = True
  #Almacena el predecesor de un vértice (en una ruta de impresión)
  prev = [-1] *  n
  #Se ejecuta hasta que el grafo esté vacío
  while pq:
    node = heappop(pq)   #Quitar y devolver el mejor vértice
    u = node.vertex      #Obtener el número de vértice

    #Hacer para cada vecino 'v' de 'u'
    for (v, weight) in graph.adjList[u]:
      if not done[v] and (dist[u] + weight) < dist[v]:   #Escalon de relajación
        dist[v] = dist[u] + weight
        prev[v] = u
        heappush(pq, Node(v, dist[v]))

    #Marca el vértice 'u' como hecho para que no se vuelva a recoger
    done[u] = True

  route = []
  for i in range(n):
    if i != source and dist[i] != sys.maxsize:
      get_route(prev, i, route)
      print(f'Path ({source} -> {i}): Minimum cost = {dist[i]}, Route = {route}')
      route.clear()

if __name__ == '__main__':
  start_time = time.time()
  #Inicializar el grafo con el siguiente diagrama
  #(u,v,w) representa la arista del vertice 'u' al vertice 'v' con peso 'w'
  #El siguiente vector representa el grafo
  edges = [
      #(0,1,10),(0,4,3),(1,2,2),(1,4,4),(2,3,9),(2,3,7),(4,1,1),(4,2,8),(4,2,8),
      #(4,3,2)
      (0,2,2),(1,2,5),(2,3,2),(2,4,4),(3,4,1),(4,5,4)
  ]
  #Numero total de nodo en el grafo (etiquetados del 0 al 4)
  n=7
  #Construccion del grafo
  graph = Graph(edges,n)
  #Ejecuta el algoritmo dijkstra desde cada nodo, para hacer la ruta
  for source in range(n):
    findShortestPaths(graph, source, n)
  end_time = time.time()

  # Calcula el tiempo total de ejecución
  execution_time = end_time - start_time

  print(f"Tiempo de ejecución: {execution_time} segundos")