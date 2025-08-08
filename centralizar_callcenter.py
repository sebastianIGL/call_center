# Cargar variables de entorno desde .env
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

# Ruta base y nombres de archivo desde .env
ruta_base = os.getenv("RUTA_BASE")

# Lista de nombres de archivos a procesar (agrega aquí los nombres de tus archivos)
nombre_archivo = [
    "Informe Mutual EPA 2023 Noviembre.xlsx",
    "Informe Mutual EPA 2023 - Diciembre.xlsx",
    "Informe Mutual EPA 2024 - Enero.xlsx",
    "Informe Mutual EPA 2024 - Febrero.xlsx",
    "Informe Mutual EPA 2024 - Marzo.xlsx",
    "Informe Mutual EPA 2024 - Abril 2024.xlsx",
    "Informe Mutual EPA 2024 - Mayo 2024.xlsx",
    "Informe Mutual EPA 2024 - Junio.xlsx",
    "Informe Mutual EPA 2024 - Julio.xlsx",
    "Informe Mutual EPA 2024 - Agosto.xlsx",
    "Informe Mutual EPA 2024 - Septiembre.xlsx",
    "Informe Mutual EPA 2024 - Octubre.xlsx",
    "Informe Mutual EPA 2024 - Noviembre.xlsx",
    "Informe Mutual EPA 2024 - Diciembre.xlsx",
    "Informe Mutual EPA 2025 - Enero.xlsx",
    "Informe Mutual EPA 2025 - Febrero.xlsx",
    "Informe Mutual EPA 2025 - Marzo.xlsx",
    "Informe Mutual EPA 2025 - Abril.xlsx",
    "Informe Mutual EPA 2025 - Mayo.xlsx",
    "Informe Mutual EPA 2025 - Junio.xlsx",
]


# Nombre de la hoja a leer	
hoja = "BBDD EPA"

# Columnas esperadas en el DataFrame final
columnas = [
    "VALIDACIÓN", "ID", "LLAMADA", "RESPUESTA 1", "RESPUESTA 2", "SERVICIO", "RUT", "TELEFONO", "IVR", "AGENTE", "CREADO", "Fecha Fix", "Plataforma", "DNIS", "Cliente", "Conclucion Final", "Conclucion", "Tipo IVR"
]

df_total = pd.DataFrame(columns=columnas)

for archivo in nombre_archivo:
    ruta_archivo = os.path.join(ruta_base, archivo)
    try:
        df = pd.read_excel(ruta_archivo, sheet_name=hoja)
        # Asegurar que todas las columnas estén presentes y rellenar con "" donde falten
        for col in columnas:
            if col not in df.columns:
                df[col] = ""
        # Reordenar columnas
        df = df[columnas]
        df_total = pd.concat([df_total, df], ignore_index=True)
    except Exception as e:
        print(f"Error al procesar {archivo}: {e}")

# Guardar el DataFrame centralizado en un archivo CSV en la carpeta del repositorio
output_csv = os.path.join(os.path.dirname(__file__), "centralizado_call_center.csv")
# df_total.to_csv(output_csv, index=False, encoding="utf-8-sig")  # Comentado para respaldar el archivo correcto
print(f"Archivo CSV respaldado en: {output_csv}")
print(f"Cantidad total de filas: {len(df_total)}")
# --- Análisis exploratorio solicitado ---
