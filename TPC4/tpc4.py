import json
import re

# VER OS EXEMPLOS QUE FALTAM (3 PRA FRENTE)

class Database:
    def __init__(self):
        self.properties = {}

    def parseLines(self,ficheiro):
        file1 = open(ficheiro, 'r')
        lines = file1.readlines()

        skip = False

        somaF = False
        mediaF = False
        pLista = False
        soma = 0
        counter = 0
        nameLista = ""

        rgxLista = r',?(?P<nomeLista>\w+)\{(?P<menor>\d+),*(?P<maior>\d+)*\}:?:?(?P<tipo>\w+)?'
        rgxSum = r'\w+_(?:sum)'
        rgxMedia= r'\w+_(?:media)'

        # guarda os tipos dos valores a armazenar
        order = []

        # controla as linhas a que cada valor pertence
        i = -1

        for l in lines:
            l = l.strip()
            # linha dos parametros (primeira linha)
            if i == -1:
                tipos = re.split(",", l)
                s = 0
                while s < len(tipos):
                    # case: tipo{3,5} e tipo{3,5}::<param>
                    if ('{' in tipos[s]) and ('}' not in tipos[s]):
                        #print("LISTA DE DOIS")
                        tipos[s] = tipos[s] + "," + tipos[s+1]
                        skip = True

                    # case: LISTA
                    if '{' in tipos[s]:
                        pLista = True
                        lista = re.findall(rgxLista,tipos[s])

                        # se nao houver agregacao
                        if lista[0][3] == '':
                            param = lista[0][0]
                        # se houver agregacao
                        else:
                            param = lista[0][0] + "_" + lista[0][3]

                        menor = int(lista[0][1])

                        # se houver intervalo de valores na lista
                        if lista[0][2] != "":
                            maior = int(lista[0][2])
                            self.properties.update({param : {"{N,M}" : (menor,maior)}})
                        else:
                            self.properties.update({param: {"{N,M}": ("",menor)}})
                        order.append(param)

                    # case , da lista
                    elif tipos[s] == "":
                        order.append(",")

                    # case: param normal
                    else:
                        self.properties.update({tipos[s] : {}})
                        order.append(tipos[s])

                    # caso tenha apanhado tipo{3,5}, passa o proximo á frente
                    if skip:
                        skip = False
                        s += 1

                    s += 1

            # linha dos valores
            else:
                #print(self.properties)
                valores = re.split(",", l)
                # if order == lista, ignorar esse e so contam os que tao pra frente
                #print(order)
                #print(valores)
                #print(pLista)
                #print(pLista and len(valores) != (len(order) - 1))

                # se houver uma lista
                if pLista:
                    # verifica se o num de campos e valido
                    if len(valores) != (len(order) - 1):
                        #print("continue")
                        continue
                # verifica se o num de campos e valido
                elif len(valores) != len(order):
                    #print("continue")
                    continue

                # controla o campo em que o valor e inserido
                j = 0
                for v in valores:
                    # se soma
                    if re.match(rgxSum,order[j]) != None:
                        #print("SOMA")
                        somaF = True

                    # se media
                    elif re.match(rgxMedia,order[j]) != None:
                        #print("MEDIA")
                        mediaF = True

                    # se houver campo que é lista
                    if order[j] != "," and "{N,M}" in self.properties[order[j]].keys():
                        nameLista = order[j]
                        j += 1
                        #campos = int(self.properties[order[j]]["{N,M}"][1])


                    # se elemento da lista
                    if order[j] == "," and v != "":
                        # calcula-se a soma e a media, caso haja agreg
                        if somaF or mediaF:
                            soma += int(v)
                            if mediaF:
                                counter += 1
                        # lista sem agreg
                        else:
                            # se ainda nao existir lista para a linha no dict, cria
                            if i not in self.properties[nameLista].keys():
                                #print("nao ha i, elemento: " + str(j))
                                self.properties[nameLista].update({i:[v]})
                            # adiciona valor a lista
                            else:
                                #print("ja ha i, elemento: " + str(j))
                                #print("aux: " + str(j) + " "+ str(self.properties.get(nameLista).get(i)))
                                self.properties[nameLista][i] += [v]

                    # se valor normal, ou caso haja uma funcao de agregacao e estamos no ultimo elemento da lista
                    if order[j] != "," or ((somaF or mediaF) and j == (len(order) - 1)):
                        # insere-se a soma dos elementos da lista
                        if somaF:
                            self.properties[nameLista].update({i: soma})
                            somaF = False
                            soma = 0

                        # insere-se a media dos elementos da lista
                        elif mediaF:
                            media = soma / counter
                            self.properties[nameLista].update({i: media})
                            mediaF = False
                            soma = 0
                            counter = 0

                        # caso seja um valor normal
                        else:
                            self.properties[order[j]].update({i: v})
                        nameLista = ""
                    j += 1
            i += 1
        return i

    def criaJson(self,ficheiro,linhas):
        i = 0
        while(i <= linhas)
