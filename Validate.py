import pandas as pd

import pandera as pa

dataframe = pd.read_csv("/home/vinicius/Downloads/ocorrencia_2010_2020.csv",parse_dates=['ocorrencia_dia'], dayfirst=True)

dataframe.replace(["****", "**", "###!", "*****", "####"], pd.NA, inplace = True)

schema = pa.DataFrameSchema(
    columns = {
        'codigo_ocorrencia':pa.Column(pa.Int),
        'codigo_ocorrencia2':pa.Column(pa.Int),
        'ocorrencia_classificacao':pa.Column(pa.String),
        'ocorrencia_cidade':pa.Column(pa.String),
        'ocorrencia_uf':pa.Column(pa.String),
        'ocorrencia_aerodromo':pa.Column(pa.String, nullable = True),
        'ocorrencia_dia':pa.Column(pa.DateTime),
        'ocorrencia_hora':pa.Column(pa.String),
        'total_recomendacoes':pa.Column(pa.Int)
    }
)
schema.validate(dataframe)
