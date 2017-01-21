import codecs
from bs4 import BeautifulSoup

f = codecs.open("D_MEGA.HTM", 'r')

soup = BeautifulSoup(f.read(), 'html.parser')

table = soup.find("table")

rows = table.findAll('tr')

concursos = []
datas = []
numeros_1 = []
numeros_2 = []
numeros_3 = []
numeros_4 = []
numeros_5 = []
numeros_6 = []
list_ganhadores_sena = []
list_ganhadores_quina = []
list_ganhadores_quadra = []

for tr in rows:
    cols = tr.findAll('td')
    if len(cols) > 3:
        concurso, data, numero_1, numero_2, numero_3, numero_4, numero_5, numero_6, arrecadacao, ganhadores_sena, \
        cidade, uf, rateio_sena, ganhadores_quina, rateio_quina, ganhadores_quadra, rateio_quadra, acumulado, \
        valor_acomulado, estimativa, acomulado_mega_virada = [c.text for c in cols]
        concursos += [int(concurso)]
        datas += [str(data)]
        numeros_1 += [int(numero_1)]
        numeros_2 += [int(numero_2)]
        numeros_3 += [int(numero_3)]
        numeros_4 += [int(numero_4)]
        numeros_5 += [int(numero_5)]
        numeros_6 += [int(numero_6)]
        list_ganhadores_sena += [int(ganhadores_sena)]
        list_ganhadores_quina += [int(ganhadores_quina)]
        list_ganhadores_quadra += [int(ganhadores_quadra)]

mega_sena = {'concursos': concursos,
             'datas': datas,
             'numeros_1': numeros_1,
             'numeros_2': numeros_2,
             'numeros_3': numeros_3,
             'numeros_4': numeros_4,
             'numeros_5': numeros_5,
             'numeros_6': numeros_6,
             'list_ganhadores_sena': list_ganhadores_sena,
             'list_ganhadores_quina': list_ganhadores_quina,
             'list_ganhadores_quadra': list_ganhadores_quadra}
