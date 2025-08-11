import pandas as pd

# Cargar los dos CSV en dataframes
call_center = pd.read_csv("centralizado_call_center.csv")
columnas_reducidas = ["ID", "RESPUESTA 1", "RESPUESTA 2", "SERVICIO", "RUT", "CREADO", "Plataforma", "Cliente", "Tipo IVR"]
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

# Mostrar el resultado en consola
print(call_center_rpais)
