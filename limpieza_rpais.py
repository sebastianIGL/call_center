# Cargar variables de entorno desde .env
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

# Ruta base y nombres de archivo desde .env
ruta_base = os.getenv("RUTA_BASE")
nombre_rpais = os.getenv("RPAIS")

ruta_rpais = r"C:\Users\sgati\OneDrive\Documentos\Data_Mutual\Rpais nueva versión reducida 01-08-25.xlsx"

# Leer la hoja "default_1"
df_rpais = pd.read_excel(ruta_rpais, sheet_name="default_1")

# Seleccionar solo las columnas necesarias
columnas_necesarias = [
    "ADHR_RAZON_SOCIAL", "ADHR_RUT_EMPRESA", "ADHR_DV_EMPRESA",
    "ADHR_ESTADO",
    "ADHR_MACROSEGMENTO", "ADHR_MACROSEGMENTO_N2", "ADHR_CCHC", "CART_CARTERA(2)",
    "Nombre Cliente",
    "Estado", "CLSF_CODIGO", "Actividad Economica"
]
df_rpais = df_rpais[columnas_necesarias]

print(f"DataFrame reducido creado con {len(df_rpais)} filas y {len(df_rpais.columns)} columnas.")

# Filtrar donde ADHR_ESTADO == "A"
df_filtrado = df_rpais[df_rpais["ADHR_ESTADO"] == "A"].copy()

# Crear columna RUT_EMPRESA_COMPLETO concatenando ADHR_RUT_EMPRESA y ADHR_DV_EMPRESA con "-"
df_filtrado["RUT_EMPRESA_COMPLETO"] = df_filtrado["ADHR_RUT_EMPRESA"].astype(str) + "-" + df_filtrado["ADHR_DV_EMPRESA"].astype(str)

# Guardar el DataFrame filtrado como CSV
df_filtrado.to_csv("RPAIS.csv", index=False, encoding="utf-8-sig")


