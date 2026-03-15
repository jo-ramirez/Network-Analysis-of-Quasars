import pandas as pd
import numpy  as np

from astropy.io import fits
from astropy    import units

def open_fits (filepath:str) -> list:
    with fits.open(filepath) as hdul:
        header = hdul[1].header
        data   = hdul[1].data
    return header, data

def convert_to_little_endian(df):
    for col in df.columns:
        arr = np.array(df[col])
        if hasattr(arr.dtype, "byteorder") and arr.dtype.byteorder == '>':
            df[col] = arr.byteswap().view(arr.dtype.newbyteorder('<'))
    return df

if __name__ == "__main__":
    # Abrimos los .fits
    phot_header, phot_data = open_fits("data/raw/DR16Q_v4.fits")

    # Generamos nuestros dataframes
    df_phot = pd.DataFrame({
        "SDSS_NAME": phot_data["SDSS"],

        # ESPACIO
        "RA" : phot_data["RAJ2000"],             # deg (J2000)
        "DEC": phot_data["DEJ2000"],             # deg (J2000)
        "Z"  : phot_data["z"],                   # adimensional

        # GALEX (UV)
        "FUV_flux": np.array(phot_data["FFUV"]), # nMgy
        "NUV_flux": np.array(phot_data["FNUV"]), # nMgy

        # SDSS (óptico) 
        "u_mag": np.array(phot_data["umag"]),   # mag (AB)
        "g_mag": np.array(phot_data["gmag"]),   # mag (AB)
        "r_mag": np.array(phot_data["rmag"]),   # mag (AB)
        "i_mag": np.array(phot_data["imag"]),   # mag (AB)
        "z_mag": np.array(phot_data["zmag"]),   # mag (AB)

        # 2MASS (NIR) 
        "2j_mag": np.array(phot_data["jmag"]),   # mag (Vega)
        "2h_mag": np.array(phot_data["hmag"]),   # mag (Vega)
        "2k_mag": np.array(phot_data["kmag"]),   # mag (Vega)

        # flujos YJHK
        "UY_FLUX": np.array(phot_data["FY"]),    # densidad de flujo (W m^-2 Hz^-1)
        "UJ_FLUX": np.array(phot_data["FJ"]),    # densidad de flujo (W m^-2 Hz^-1)
        "UH_FLUX": np.array(phot_data["FH"]),    # densidad de flujo (W m^-2 Hz^-1)
        "UK_FLUX": np.array(phot_data["FK"]),    # densidad de flujo (W m^-2 Hz^-1)

        # WISE (IR medio) 
        "W1_mag": np.array(phot_data["W1mag"]),  # flujo (309.05nJy)
        "W2_mag": np.array(phot_data["W2mag"]),  # flujo (167.66nJy)

        # Calidad de la medicion
        "SN": np.array(phot_data["SNR"])
    })

    df_phot = convert_to_little_endian(df_phot).dropna()
    df_phot.to_csv("data/pre_processed/SDSS_DR16Q_phot.csv", index=False)
