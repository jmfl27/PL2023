import json
import re

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
        order = []

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
                        print("LISTA DE DOIS")
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
                print(order)
                print(self.properties)
                valores = re.split(",", l)
                # if order == lista, ignorar esse e so contam os que tao pra frente
                print(valores)
                print(order)
                print(pLista)
                print(pLista and len(valores) != (len(order) - 1))
                if pLista:
                    if len(valores) != (len(order) - 1):continue
                elif len(valores) != len(order):
                    continue

                j = 0
                for v in valores:
                    # se soma
                    if re.match(rgxSum,order[j]) != None:
                        somaF = True

                    # se media
                    elif re.match(rgxMedia,order[j]) != None:
                        mediaF = True

                    # se lista
                    if order[j] != "," and "{N,M}" in self.properties[order[j]].keys():
                        nameLista = order[j]
                        j += 1

                        #campos = int(self.properties[order[j]]["{N,M}"][1])


                    # se elemento da lista
                    if order[j] == ",":
                        if somaF or mediaF:
                            soma += int(v)
                            if mediaF:
                                counter += 1

                        else:
                            if i not in self.properties[nameLista].keys():
                                print("nao ha i, elemento: " + str(j))
                                self.properties[nameLista].update({i:[v]})
                            else:
                                print("ja ha i, elemento: " + str(j))
                                print("aux: " + str(j) + " "+ str(self.properties.get(nameLista).get(i)))
                                self.properties[nameLista][i] += [v]

                    # se param normal
                    else:
                        print("ENTREI NO PARAM NORMAL")
                        if somaF:
                            self.properties[nameLista].update({i: soma})
                            somaF = False
                            soma = 0

                        elif mediaF:
                            media = soma / counter
                            self.properties[nameLista].update({i: media})
                            soma = 0
                            counter = 0

                        else:
                            self.properties[order[j]].update({i: v})
                        nameLista = ""
                    j += 1
            i += 1