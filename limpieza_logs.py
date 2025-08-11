import pandas as pd

# Leer el archivo CSV
df_log = pd.read_csv("Log accesos.csv", encoding="latin1")

# Seleccionar solo las columnas necesarias
columnas_necesarias = [
    "RUT_EMPRESA", "RUT_USUARIO", "FECHA_REGISTRO", "USU_NOMBRE",
    "USU_APELLIDO_PATERNO", "USU_APELLIDO_MATERNO", "NOMBRE"
]
df_log = df_log[columnas_necesarias]

# Convertir FECHA_REGISTRO a tipo datetime
df_log["FECHA_REGISTRO"] = pd.to_datetime(df_log["FECHA_REGISTRO"], errors="coerce")

# Ordenar por FECHA_REGISTRO descendente y dejar solo el registro más reciente por RUT_EMPRESA y RUT_USUARIO
df_log_limpio = (
    df_log.sort_values("FECHA_REGISTRO", ascending=False)
    .drop_duplicates(subset=["RUT_EMPRESA", "RUT_USUARIO"], keep="first")
    .reset_index(drop=True)
)

print(df_log_limpio)