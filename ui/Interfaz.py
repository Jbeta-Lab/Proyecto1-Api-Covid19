import pandas as pd
from api.ConsultaApi import consultar_casos

def pedir_datos():
    departamento = input("Departamento a consultar: ").strip()

    while True:
        texto = input("Número de registros (ej. 20): ").strip()
        if texto.isdigit() and int(texto) > 0:
            limite = int(texto)
            break
        print("Por favor ingrese un número entero mayor que 0.")

    return departamento, limite

def mostrar_resultados(df):
    if df.empty:
        print("No se encontraron registros para esa consulta.")
        return

    formato = "{:<22} {:<14} {:>5}  {:<14} {:<10} {:<20}"
    print(formato.format("Ciudad", "Departamento", "Edad", "Tipo", "Estado", "País de procedencia"))
    print("-" * 95)

    for _, fila in df.iterrows():
        pais = fila["pais_viajo_1_nom"]
        if pd.isna(pais):
            pais = "N/A"
        print(formato.format(
            str(fila["ciudad_municipio_nom"]),
            str(fila["departamento_nom"]),
            str(fila["edad"]),
            str(fila["fuente_tipo_contagio"]),
            str(fila["estado"]),
            str(pais),
        ))

def ejecutar():
    departamento, limite = pedir_datos()
    print("\nConsultando, por favor espere...\n")
    df = consultar_casos(departamento, limite)
    mostrar_resultados(df)
