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

# a) Contar las categorías de RESPUESTA 1 con porcentaje
print("\nConteo y porcentaje de RESPUESTA 1:")
conteo_resp1 = df["RESPUESTA 1"].value_counts()
porcentaje_resp1 = df["RESPUESTA 1"].value_counts(normalize=True) * 100
print(pd.DataFrame({"conteo": conteo_resp1, "porcentaje": porcentaje_resp1.round(2)}))

# b) Contar RESPUESTA 2 agrupadas por RESPUESTA 1
print("\nConteo de RESPUESTA 2 agrupadas por RESPUESTA 1:")
print(df.groupby("RESPUESTA 1")["RESPUESTA 2"].value_counts())

# c) Contar SERVICIO con porcentaje
print("\nConteo y porcentaje de SERVICIO:")
conteo_servicio = df["SERVICIO"].value_counts()
porcentaje_servicio = df["SERVICIO"].value_counts(normalize=True) * 100
print(pd.DataFrame({"conteo": conteo_servicio, "porcentaje": porcentaje_servicio.round(2)}))

# d) Contar solo los RUT que se repiten más de una vez
ruts_repetidos = df["RUT"].value_counts()
ruts_mas_de_una_vez = ruts_repetidos[ruts_repetidos > 1]
print("\nRUTs que se repiten más de una vez:")
print(ruts_mas_de_una_vez)

# e) Contar días de la semana en español con porcentaje
print("\nConteo y porcentaje de días de la semana (en español):")
conteo_dias = df["dia_de_semana_es"].value_counts()
porcentaje_dias = df["dia_de_semana_es"].value_counts(normalize=True) * 100
print(pd.DataFrame({"conteo": conteo_dias, "porcentaje": porcentaje_dias.round(2)}))

# f) Contar franja horaria con porcentaje
print("\nConteo y porcentaje de franja horaria:")
conteo_franja = df["franja_horaria"].value_counts()
porcentaje_franja = df["franja_horaria"].value_counts(normalize=True) * 100
print(pd.DataFrame({"conteo": conteo_franja, "porcentaje": porcentaje_franja.round(2)}))

# g) Contar Plataforma con porcentaje
print("\nConteo y porcentaje de Plataforma:")
conteo_plataforma = df["Plataforma"].value_counts()
porcentaje_plataforma = df["Plataforma"].value_counts(normalize=True) * 100
print(pd.DataFrame({"conteo": conteo_plataforma, "porcentaje": porcentaje_plataforma.round(2)}))

# h) Contar Cliente con porcentaje
print("\nConteo y porcentaje de Cliente:")
conteo_cliente = df["Cliente"].value_counts()
porcentaje_cliente = df["Cliente"].value_counts(normalize=True) * 100
print(pd.DataFrame({"conteo": conteo_cliente, "porcentaje": porcentaje_cliente.round(2)}))

# i) Contar Tipo IVR con porcentaje
print("\nConteo y porcentaje de Tipo IVR:")
conteo_ivr = df["Tipo IVR"].value_counts()
porcentaje_ivr = df["Tipo IVR"].value_counts(normalize=True) * 100
print(pd.DataFrame({"conteo": conteo_ivr, "porcentaje": porcentaje_ivr.round(2)}))

columnas_reducidas = ["ID", "RESPUESTA 1", "RESPUESTA 2", "SERVICIO", "RUT", "CREADO", "Plataforma", "Cliente", "Tipo IVR"]
df = df_total[columnas_reducidas]

print(f"DataFrame reducido creado con {len(df)} filas y {len(df.columns)} columnas.")
