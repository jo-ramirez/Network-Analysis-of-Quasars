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
    spec_header, spec_data = open_fits("data/raw/dr14q_spec_prop.fits")

    # Generamos nuestros dataframes
    df_phot = pd.DataFrame({
        "SDSS_NAME": phot_data["SDSS_NAME"],

        # ESPACIO
        "RA" : phot_data["RA"],                                 # deg (J2000)
        "DEC": phot_data["DEC"],                                # deg (J2000)
        "Z"  : phot_data["Z"],                                  # adimensional

        # GALEX (UV)
        "FUV": np.array(phot_data["FUV"]),                      # nMgy
        "NUV": np.array(phot_data["NUV"]),                      # nMgy

        # SDSS (óptico) 
        "PSFMAG_u": np.array(phot_data["PSFMAG"])[:, 0],        # mag (AB)
        "PSFMAG_g": np.array(phot_data["PSFMAG"])[:, 1],        # mag (AB)
        "PSFMAG_r": np.array(phot_data["PSFMAG"])[:, 2],        # mag (AB)
        "PSFMAG_i": np.array(phot_data["PSFMAG"])[:, 3],        # mag (AB)
        "PSFMAG_z": np.array(phot_data["PSFMAG"])[:, 4],        # mag (AB)

        "GAL_EXT_u": np.array(phot_data["EXTINCTION"])[:, 0],   # mag(AB)
        "GAL_EXT_g": np.array(phot_data["EXTINCTION"])[:, 1],   # mag(AB)
        "GAL_EXT_r": np.array(phot_data["EXTINCTION"])[:, 2],   # mag(AB)
        "GAL_EXT_i": np.array(phot_data["EXTINCTION"])[:, 3],   # mag(AB)
        "GAL_EXT_z": np.array(phot_data["EXTINCTION"])[:, 4],   # mag(AB)

        # 2MASS (NIR) 
        "JMAG": np.array(phot_data["JMAG"]),                    # mag (Vega)
        "HMAG": np.array(phot_data["HMAG"]),                    # mag (Vega)
        "KMAG": np.array(phot_data["KMAG"]),                    # mag (Vega)

        # UKIDSS (YJHK)
        "YFLUX": np.array(phot_data["YFLUX"]),                  # densidad de flujo (W m^-2 Hz^-1)
        "JFLUX": np.array(phot_data["JFLUX"]),                  # densidad de flujo (W m^-2 Hz^-1)
        "HFLUX": np.array(phot_data["HFLUX"]),                  # densidad de flujo (W m^-2 Hz^-1)
        "KFLUX": np.array(phot_data["KFLUX"]),                  # densidad de flujo (W m^-2 Hz^-1)

        # WISE (IR medio) 
        "W1_FLUX": np.array(phot_data["W1_FLUX"]),              # mag (vega)
        "W2_FLUX": np.array(phot_data["W2_FLUX"]),              # mag (vega)
    })

    df_spec = pd.DataFrame({
        "SDSS_NAME": np.array(spec_data["SDSS_NAME"]),

        # Identificadores
        "PLATE"  : np.array(spec_data["PLATE"]),                  # adimensional
        "MJD"    : np.array(spec_data["MJD"]),                    # días (Modified Julian Date)
        "FIBERID": np.array(spec_data["FIBERID"]),                # adimensional

        # Anchos de línea NA (FWHM) 
        "FWHM_HA_NA": np.array(spec_data["FWHM_HA_NA"]),          # km s^-1  (línea Ha)
        "FWHM_HA_BR": np.array(spec_data["FWHM_HA_BR"]),          # km s^-1  (línea Ha)
        "FWHM_HB_NA": np.array(spec_data["FWHM_HB_NA"]),          # km s^-1  (línea Ha)
        "FWHM_HB_BR": np.array(spec_data["FWHM_HB_BR"]),          # km s^-1  (línea Ha)
        "FWHM_HG_BR": np.array(spec_data["FWHM_HG_BR"]),          # km s^-1  (línea Ha)
        "FWHM_MGII_NA": np.array(spec_data["FWHM_MGII_NA"]),      # km s^-1  (línea Mg II λ2798)
        "FWHM_MGII_BR": np.array(spec_data["FWHM_MGII_BR"]),      # km s^-1  (línea Mg II λ2798)

        "FWHM_CIII": np.array(spec_data["FWHM_CIII"]),            # km s^-1  (línea C IV λ1549)
        "FWHM_CIV" : np.array(spec_data["FWHM_CIV"]),             # km s^-1  (línea C IV λ1549)

        "FWHM_LYA": np.array(spec_data["FWHM_LYA"]),              # km s^-1  (línea C IV λ1549)
    })

    df_phot = convert_to_little_endian(df_phot).dropna()
    df_spec = convert_to_little_endian(df_spec).dropna()

    df_merged = pd.merge(df_phot, df_spec, on='SDSS_NAME', how='inner')

    df_merged.to_csv("data/pre_processed/SDSS_DR14Q.csv"   , index=False)
    df_phot.to_csv("data/pre_processed/SDSS_DR14Q_phot.csv", index=False)
    df_spec.to_csv("data/pre_processed/SDSS_DR14Q_spec.csv", index=False)