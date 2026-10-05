import pandas as pd
from sodapy import Socrata

DOMINIO = "www.datos.gov.co"
DATASET = "gt2j-8ykr"

COLUMNAS = [
    "ciudad_municipio_nom",
    "departamento_nom",
    "edad",
    "fuente_tipo_contagio",
    "estado",
    "pais_viajo_1_nom",
]

def consultar_casos(nombre_departamento, limite_registros):
    client = Socrata(DOMINIO, None)
    results = client.get(
        DATASET,
        limit=limite_registros,
        departamento_nom=nombre_departamento.upper(),
    )
    df = pd.DataFrame.from_records(results)

    if df.empty:
        return df

    df = df.reindex(columns=COLUMNAS)
    return df