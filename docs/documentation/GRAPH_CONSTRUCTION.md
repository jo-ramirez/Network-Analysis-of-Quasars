# Descripción de la construcción del grafo

## Definición del grafo

El grafo se define como un grafo no dirigido y no pesado, donde cada nodo representa un cuásar y cada arista representa una conexión entre dos cuásares.

Denotado por el triplete (V, E, w), donde V es el conjunto de nodos, E es el conjunto de aristas y w es la función de peso.

- Vertices y aristas: Sea $V = \{v_1, v_2, ..., v_n\}$ el conjunto de vertices (Nuestras AGNs)y $E \subset \{(i, j): i, j \in V ,  i \neq j\}$ el conjunto de aristas.
- Funcion de peso: Sea $w: E \rightarrow \mathbb{R+}$ la funcion de peso que asigna un valor real a cada arista.

Una vez con el grafo definido es importante calcular la matriz de adyacencia $A$ y la matriz de distancias $D$.

- Matriz de adyacencia: Sea $A \in \mathbb{R}^{n \times n}$ la matriz de adyacencia, donde $A_{ij} = w(i, j)$ si $(i, j) \in E$ y $A_{ij} = 0$ en caso de que $(i, j) \not\in E$.
- Matriz de distancias: Sea $D \in \mathbb{R}^{n \times n}$ la matriz de distancias, donde $D_{ij} = w(i, j)$ si $(i, j) \in E$ y $D_{ij} = \infty$ en caso de que $(i, j) \not\in E$.

Ademas podemos calcular el grado de cada vertice $i$ como:

$$
deg_i = \sum_{j=1}^{n} w(i, j)
$$

## Construcción del grafo

