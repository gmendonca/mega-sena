import codecs
from bs4 import BeautifulSoup

f = codecs.open("D_MEGA.HTM", 'r')

soup = BeautifulSoup(f.read(), 'html.parser')

table = soup.find("table")

rows = table.findAll('tr')

for tr in rows:
    cols = tr.findAll('td')
    if len(cols) > 3:
        concurso, data, numero_1, numero_2, numero_3, numero_4, numero_5, numero_6, arrecadacao, ganhadores_sena, \
        cidade, uf, rateio_sena, ganhadores_quina, rateio_quina, ganhadores_quadra, rateio_quadra, acumulado, \
        valor_acomulado, estimativa, acomulado_mega_virada = [c.text for c in cols]
        print concurso, data, numero_1, numero_2, numero_3, numero_4, numero_5, numero_6, \
            ganhadores_sena, ganhadores_quina, ganhadores_quadra
