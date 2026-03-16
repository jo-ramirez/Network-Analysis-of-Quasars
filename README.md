# Topología del Espacio Latente Fotométrico: Taxonomía No Supervisada de Cuásares

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-research-blueviolet)

## 📖 Abstract / Descripción

Este proyecto presenta un pipeline de Machine Learning **completamente no supervisado** diseñado para el análisis topológico y la clasificación taxonómica de Cuásares (Núcleos Galácticos Activos - AGNs). Utilizando **exclusivamente datos fotométricos**, este repositorio demuestra que es posible redescubrir la taxonomía compleja de los AGNs (Radio-loud, Type 2, Red Quasars) y aislar poblaciones anómalas (como *Broad Absorption Line* o *Changing-State AGNs*).

A través del mapeo topológico y del espacio latente de sus colores fotométricos, el proyecto prescinde por completo de la necesidad de espectroscopía previa o etiquetas de entrenamiento, revelando eficazmente la estructura subyacente de la población de cuásares a partir del *manifold* de sus observaciones en múltiples bandas.

---

## ⚙️ Arquitectura del Pipeline

El ciclo de vida del análisis se articula en tres etapas fundamentales:

### 1. Preprocesamiento Físico
- **K-Correction:** Cálculo de magnitudes absolutas aplicando una corrección basada en la interpolación de un espectro template al *rest-frame*. Esto resulta crucial para lidiar de forma robusta con la amplia dispersión temporal y de corrimiento al rojo (redshift, $z$).
- **Imputación Inteligente:** Manejo físico-matemático de flujos fotométricos negativos o nulos para prevenir sesgos de supervivencia (*survival bias*), lo que de otra manera penalizaría enormemente y descartaría a las poblaciones originadas bajo fuerte oscurecimiento intrínseco.
- **Transformación de Dimensionalidad:** Construcción del espacio original de características basado en índices de color.

### 2. Modelado Topológico
- **Reducción de Dimensionalidad (UMAP):** Proyección matemática utilizando el algoritmo *Uniform Manifold Approximation and Projection*. Se calibró específicamente con la métrica de Manhattan ($L_1$), confiriendo al modelo una **alta robustez estructural frente a outliers astrofísicos** extremos que abundan en los catálogos observacionales.

### 3. Aprendizaje sobre Grafos (*Graph Learning*)
- **Construcción del Grafo:** Formulación de un grafo de similitud k-NN, finamente ponderado mediante un Heat Kernel (Gaussiano) que promueve transiciones analíticas suaves en todo el manifold fotométrico.
- **Clustering Topológico:** Implementación del Algoritmo de Leiden optimizado (a resolución topológica $r = 0.2$), estabilizando el tejido de datos subyacente.

---

## 🔬 Hallazgos y Resultados de Validación

El modelo detectó convergencia estructural en **6 meso-estructuras estables** de la población astrofísica (con un global *Silhouette Score* $\approx 0.35$). Para comprobar su veracidad física, el particionado fue expuesto a un riguroso esquema de validación cruzada utilizando datos externos (emisión en radio, espectroscopía subyacente) provenientes del **catálogo SDSS DR16Q** (ej: contrastes con indicadores como `F1_4p`, `Chi2CIV`, `Chi2MgII`).

El Pipeline no supervisado identificó con éxito:

- **La Población Jet-Dominated:** Agrupó exitosamente a casi la totalidad de Blázares / FSRQs cuyas propiedades fotométricas estaban intrínsecamente dominadas por la potente emisión del jet no térmico.
- **Oscurecidos & Red Quasars:** Aislamiento sin precedentes de la población atípica severamente afectada por extinción de las bandas ópticas y enrojecida debido a un exceso marcado de emisión térmica infrarroja (IR).
- **Poblaciones de Cinemática Extrema:** Las comunidades lograron perfilar sub-poblaciones marginales compuestas por flujos absortivos masivos (como los Cuásares BAL), diagnosticadas empíricamente en el espacio no-supervisado como fallos catastróficos en correlaciones estelares estándar de ajustes.

---

## 📁 Estructura del Proyecto

```text
Network-Analysis-of-Quasars/
├── data/                  # Datasets fotométricos, metadata y catálogos (SDSS DR16Q)
├── docs/                  # Documentación teórica, diagramas y artículos de referencia
├── notebooks/             # Workspace iterativo para EDA y modelamiento
│   ├── photometric_cleaning.ipynb # Preprocesamiento físico (K-correction, imputación)
│   └── topological_analysis.ipynb # Grafo k-NN, UMAP y Algoritmo de Leiden
├── results/               # Salidas de clusters, métricas, gráficas y embeddings
├── scripts/               # Scripts de ejecución modularizada
│   └── data_merge.py      # Cruce posicional de tablas fotométricas/espectroscópicas
├── venv/                  # Entorno virtual local (ignorado en git)
├── requirements.txt       # Control de dependencias de Python
└── README.md              # Este archivo
```

---

## 🛠️ Instalación y Requisitos

Para replicar el entorno de ejecución aislando los paquetes de análisis (como `umap-learn`, `igraph`, `leidenalg`, `astropy`, etc.):

```bash
# 1. Clonar este repositorio
git clone https://github.com/tu-usuario/Network-Analysis-of-Quasars.git
cd Network-Analysis-of-Quasars

# 2. Crear y activar tu entorno virtual
python -m venv venv

# En Linux o macOS:
source venv/bin/activate
# En Windows:
venv\Scripts\activate

# 3. Instalar las dependencias exactas del proyecto
pip install -r requirements.txt
```
