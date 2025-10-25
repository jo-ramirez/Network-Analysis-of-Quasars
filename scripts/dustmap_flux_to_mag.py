import numpy as np
from astropy.io import fits

FITS_PATH   = "data/dustmaps/COM_CompMap_Dust-GNILC-Model-Opacity_2048_R2.01.fits"
OUTPUT_PATH = "data/dustmaps/final_dustmap_ebv.fits"

FIELD = 'TAU353'
K_TAU = 14900.0

with fits.open(FITS_PATH) as hdul:
    dustmap_header = hdul[1].header
    dustmap_data   = hdul[1].data

ebv = dustmap_data[FIELD] * K_TAU
ebv = np.clip(ebv, 0.0, None).astype(np.float32)

new_header = dustmap_header.copy()
new_header["COMMENT"] = "E(B-V) dust map derived from Planck GNILC TAU353"
new_header["BUNIT"]   = "mag"
new_header["K_TAU"]   = (K_TAU, "Conversion factor from tau353 to E(B-V)")

hdu = fits.PrimaryHDU(data=ebv, header=new_header)
hdulist = fits.HDUList([hdu])
hdulist.writeto(OUTPUT_PATH, overwrite=True)

print(f"Mapa corregido guardado en: {OUTPUT_PATH}")