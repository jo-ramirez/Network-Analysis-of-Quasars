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
    spec_header, spec_data = open_fits("data/raw/dr16q_prop_May01_2024.fits.gz")

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

        # 2MASS (NIR) - Corregido a mayúsculas
        "2j_mag": np.array(phot_data["Jmag"]),   # mag (Vega)
        "2h_mag": np.array(phot_data["Hmag"]),   # mag (Vega)
        "2k_mag": np.array(phot_data["Kmag"]),   # mag (Vega)

        # WISE (IR medio) 
        "W1_mag": np.array(phot_data["W1mag"]),  # flujo (309.05nJy)
        "W2_mag": np.array(phot_data["W2mag"]),  # flujo (167.66nJy)

        # Calidad de la medicion
        "SN": np.array(phot_data["SNR"])
    })

    df_spec = pd.DataFrame({
        "SDSS_NAME": spec_data["SDSS_NAME"],

        "FEII_OPT_EW":  spec_data["FEII_OPT_EW"],

        "HALPHA_BR_FWHM": spec_data["HALPHA_BR"][:, 4],
        "HALPHA_BR_EW": spec_data["HALPHA_BR"][:, 5],

        "HBETA_BR_FWHM": spec_data["HBETA_BR"][:, 4],
        "HBETA_BR_EW": spec_data["HBETA_BR"][:, 5],
        
        "OIII5007_FWHM": spec_data["OIII5007"][:, 4],
        "OIII5007_EW": spec_data["OIII5007"][:, 5],

        "NII6585_FWHM": spec_data["NII6585"][:, 4],
        "NII6585_EW": spec_data["NII6585"][:, 5],

        "SII6718_FWHM": spec_data["SII6718"][:, 4],
        "SII6718_EW": spec_data["SII6718"][:, 5],

        "MGII_BR_EW": spec_data["MGII_BR"][:, 5],
        "MGII_BR_FWHM": spec_data["MGII_BR"][:, 4],

        "CIV_EW": spec_data["CIV"][:, 5],
        "CIV_FWHM": spec_data["CIV"][:, 4],

        "LOGMBH": spec_data["LOGMBH"],
        "LOGLBOL": spec_data["LOGLBOL"],
        "LOGLEDD_RATIO": spec_data["LOGLEDD_RATIO"]
    })

    df_phot = convert_to_little_endian(df_phot).dropna()
    df_spec = convert_to_little_endian(df_spec).dropna()

    df_phot.to_csv("data/pre_processed/SDSS_DR16Q_phot.csv", index=False)
    df_spec.to_csv("data/pre_processed/SDSS_DR16Q_spec.csv", index=False)