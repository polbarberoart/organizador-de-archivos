# organizer_sc.py
import os
import shutil
from datetime import datetime

# Rutas directas en inglés
ruta_usuario = os.path.expanduser('~')
ruta_descargas = os.path.join(ruta_usuario, 'Downloads')
ruta_documentos = os.path.join(ruta_usuario, 'Documents')
ruta_organizados = os.path.join(ruta_documentos, 'Organizados')

# Verificación simple de que existan las carpetas
if not os.path.exists(ruta_descargas):
    print("Error: No se encontró la carpeta Downloads")
    exit()

if not os.path.exists(ruta_documentos):
    print("Error: No se encontró la carpeta Documents")
    exit()

# Definir las rutas de las carpetas de destino para cada tipo de archivo
rutas_destino = {
    'imagenes': os.path.join(ruta_organizados, 'Imagenes'),
    'csv': os.path.join(ruta_organizados, 'CSV'),
    'json': os.path.join(ruta_organizados, 'JSON'),
    'pdf': os.path.join(ruta_organizados, 'PDF'),
    'videos': os.path.join(ruta_organizados, 'Videos'),
    'excel': os.path.join(ruta_organizados, 'Excel'),
    'mp3': os.path.join(ruta_organizados, 'MP3'),
    'otros': os.path.join(ruta_organizados, 'Otros')
}

# Crear las carpetas de destino si no existen
for ruta in rutas_destino.values():
    os.makedirs(ruta, exist_ok=True)

# Definir las extensiones y su categoría
extensiones = {
    '.jpg': 'imagenes',
    '.jpeg': 'imagenes',
    '.png': 'imagenes',
    '.gif': 'imagenes',
    '.csv': 'csv',
    '.xlsx': 'excel',
    '.xls': 'excel',
    '.json': 'json',
    '.pdf': 'pdf',
    '.mp4': 'videos',
    '.avi': 'videos',
    '.mov': 'videos',
    '.mp3': 'mp3'
    # Puedes agregar más extensiones si lo necesitas
}

def obtener_fecha_archivo(ruta_archivo):
    # Obtener la fecha de modificación del archivo
    timestamp = os.path.getmtime(ruta_archivo)
    fecha = datetime.fromtimestamp(timestamp)
    return fecha.strftime('%d-%m-%Y')

# Función para procesar los archivos en la carpeta de descargas
def procesar_archivos():
    try:
        # Verificar si la carpeta de descargas existe
        if not os.path.exists(ruta_descargas):
            print(f"La carpeta de descargas no existe: {ruta_descargas}")
            return

        # Obtener la lista de archivos en la carpeta de descargas
        archivos = os.listdir(ruta_descargas)

        if not archivos:
            print("No hay archivos para procesar en la carpeta de descargas")
            return

        # Procesar cada archivo de la carpeta de descargas
        for archivo in archivos:
            try:
                ruta_archivo = os.path.join(ruta_descargas, archivo)
                
                if os.path.isfile(ruta_archivo):
                    nombre, extension = os.path.splitext(archivo)
                    extension = extension.lower()
                    fecha = obtener_fecha_archivo(ruta_archivo)
                    
                    # Crear nuevo nombre con fecha
                    nombre_con_fecha = f"{nombre}_{fecha}{extension}"
                    
                    categoria = extensiones.get(extension, 'otros')
                    ruta_destino = rutas_destino[categoria]
                    ruta_nueva = os.path.join(ruta_destino, nombre_con_fecha)
                    
                    # Manejar duplicados si existen
                    if os.path.exists(ruta_nueva):
                        contador = 1
                        while os.path.exists(ruta_nueva):
                            nombre_nuevo = f"{nombre}_{fecha}_{contador}{extension}"
                            ruta_nueva = os.path.join(ruta_destino, nombre_nuevo)
                            contador += 1
                    
                    shutil.move(ruta_archivo, ruta_nueva)
                    print(f"Movido: {archivo} -> {os.path.basename(ruta_nueva)}")

            except Exception as e:
                print(f"Error al procesar el archivo {archivo}: {str(e)}")
    except Exception as e:
        print(f"Error general: {str(e)}")

# Ejecutar la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    procesar_archivos()
