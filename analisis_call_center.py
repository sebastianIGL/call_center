import pandas as pd
df_total = pd.read_csv("centralizado_call_center.csv")

# Seleccionar solo las columnas necesarias
columnas_reducidas = ["ID", "RESPUESTA 1", "RESPUESTA 2", "SERVICIO", "RUT", "CREADO", "Plataforma", "Cliente", "Tipo IVR"]
df = df_total[columnas_reducidas]

# Procesar la columna "CREADO" para extraer fecha, día de semana y franja horaria
def convertir_fecha(fecha_str):
    for fmt in ("%Y-%m-%d %H:%M:%S", "%d/%m/%Y %H:%M:%S"):
        try:
            return pd.to_datetime(fecha_str, format=fmt)
        except (ValueError, TypeError):
            continue
    return pd.NaT

df["CREADO"] = df["CREADO"].apply(convertir_fecha)
df["dia_de_semana"] = df["CREADO"].dt.day_name()

dias_semana_es = {
    "Monday": "Lunes",
    "Tuesday": "Martes",
    "Wednesday": "Miércoles",
    "Thursday": "Jueves",
    "Friday": "Viernes",
    "Saturday": "Sábado",
    "Sunday": "Domingo"
}
df["dia_de_semana_es"] = df["dia_de_semana"].map(dias_semana_es)

def franja_horaria(row):
    if pd.isnull(row):
        return "desconocido"
    h = row.hour
    if 6 <= h < 12:
        return "mañana"
    elif 12 <= h < 18:
        return "tarde"
    elif 18 <= h < 24:
        return "noche"
    else:
        return "madrugada"

df["franja_horaria"] = df["CREADO"].apply(franja_horaria)

# a) Contar las categorías de RESPUESTA 1
print("\nConteo de RESPUESTA 1:")
print(df["RESPUESTA 1"].value_counts())

# b) Contar RESPUESTA 2 agrupadas por RESPUESTA 1
print("\nConteo de RESPUESTA 2 agrupadas por RESPUESTA 1:")
print(df.groupby("RESPUESTA 1")["RESPUESTA 2"].value_counts())

# c) Contar SERVICIO
print("\nConteo de SERVICIO:")
print(df["SERVICIO"].value_counts())

# d) Contar solo los RUT que se repiten más de una vez
ruts_repetidos = df["RUT"].value_counts()
ruts_mas_de_una_vez = ruts_repetidos[ruts_repetidos > 1]
print("\nRUTs que se repiten más de una vez:")
print(ruts_mas_de_una_vez)

# e) Contar los días de la semana en español
print("\nConteo de días de la semana (en español):")
print(df["dia_de_semana_es"].value_counts())

# e) Contar franja horaria
print("\nConteo de franja horaria:")
print(df["franja_horaria"].value_counts())

# f) Contar Plataforma
print("\nConteo de Plataforma:")
print(df["Plataforma"].value_counts())

# g) Contar Cliente
print("\nConteo de Cliente:")
print(df["Cliente"].value_counts())

# h) Contar Tipo IVR
print("\nConteo de Tipo IVR:")
print(df["Tipo IVR"].value_counts())

columnas_reducidas = ["ID", "RESPUESTA 1", "RESPUESTA 2", "SERVICIO", "RUT", "CREADO", "Plataforma", "Cliente", "Tipo IVR"]
df = df_total[columnas_reducidas]

print(f"DataFrame reducido creado con {len(df)} filas y {len(df.columns)} columnas.")
