import os
import requests

def download_real_sfd_maps(output_dir="../data/dustmaps/"):
    os.makedirs(output_dir, exist_ok=True)
    
    # Repositorio oficial de datos mantenido por el autor de sfdmap
    urls = {
        "SFD_dust_4096_ngp.fits": "https://raw.githubusercontent.com/kbarbary/sfddata/master/SFD_dust_4096_ngp.fits",
        "SFD_dust_4096_sgp.fits": "https://raw.githubusercontent.com/kbarbary/sfddata/master/SFD_dust_4096_sgp.fits"
    }
    
    for filename, url in urls.items():
        file_path = os.path.join(output_dir, filename)
        
        if os.path.exists(file_path):
            # Si el archivo pesa menos de 1MB, es el de prueba que dio error. Lo borramos.
            if os.path.getsize(file_path) < 1000000:
                print(f"Borrando archivo falso/corrupto: {filename}...")
                os.remove(file_path)
            else:
                print(f"✓ {filename} ya existe y es correcto. Saltando...")
                continue
            
        print(f"Descargando {filename} desde GitHub (Aprox. 45 MB)...")
        try:
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status() 
            
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"✓ {filename} descargado con éxito.")
            
        except Exception as e:
            print(f"Error al descargar {filename}: {e}")

if __name__ == "__main__":
    print("Iniciando descarga de los mapas SFD desde el repositorio oficial...")
    download_real_sfd_maps()
    print("¡Proceso completado!")