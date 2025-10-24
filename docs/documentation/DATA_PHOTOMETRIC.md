# Descripción de los datos fotométricos — Catálogo de cuásares (SDSS DR16Q)

Este documento describe las columnas fotométricas incluidas en el DataFrame `df_phot`, utilizadas para el análisis de cuásares en el marco del **Sloan Digital Sky Survey (SDSS) DR16Q**.  
Los datos abarcan desde el **ultravioleta (UV)** hasta el **infrarrojo medio (MIR)**, integrando información de múltiples misiones astronómicas.

## Información básica de la fuente

| Columna     | Descripción | Unidad | Fuente |
|--------------|-------------|---------|---------|
| `SDSS_NAME` | Nombre del cuásar en el catálogo SDSS | — | [SDSS DR16Q; Lyke et al. 2020](https://doi.org/10.3847/1538-4365/ab5b9d) |
| `RA`, `DEC` | Coordenadas ecuatoriales (J2000) | grados | SDSS DR16Q |
| `Z` | Desplazamiento al rojo espectroscópico | adimensional | SDSS DR16Q |

## Fotometría ultravioleta (GALEX)

| Columna | Banda | Unidad | Sistema | Descripción |
|----------|--------|---------|----------|--------------|
| `FUV` | Far-UV (1528 Å) | nMgy | AB | Flujo FUV de GALEX |
| `NUV` | Near-UV (2271 Å) | nMgy | AB | Flujo NUV de GALEX |

**Referencia:**  
Martin et al. (2005), *The Galaxy Evolution Explorer: A Space Ultraviolet Survey Mission*, ApJ 619, L1.  
[DOI: 10.1086/426387](https://doi.org/10.1086/426387)

## Fotometría óptica (SDSS)

| Columna | Banda | Unidad | Sistema | Descripción |
|----------|--------|---------|----------|--------------|
| `PSFMAG_u`, `PSFMAG_g`, `PSFMAG_r`, `PSFMAG_i`, `PSFMAG_z` | u, g, r, i, z | mag | AB | Magnitudes PSF del SDSS |
| `GAL_EXT_u`, `GAL_EXT_g`, `GAL_EXT_r`, `GAL_EXT_i`, `GAL_EXT_z` | Extinción galáctica | mag | AB | Corrección de extinción en cada banda |

**Referencias:**  
Gunn et al. (1998), *The Sloan Digital Sky Survey Photometric System*, AJ 116, 3040.  
[DOI: 10.1086/300645](https://doi.org/10.1086/300645)  
York et al. (2000), *The Sloan Digital Sky Survey: Technical Summary*, AJ 120, 1579.  
[DOI: 10.1086/301513](https://doi.org/10.1086/301513)

**Notas:**  
- Magnitudes en el sistema **AB**.  
- Las extinciones (`GAL_EXT_*`) se calculan siguiendo *Schlegel, Finkbeiner & Davis (1998)* y la ley de extinción de *Cardelli et al. (1989)*.

## Fotometría en el infrarrojo cercano (2MASS)

| Columna | Banda | Unidad | Sistema | Descripción |
|----------|--------|---------|----------|--------------|
| `JMAG`, `HMAG`, `KMAG` | J, H, Ks | mag | Vega | Magnitudes del 2MASS All-Sky Survey |

**Referencia:**  
Skrutskie et al. (2006), *The Two Micron All Sky Survey (2MASS)*, AJ 131, 1163.  
[DOI: 10.1086/498708](https://doi.org/10.1086/498708)

## Fotometría NIR (UKIDSS)

| Columna | Banda | Unidad | Sistema | Descripción |
|----------|--------|---------|----------|--------------|
| `YFLUX`, `JFLUX`, `HFLUX`, `KFLUX` | Y, J, H, K | W·m⁻²·Hz⁻¹ | — | Densidades de flujo fotométrico de UKIDSS |

**Referencia:**  
Lawrence et al. (2007), *The UKIRT Infrared Deep Sky Survey (UKIDSS)*, MNRAS 379, 1599.  
[DOI: 10.1111/j.1365-2966.2007.12040.x](https://doi.org/10.1111/j.1365-2966.2007.12040.x)

## Fotometría infrarroja media (WISE)

| Columna | Banda | Unidad | Sistema | Descripción |
|----------|--------|---------|----------|--------------|
| `W1_FLUX`, `W2_FLUX` | W1 (3.4 μm), W2 (4.6 μm) | mag | Vega | Magnitudes en el infrarrojo medio (WISE) |

**Referencia:**  
Wright et al. (2010), *The Wide-field Infrared Survey Explorer (WISE): Mission Description and Initial Performance*, AJ 140, 1868.  
[DOI: 10.1088/0004-6256/140/6/1868](https://doi.org/10.1088/0004-6256/140/6/1868)

**Referencias clave**  
- Schlegel, D. J., Finkbeiner, D. P., & Davis, M. (1998). *ApJ, 500, 525.*  
- Schlafly, E. F., & Finkbeiner, D. P. (2011). *ApJ, 737, 103.*  
- Yuan, H. B., Liu, X. W., & Xiang, M. S. (2013). *MNRAS, 430, 2188.*  
- Cardelli, J. A., Clayton, G. C., & Mathis, J. S. (1989). *ApJ, 345, 245.*  
- Vanden Berk, D. E. et al. (2001). *AJ, 122, 549.*  
- Selsing, J. et al. (2016). *A&A, 585, A87.*  
- Hogg, D. W. (2002). *arXiv:astro-ph/9905116.*  

🧠 **Autor:** *Jose Miguel Ramirez*  
📅 **Versión:** 1.1 — Octubre 2025  
📁 **Proyecto:** *Corrección K y análisis fotométrico de cuásares (SDSS DR16Q)*