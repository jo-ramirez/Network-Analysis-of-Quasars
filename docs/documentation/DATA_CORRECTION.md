# 📘 Descripción de la corrección de datos fotométricos — Catálogo de cuásares (SDSS DR16Q)

Este documento describe el proceso de **corrección y homogenización fotométrica** aplicado al catálogo de cuásares **SDSS DR16Q**, para convertir todas las observaciones en **magnitudes absolutas AB** en el rango **UV–MIR**.  

Estas correcciones son necesarias para comparar objetos a distintos desplazamientos al rojo y construir un **grafo de similitud** basado en sus propiedades intrínsecas (rest–frame).

## Conversión general a magnitudes absolutas

El flujo de corrección por objeto y por banda \(X\) es:

$$
  \boxed{M_X = m_{X,\mathrm{AB}} - A_X - \mu(z) - K_X(z)}
$$

donde:
- $m_{X,\mathrm{AB}}$: magnitud **AB observada**, tras convertir desde Vega o flujo físico.  
- $A_X$: extinción galáctica en la banda \(X\).  
- $\mu(z)$: módulo de distancia.  
- $K_X(z)$: corrección K para redshift \(z\).

> **Convención AB:**  
> $$
>   m_{\mathrm{AB}} = -2.5\,\log_{10}\!\left(\frac{f_\nu}{3631\,\mathrm{Jy}}\right)
> $$
> *(Oke & Gunn 1983, ApJ 266, 713).*

---

## 1. Extinción galáctica

La luz de cada cuásar se atenúa por el polvo interestelar en la Vía Láctea.  
La magnitud corregida se obtiene como:

$$
  m'_{X} = m_{X} - A_X
$$

donde $A_X = R_X \, E(B-V)$.

- **Mapa de polvo usado:**  
  *SFD98* (Schlegel, Finkbeiner & Davis 1998, ApJ 500, 525)  
  implementado mediante [`dustmaps.sfd`](https://github.com/gregreen/dustmaps).  
- **Recalibración:**  
  Coeficientes $R_X = A_\lambda / E(B-V)$ de *Schlafly & Finkbeiner (2011, ApJ 737, 103)*.  
- **Ampliación UV/MIR:**  
  Para GALEX y WISE se emplean valores de *Yuan, Liu & Xiang (2013, MNRAS 430, 2188)*.


> En el rango óptico y NIR se adopta la ley de extinción de *Cardelli, Clayton & Mathis (1989, ApJ 345, 245)* con $R_V = 3.1$.

## 2. Unificación de sistemas fotométricos a **AB**

Los diferentes catálogos usan sistemas de magnitudes distintos.  
Todos se convierten a **AB** antes de aplicar la corrección K.

### 2.1 GALEX (FUV, NUV en *nMgy*)

Las columnas `FUV`, `NUV` vienen en **nanomaggies**, ya en el sistema AB:

$$
  m_{\mathrm{AB}} = 22.5 - 2.5\,\log_{10}(\mathrm{nMgy})
$$

*(GALEX — Martin et al. 2005, ApJ 619, L1).*

### 2.2 SDSS (u, g, r, i, z)

Las columnas `PSFMAG_*` del SDSS ya están en el sistema **AB**.  
Solo se aplica la extinción:

$$
  m_{X,\mathrm{AB}} = m_{X} - A_X
$$

*(SDSS — Gunn et al. 1998, AJ 116, 3040).*

### 2.3 2MASS (J, H, K en *Vega*)

Conversión a AB mediante offsets promedio:

$$
\begin{aligned}
  J_{\mathrm{AB}} &= J_{\mathrm{Vega}} + 0.894 \\
  H_{\mathrm{AB}} &= H_{\mathrm{Vega}} + 1.374 \\
  K_{\mathrm{AB}} &= K_{\mathrm{Vega}} + 1.840
\end{aligned}
$$

*(Skrutskie et al. 2006, AJ 131, 1163).*

Luego se corrige por extinción galáctica:  
$m'_{X} = m_{X,\; \mathrm{AB}} - A_X$.

### 2.4 UKIDSS (Y, J, H, K en *densidad de flujo*)

1. Convertir flujo a Jy:  
   $$
    f_\nu[\mathrm{Jy}] = f_\nu[W\,m^{-2}\,Hz^{-1}] \times 10^{26}
   $$
2. Pasar a magnitud AB:  
   $$
    m_{\mathrm{AB}} = -2.5\,\log_{10}\!\left(\frac{f_\nu[\mathrm{Jy}]}{3631}\right)
   $$
3. Restar la extinción $A_X$ correspondiente.

*(Lawrence et al. 2007, MNRAS 379, 1599).*

### 2.5 WISE (W1, W2 en *Vega*)

Offsets de conversión a AB:

$$
  \begin{aligned}
    W1_{\mathrm{AB}} &= W1_{\mathrm{Vega}} + 2.699 \\
    W2_{\mathrm{AB}} &= W2_{\mathrm{Vega}} + 3.339
  \end{aligned}
$$

*(Wright et al. 2010, AJ 140, 1868).*

La extinción en el IR medio es generalmente pequeña,  
pero se puede aplicar $A_{W1}, A_{W2}$ de Yuan et al. (2013).

> **Resultado:** todos los valores fotométricos están en el sistema **AB**, corregidos por extinción.

## 3️⃣ Módulo de distancia $\mu(z)$

La relación entre magnitud aparente y absoluta depende del módulo de distancia:

$$
  \mu(z) = 5\,\log_{10}\!\left(\frac{D_L(z)}{10\,\mathrm{pc}}\right)
$$

El **luminosity distance** $D_L$ para una cosmología plana ΛCDM es:

$$
D_L(z) = (1+z)\,\frac{c}{H_0}\int_0^z \frac{dz'}{\sqrt{\Omega_m(1+z')^3 + \Omega_\Lambda}}
$$

Adoptamos los parámetros cosmológicos:

$$
H_0 = 70\,\mathrm{km\,s^{-1}\,Mpc^{-1}},\quad \Omega_m = 0.3,\quad \Omega_\Lambda = 0.7
$$

*(Planck Collaboration 2018, A&A 641, A6).*

## 4️⃣ K–correcciones $K_X(z)$

La K–corrección transforma la magnitud observada en la banda $X$
al valor equivalente que tendría si el objeto estuviera en reposo ($z=0$).

### 4.1 Aproximación de ley de potencias (rápida)

Si el espectro del cuásar se aproxima como $f_\nu \propto \nu^{\alpha}$,  
la K–corrección en el sistema AB es:

$$
  \boxed{K_X(z) \approx -2.5(1+\alpha)\,\log_{10}(1+z)}
$$

Valores típicos para cuásares:  
$\alpha \in [-0.7, -0.3]$ (Vanden Berk et al. 2001; Selsing et al. 2016).

> Esta aproximación es útil cuando no se dispone de una SED completa  
> o cuando las bandas cubren regiones similares en el marco rest–frame.


### 4.2 Definición espectral (precisa)

Para una banda $X$ con respuesta $R_X(\nu)$ y SED $f_\nu(\nu)$:

$$
  K_X(z) = -2.5\,\log_{10}\left[(1+z) \,\frac{\int f_\nu((1+z)\nu)\,R_X(\nu)\,d\nu}{\int f_\nu(\nu)\,R_X(\nu)\,d\nu}\right]
$$

(Equivalente en longitud de onda si se usa $R_X(\lambda)$).  

Se recomienda utilizar una **SED compuesta de cuásar** como referencia:
- *Vanden Berk et al. 2001, AJ 122, 549* — SED óptico-UV de SDSS.  
- *Selsing et al. 2016, A&A 585, A87* — SED extendida UV–MIR.  

Puede combinarse con una extrapolación por **ley de potencias** en las zonas donde el template no cubre el rango del filtro (por ejemplo, en WISE).

## 📚 Referencias

- Schlegel, D. J., Finkbeiner, D. P., & Davis, M. (1998). *Maps of Dust Infrared Emission for Use in Estimation of Reddening and Cosmic Microwave Background Radiation Foregrounds*. **ApJ, 500, 525.** DOI: [10.1086/305772](https://doi.org/10.1086/305772)  
- Schlafly, E. F., & Finkbeiner, D. P. (2011). *Measuring Reddening with Sloan Digital Sky Survey Stellar Spectra and Recalibrating SFD*. **ApJ, 737, 103.**  
- Yuan, H. B., Liu, X. W., & Xiang, M. S. (2013). *Empirical extinction coefficients for 2MASS, WISE, and GALEX bands*. **MNRAS, 430, 2188.**  
- Cardelli, J. A., Clayton, G. C., & Mathis, J. S. (1989). *The Relationship between Infrared, Optical, and Ultraviolet Extinction*. **ApJ, 345, 245.**  
- Vanden Berk, D. E. et al. (2001). *Composite Quasar Spectra from the SDSS*. **AJ, 122, 549.**  
- Selsing, J. et al. (2016). *An Empirical Extended QSO Template from UV to MIR*. **A&A, 585, A87.**  
- Hogg, D. W. (2002). *K Corrections and Filter Transformations in Astronomy*. [arXiv:astro-ph/9905116](https://arxiv.org/abs/astro-ph/9905116).  
- Planck Collaboration. (2018). *Planck 2018 Results. VI. Cosmological Parameters.* **A&A, 641, A6.**

🧠 **Autor:** *Jose Miguel Ramirez*  
📅 **Versión:** 1.1 — Octubre 2025  
📁 **Proyecto:** *Corrección K y grafo de similitud de cuásares (SDSS DR16Q)*
