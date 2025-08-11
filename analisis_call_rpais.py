import pandas as pd

# Cargar los dos CSV en dataframes
call_center = pd.read_csv("centralizado_call_center.csv")
columnas_reducidas = ["ID", "RESPUESTA 1", "RESPUESTA 2", "SERVICIO", "RUT","IVR", "CREADO", "Plataforma", "Cliente", "Tipo IVR"]
call_center = call_center[columnas_reducidas]

rpais = pd.read_csv("RPAIS.csv")
columnas_necesarias = [
    "ADHR_RAZON_SOCIAL", "ADHR_RUT_EMPRESA", "ADHR_DV_EMPRESA",
    "ADHR_ESTADO",
    "ADHR_MACROSEGMENTO", "ADHR_MACROSEGMENTO_N2", "ADHR_CCHC", "CART_CARTERA(2)",
    "Nombre Cliente",
    "Estado", "CLSF_CODIGO", "Actividad Economica", "RUT_EMPRESA_COMPLETO"
]
rpais = rpais[columnas_necesarias]


# Realizar el cruce (merge) usando las llaves correspondientes
call_center_rpais = call_center.merge(rpais, left_on="RUT", right_on="RUT_EMPRESA_COMPLETO", how="inner")


        #FILTRO APLICADO EN BASE AL NOMBRE CLIENTE
#call_center_rpais = call_center_rpais[call_center_rpais["Nombre Cliente"].str.contains("CENCOSUD", case=False, na=False)]

# Mostrar el resultado en consola
print(call_center_rpais)

# a) Contar las categorías de RESPUESTA 1 con porcentaje
print("\nConteo y porcentaje de RESPUESTA 1 (cruce):")
conteo_resp1 = call_center_rpais["RESPUESTA 1"].value_counts()
porcentaje_resp1 = call_center_rpais["RESPUESTA 1"].value_counts(normalize=True) * 100
print(pd.DataFrame({"conteo": conteo_resp1, "porcentaje": porcentaje_resp1.round(2)}))

# b) Contar RESPUESTA 2 agrupadas por RESPUESTA 1
print("\nConteo de RESPUESTA 2 agrupadas por RESPUESTA 1 (cruce):")
print(call_center_rpais.groupby("RESPUESTA 1")["RESPUESTA 2"].value_counts())

# c) Contar SERVICIO con porcentaje
print("\nConteo y porcentaje de SERVICIO (cruce):")
conteo_servicio = call_center_rpais["SERVICIO"].value_counts()
porcentaje_servicio = call_center_rpais["SERVICIO"].value_counts(normalize=True) * 100
print(pd.DataFrame({"conteo": conteo_servicio, "porcentaje": porcentaje_servicio.round(2)}))

# d) Contar solo los RUT que se repiten más de una vez, mostrando también ADHR_RAZON_SOCIAL, cantidad y porcentaje
ruts_repetidos = call_center_rpais["RUT"].value_counts()
ruts_mas_de_una_vez = ruts_repetidos[ruts_repetidos > 1]

df_ruts = call_center_rpais[call_center_rpais["RUT"].isin(ruts_mas_de_una_vez.index)][["ADHR_RAZON_SOCIAL", "RUT"]]
df_ruts = df_ruts.drop_duplicates()

# Crear DataFrame con cantidad y porcentaje
df_ruts_analisis = (
    call_center_rpais[call_center_rpais["RUT"].isin(ruts_mas_de_una_vez.index)]
    .groupby(["ADHR_RAZON_SOCIAL", "RUT"])
    .size()
    .reset_index(name="cantidad")
)
df_ruts_analisis["porcentaje"] = (df_ruts_analisis["cantidad"] / len(call_center_rpais) * 100).round(2)

print("\nRUTs que se repiten más de una vez (cruce) con ADHR_RAZON_SOCIAL, cantidad y porcentaje:")
print(df_ruts_analisis)

# g) Contar Plataforma con porcentaje
print("\nConteo y porcentaje de Plataforma (cruce):")
conteo_plataforma = call_center_rpais["Plataforma"].value_counts()
porcentaje_plataforma = call_center_rpais["Plataforma"].value_counts(normalize=True) * 100
print(pd.DataFrame({"conteo": conteo_plataforma, "porcentaje": porcentaje_plataforma.round(2)}))

# i) Contar Tipo IVR con porcentaje
print("\nConteo y porcentaje de Tipo IVR (cruce):")
conteo_ivr = call_center_rpais["Tipo IVR"].value_counts()
porcentaje_ivr = call_center_rpais["Tipo IVR"].value_counts(normalize=True) * 100
print(pd.DataFrame({"conteo": conteo_ivr, "porcentaje": porcentaje_ivr.round(2)}))

# Guardar el DataFrame filtrado en un archivo Excel
#call_center_rpais.to_excel("call_center_rpais_cencosud.xlsx", index=False)
#print("El archivo Excel ha sido guardado exitosamente.")
