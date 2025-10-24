import numpy as np
import matplotlib.pyplot as plt

from astropy.io import fits

from scipy.optimize import curve_fit

def open_filter(filepath):
    data = np.loadtxt(filepath)
    return data[:, 0], data[:, 1]

def power_law_lambda(lam, A, alpha, C, lam0):
    x = lam / lam0
    return A * np.power(x, -alpha) + C

def mask_bad_ranges(lam, ranges):
    bad = np.zeros_like(lam, dtype=bool)
    for _min, _max in ranges:
        bad |= (lam >= _min) & (lam <= _max)
    return bad

MIN_LAM_TARGET = 900.0      # ~ UV (FUV/NUV)
MAX_LAM_TARGET = 60000.0    # ~ 6 micras (cubre WISE W1/W2)

PROBLEMATIC_RANGES = [
    (0.0,     2000.0),
    (4900.0,  5200.0),
    (5400.0,  5600.0),
    (6000.0,  6400.0),
    (8000.0,  8450.0),
]

OUTPUT_PATH = "data/templates/template_extendido.dat"

if __name__ == "__main__":
    with fits.open("./data/templates/optical_nir_qso_sed_001.fits") as hdul:
        lam = np.asarray(hdul[1].data["WAVELENGTH"], dtype=float)
        flx = np.asarray(hdul[1].data["FLUX"],       dtype=float)

    # Ordena por longitud de onda por si viene desordenado
    order = np.argsort(lam)
    lam, flx = lam[order], flx[order]

    # Enmascarado de rangos problemáticos y valores no finitos/no positivos
    bad_ranges = mask_bad_ranges(lam, PROBLEMATIC_RANGES)
    finite = np.isfinite(lam) & np.isfinite(flx)
    positive = flx > 0   # evita que un offset negativo "arregle" problemas de signo
    good = (~bad_ranges) & finite & positive

    lam_good = lam[good]
    flx_good = flx[good]

    # Pivote en el centro del rango bueno para reducir covarianza
    lam0 = np.median(lam_good)

    # Ajuste
    popt, pcov = curve_fit(
        lambda L, A, alpha, C: power_law_lambda(L, A, alpha, C, lam0),
        lam_good, flx_good
    )
    A_fit, alpha_fit, C_fit = popt

    # Paso típico para la grilla extendida (usa la mediana del spacing original)
    dl = np.median(np.diff(lam))

    # Grillas extendidas (azul y rojo)
    lam_lo = np.arange(MIN_LAM_TARGET, max(lam.min() - dl, MIN_LAM_TARGET), dl)
    lam_hi = np.arange(lam.max() + dl, min(MAX_LAM_TARGET + dl, 10*MAX_LAM_TARGET), dl)

    # Evita intervalos vacíos
    lam_lo = lam_lo[lam_lo < lam.min()]
    lam_hi = lam_hi[lam_hi > lam.max()]

    flx_lo = power_law_lambda(lam_lo, A_fit, alpha_fit, C_fit, lam0) if lam_lo.size else np.array([])
    flx_hi = power_law_lambda(lam_hi, A_fit, alpha_fit, C_fit, lam0) if lam_hi.size else np.array([])

    # Construye el espectro total extendido
    full_lam = np.concatenate([lam_lo, lam, lam_hi])
    full_flx = np.concatenate([flx_lo, flx, flx_hi])

    # Guarda a CSV (con cabecera y precisión razonable)
    header = (
        "# Template extendido con power-law (f_lambda = A * (lam/lam0)^(-alpha) + C)\n"
        f"# A = {A_fit:.6e}, alpha = {alpha_fit:.6f}, C = {C_fit:.6e}, lam0 = {lam0:.1f} Angstrom\n"
        "# columns: lambda_Angstrom, f_lambda\n"
    )
    np.savetxt(
        OUTPUT_PATH,
        np.column_stack((full_lam, full_flx)),
        delimiter=",",
        header=header,
        comments="",
        fmt="%.6f,%.6e"
    )

    print(f"Guardado: {OUTPUT_PATH}")
    print(f"Parámetros: A={A_fit:.6e}, alpha={alpha_fit:.4f}, C={C_fit:.6e}, lam0={lam0:.1f} Å")

    plt.plot(full_lam, full_flx)
    plt.show()