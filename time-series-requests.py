import requests
import xmltodict
import json

request_params = []
qtd_stations = int(input())

for i in range(qtd_stations+4):
    request_params.append(str(input()))


stations = request_params[:qtd_stations]
data_inicio = request_params[qtd_stations]
data_fim = request_params[qtd_stations+1]
tipo_dados = request_params[qtd_stations+2]
nivel_consistencia = request_params[qtd_stations+3]

# print(stations)
# print(data_inicio)
# print(data_fim)
# print(tipo_dados)
# print(nivel_consistencia)


def get_time_series(station, data_inicio, data_fim, tipo_dados, nivel_consistencia):
    endpoint = "http://telemetriaws1.ana.gov.br/ServiceANA.asmx/HidroSerieHistorica"
    params = {
        "codEstacao": station,
        "dataInicio": data_inicio,
        "dataFim": data_fim,
        "tipoDados": tipo_dados,
        "nivelConsistencia": nivel_consistencia,
    }
    # print(params)
    r = requests.get(endpoint, params=params)
    # print(r.request)
    return json.dumps(xmltodict.parse(r.content))
    # return 'aaa'


print(get_time_series(stations[0], data_inicio,
      data_fim, tipo_dados, nivel_consistencia))
