# 🕸️ Network Analysis of Quasars — SDSS DR16Q

Este proyecto explora la **estructura topológica en el espacio de parámetros físicos de cuásares** usando técnicas de análisis de redes.  
El objetivo principal es investigar si existen **agrupamientos naturales en el espacio físico de cuásares con \( z < 2.5 \)** y buen SNR.

---

## 📚 Objetivos científicos

- Construir un subconjunto bien definido del catálogo **SDSS DR16Q** (cuásares con \( z < 2.5 \), alto S/N).
- Representar los objetos como nodos de una red basada en similitudes físicas.
- Explorar la estructura topológica de la red:
  - comunidades
  - hubs y nodos puente
  - modularidad y conectividad
- Identificar posibles **subpoblaciones físicas emergentes**.
- Establecer una base metodológica para comparaciones futuras (e.g. clustering clásico vs. redes).

---

## 🧭 Roadmap del proyecto

| Fase | Tarea principal | Estado |
|------|------------------|--------|
| 0. Preparación | Estructura de carpetas + entorno reproducible | ⏳ |
| 1. Preprocesamiento | Limpieza y selección de parámetros físicos | ⏳ |
| 2. Construcción de red | Definición de nodos y aristas (kNN / ε) | ⏳ |
| 3. Análisis topológico | Métricas, comunidades, embeddings | ⏳ |
| 4. Interpretación física | Relación con propiedades astrofísicas | ⏳ |
| 5. Redacción | Paper para envío a MNRAS / A&A / ApJ | ⏳ |

*El objetivo es tener un resultado publicable en un plazo estimado de 4–6 meses.*

---

## 📁 Estructura del repositorio

```
project/
├── data/
│ ├── raw/ # Catálogos originales
│ ├── processed/ # Subconjuntos limpios y normalizados
├── notebooks/ # Exploración y análisis paso a paso
├── scripts/ # Scripts modulares (preprocesamiento, red, métricas)
├── results/
│ ├── figures/ # Visualizaciones de red y embeddings
│ ├── tables/ # Resultados numéricos y estadísticas
├── docs/ # Notas técnicas y documentación adicional
├── paper/ # Manuscrito y figuras finales
├── README.md
└── requirements.txt / environment.yml
```

## 🧰 Stack tecnológico

- **Python** 3.10+
- [pandas](https://pandas.pydata.org/) · [numpy](https://numpy.org/) · [astropy](https://www.astropy.org/)  
- [scikit-learn](https://scikit-learn.org/) — kNN, métricas, embeddings  
- [networkx](https://networkx.org/) o [igraph](https://igraph.org/python/) — análisis de redes  
- [matplotlib](https://matplotlib.org/) / [seaborn](https://seaborn.pydata.org/) — visualización  
- [UMAP](https://umap-learn.readthedocs.io/en/latest/) — reducción de dimensionalidad

---

## 🧪 Flujo de trabajo

1. **Preprocesamiento**: Filtrado por redshift, SNR y limpieza de parámetros.  
2. **Construcción de red**: Definición de nodos (cuásares) y aristas (similitud física).  
3. **Análisis topológico**: Métricas de red, comunidades y estructura global.  
4. **Interpretación física**: Relación entre propiedades astrofísicas y estructura de red.  
5. **Publicación**: Redacción de manuscrito para revista científica.

## 📊 Métricas y análisis planeados

- **Topología global**: grado medio, clustering, modularidad.  
- **Centralidades**: degree, betweenness, closeness.  
- **Comunidades**: algoritmos Louvain / Leiden / Infomap.  
- **Proyecciones**: UMAP, t-SNE, visualizaciones 2D coloreadas por comunidad.  
- **Comparaciones**: distribución de parámetros físicos entre comunidades.

## 📝 Próximos pasos

- [ ] Descargar y limpiar SDSS DR16Q  
- [ ] Definir subconjunto z < 2.5  
- [ ] Implementar red kNN  
- [ ] Calcular métricas de red  
- [ ] Identificar comunidades y hubs  
- [ ] Redactar manuscrito inicial

## 🧑‍💻 Autoría

- **Autor/a:** *Jose Miguel Ramirez*  
- **Institución:** *Universidad De Concepcion*  
- Contacto: *joramriez2020@udec.cl*

## 🪪 Licencia

Este proyecto se distribuye bajo licencia MIT.  
Ver [LICENSE](LICENSE) para más detalles.

##  Contribuciones

¡Pull requests bienvenidas! Si quieres contribuir:
- Abre un *issue* para sugerencias
- Usa *branches* descriptivos
- Documenta claramente tus cambios