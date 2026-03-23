import pandas as pd
import numpy as np
from astropy.io import fits

def open_fits(filepath: str):
    with fits.open(filepath) as hdul:
        header = hdul[1].header
        data   = hdul[1].data
    return header, data

if __name__ == "__main__":
    # Abrimos los identificadores
    ide_header, ide_data = open_fits("data/raw/asu.fit")

    plate_arr = np.array(ide_data["Plate"])
    mjd_arr   = np.array(ide_data["MJD"])
    fiber_arr = np.array(ide_data["Fiber"])

    df_identifiers = pd.DataFrame({
        "SDSS_NAME": ide_data["SDSS"], 
        "PLATE": plate_arr.byteswap().view(plate_arr.dtype.newbyteorder('<')),
        "MJD"  : mjd_arr.byteswap().view(mjd_arr.dtype.newbyteorder('<')),
        "FIBER": fiber_arr.byteswap().view(fiber_arr.dtype.newbyteorder('<')),
    }).dropna()
   
    df = pd.read_csv("./data/processed/top_10_per_community.csv")
    df = pd.merge(df, df_identifiers, on="SDSS_NAME", how="left").dropna(subset=['PLATE', 'MJD', 'FIBER'])

    print(f"Generando enlaces para {len(df)} objetos...\n")

    # Agrupamos el DataFrame por la columna 'community'
    # Sort=True asegura que vaya en orden (0, 1, 2...)
    for comunidad, grupo in df.groupby('community', sort=True):
        
        # Opcional: puedes descomentar la siguiente línea si quieres un título para cada bloque
        print(f"--- Comunidad {comunidad} ---")
        
        for index, row in grupo.iterrows():
            plate     = int(row['PLATE'])
            mjd       = int(row['MJD'])
            fiber     = int(row['FIBER'])
            
            print(f"{plate}, {mjd}, {fiber}")
            
# https://dr16.sdss.org/optical/spectrum/search