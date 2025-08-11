import pandas as pd

# Cargar solo las columnas necesarias
call_center = pd.read_csv("centralizado_call_center.csv", usecols=["ID", "RESPUESTA 1", "RESPUESTA 2", "SERVICIO", "RUT", "IVR", "CREADO", "Plataforma", "Cliente", "Tipo IVR"])
logs = pd.read_csv("logs.csv", usecols=["RUT_EMPRESA", "RUT_USUARIO", "FECHA_REGISTRO", "USU_NOMBRE", "USU_APELLIDO_PATERNO", "USU_APELLIDO_MATERNO", "NOMBRE"])
rpais = pd.read_csv("RPAIS.csv", usecols=[
    "ADHR_RAZON_SOCIAL", "ADHR_RUT_EMPRESA", "ADHR_DV_EMPRESA", "ADHR_ESTADO",
    "ADHR_MACROSEGMENTO", "ADHR_MACROSEGMENTO_N2", "ADHR_CCHC", "CART_CARTERA(2)",
    "Nombre Cliente", "Estado", "CLSF_CODIGO", "Actividad Economica", "RUT_EMPRESA_COMPLETO"
])

# Eliminar duplicados en las llaves antes de cruzar
#call_center = call_center.drop_duplicates(subset=["RUT"])
#logs = logs.drop_duplicates(subset=["RUT_USUARIO"])
#rpais = rpais.drop_duplicates(subset=["RUT_EMPRESA_COMPLETO"])

# Primer cruce: call_center (RUT) con logs (RUT_USUARIO)
call_logs = call_center.merge(logs, left_on="RUT", right_on="RUT_USUARIO", how="inner")

# Segundo cruce: call_logs (RUT_EMPRESA) con rpais (RUT_EMPRESA_COMPLETO)
call_logs_rpais = call_logs.merge(rpais, left_on="RUT_EMPRESA", right_on="RUT_EMPRESA_COMPLETO", how="inner")

# Mostrar el DataFrame resultante en consola
print(call_logs_rpais)

# Guardar el DataFrame final en un archivo Excel
call_logs_rpais.to_excel("call_logs_rpais.xlsx", index=False)
print("Archivo call_logs_rpais.xlsx creado correctamente.")

