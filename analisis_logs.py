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
import pandas as pd

# Cargar los CSV
call_center = pd.read_csv("centralizado_call_center.csv")
logs = pd.read_csv("logs.csv")
rpais = pd.read_csv("RPAIS.csv")

# Primer cruce: call_center (RUT) con logs (RUT_USUARIO)
call_logs = call_center.merge(logs, left_on="RUT", right_on="RUT_USUARIO", how="inner")

# Segundo cruce: call_logs (RUT_EMPRESA) con rpais (RUT_EMPRESA_COMPLETO)
call_logs_rpais = call_logs.merge(rpais, left_on="RUT_EMPRESA", right_on="RUT_EMPRESA_COMPLETO", how="inner")

# Mostrar el DataFrame resultante en consola
print(call_logs_rpais)

logs = pd.read_csv("logs.csv")

