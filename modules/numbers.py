import codecs
from bs4 import BeautifulSoup
import pandas as pd
from collections import Counter


class NumbersWithHIghChanceOfWinning:
    def __init__(self, mega_sena_file):
        f = codecs.open(mega_sena_file, 'r')

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
                concurso, data, numero_1, numero_2, numero_3, numero_4, numero_5, numero_6, arrecadacao, \
                ganhadores_sena, cidade, uf, rateio_sena, ganhadores_quina, rateio_quina, ganhadores_quadra, \
                rateio_quadra, acumulado, valor_acomulado, estimativa, acomulado_mega_virada = [c.text for c in cols]
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

        self.mega_sena = pd.DataFrame({'datas': datas,
                                       'numeros_1': numeros_1,
                                       'numeros_2': numeros_2,
                                       'numeros_3': numeros_3,
                                       'numeros_4': numeros_4,
                                       'numeros_5': numeros_5,
                                       'numeros_6': numeros_6,
                                       'list_ganhadores_sena': list_ganhadores_sena,
                                       'list_ganhadores_quina': list_ganhadores_quina,
                                       'list_ganhadores_quadra': list_ganhadores_quadra}, index=concursos)

        # print mega_sena.to_dict()['numeros_1'][233]

        self.date_sequences = self.mega_sena[['datas', 'numeros_1', 'numeros_2', 'numeros_3',
                                              'numeros_4', 'numeros_5', 'numeros_6']] \
            .set_index('datas').T.to_dict('list')

        for key, value in self.date_sequences.items():
            value.sort()

        self.unique_sequences = [list(i) for i in set(tuple(j) for i, j in self.date_sequences.items())]

        chance_numero_1 = self.mega_sena.groupby('numeros_1').count()['list_ganhadores_sena'].to_dict()
        chance_numero_2 = self.mega_sena.groupby('numeros_2').count()['list_ganhadores_sena'].to_dict()
        chance_numero_3 = self.mega_sena.groupby('numeros_3').count()['list_ganhadores_sena'].to_dict()
        chance_numero_4 = self.mega_sena.groupby('numeros_4').count()['list_ganhadores_sena'].to_dict()
        chance_numero_5 = self.mega_sena.groupby('numeros_5').count()['list_ganhadores_sena'].to_dict()
        chance_numero_6 = self.mega_sena.groupby('numeros_6').count()['list_ganhadores_sena'].to_dict()

        chances = [chance_numero_1, chance_numero_2, chance_numero_3, chance_numero_4, chance_numero_5, chance_numero_6]

        c = Counter()
        for d in chances:
            c.update(d)

        self.percentage_of_number = dict(c)

        self.num_of_contests = sum(self.percentage_of_number.values()) / 6

        for key, value in self.percentage_of_number.items():
            self.percentage_of_number[key] = float(value) / self.num_of_contests

    def get_date_of_numbers(self, results):
        for date, numbers in self.date_sequences.iteritems():
            if numbers == results:
                return date

    def get_won_contests(self):
        return self.mega_sena[self.mega_sena.list_ganhadores_sena > 0]['list_ganhadores_sena'].count()
