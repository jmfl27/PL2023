from matplotlib import pyplot

class Database:
    def __init__(self):
        self.properties = {
            "idade": {},
            "sexo": {},
            "tensao": {},
            "colestrol": {},
            "batimento": {},
            "temDoença": {}
        }

    def __str__(self):
        return "Idades: " + str(self.properties["idade"]) + "\n" + \
               "Sexos: " + str(self.properties["sexo"]) + "\n" + \
               "Tensoes: " +str(self.properties["tensao"]) + "\n" + \
               "Colestrois: " +str(self.properties["colestrol"]) + "\n" + \
               "Batimentos: " +str(self.properties["batimento"]) + "\n" + \
               "TemDoencas: " +str(self.properties["temDoença"]) + "\n"

    def validEntry(self,entry):
        if len(entry) != 6:
            return False

        if not (entry[0].isdigit() and entry[2].isdigit() and entry[3].isdigit() and entry[4].isdigit()):
            return False

        #if entry[0] <= 0 and entry[2] <= 0 and entry[3] <= 0 and entry[4] <= 0:
        #    return False

        if int(entry[5]) != 1 and int(entry[5]) != 0:
            return False

        return True

    def parseFile(self):
        f = open("myheart.csv", "r")
        lines = f.readlines()

        i = -1
        for l in lines:
            # se nao for a linha identificadora
            if i != -1:
                l.strip()
                splited = l.split(",")
                # se a linha for válida
                if self.validEntry(splited):
                    self.properties["idade"].update({i:int(splited[0])})
                    self.properties["sexo"].update({i:splited[1]})
                    self.properties["tensao"].update({i:int(splited[2])})
                    self.properties["colestrol"].update({i:int(splited[3])})
                    self.properties["batimento"].update({i:int(splited[4])})
                    self.properties["temDoença"].update({i:int(splited[5])})

            i += 1

        print("Dei parse de " + str(i) + " linhas")
        print(str(self))

    def doencaPorSexo(self):
        res = {}
        for k in self.properties["sexo"]:
            if self.properties["sexo"][k] not in res:
                res.update({self.properties["sexo"][k]: [0, 0]})
            aux = res[self.properties["sexo"][k]]
            sex = aux[0] + 1
            num = aux[1]
            if self.properties["temDoença"][k] == 1:
                num += 1
            res.update({self.properties["sexo"][k]: [sex, num]})

        print("DOENCAS POR SEXO:\n")
        for k in res:
            print("Sexo " + str(k) + " possui " + str(res[k][1]) + " doentes em " + str(res[k][0]) + " indivíduos.\n")

        return res

    def minMaxdeCriterio(self,criterio):
        min = 0
        max = 0
        f = 1
        for k in self.properties[criterio]:
            if f == 1:
                max = self.properties[criterio][k]
                min = self.properties[criterio][k]
                f = 0

            if self.properties[criterio][k] > max:
                max = self.properties[criterio][k]

            if self.properties[criterio][k] < min:
                min = self.properties[criterio][k]

        #print(str(min) + " e " + str(max) + "\n")
        return (min,max)


    def gerarEscaloes(self,minMax,intervalo):
        res = []
        i, mx = minMax
        while (mx - i) >= intervalo:
            aux = (i, i + intervalo)
            res.append(aux)
            i = i + intervalo + 1

        if (mx-i) > 0:
            aux = (i, mx)
            res.append(aux)

        dic = {}

        for r in res:
            dic.update({r:0})

        #print(dic)
        return dic

    def doencaPorEscaloes(self):
        escaloes = self.gerarEscaloes(self.minMaxdeCriterio("idade"),4)
        #print(escaloes)
        for k in self.properties["idade"]:
            if self.properties["temDoença"][k] == 1:
                for e in escaloes:
                    if e[0] <= self.properties["idade"][k] <= e[1]:
                        n = escaloes[e]
                        escaloes.update({e:n+1})
                        break

        print(str(escaloes) + "\n")

        return escaloes

    """
        soma = 0
        for e in escaloes:
            soma = soma + escaloes[e]

        print(soma)
    """

    def doencaPorColestrol(self):
        intervalos = self.gerarEscaloes(self.minMaxdeCriterio("colestrol"),10)
        #print(intervalos)
        for k in self.properties["colestrol"]:
            if self.properties["temDoença"][k] == 1:
                for i in intervalos:
                    if i[0] <= self.properties["colestrol"][k] <= i[1]:
                        n = intervalos[i]
                        intervalos.update({i: n + 1})
                        break

        print(str(intervalos) + "\n")

        return intervalos

    """
        soma = 0
        for e in intervalos:
            soma = soma + intervalos[e]

        print(soma)
    """

    def printTabelaS(self,dist):
        for key in dist:
            print("-----------------------------")
            string = '|'
            comp = int((13 - len(key)) / 2)
            for i in range(comp):
                string += ' '
            string += str(key)
            for i in range(comp):
                string += ' '
            string += "|"
            comp = 13 - len(str(dist[key]))
            if comp % 2 != 0:
                comp = int(comp / 2)
                comp1 = comp + 1
            else:
                comp = int(comp / 2)
                comp1 = comp
            for i in range(comp):
                string += ' '
            string += str(dist[key])
            for i in range(comp1):
                string += ' '
            print(string + "|")
        print("-----------------------------")

    def printTabelaA(self,dist):
        for key in dist:
            print("----------------------------------")
            string = '|'
            comp = int((13 - len(key)) / 2)
            for i in range(comp):
                string += ' '
            string += str(key)
            for i in range(comp):
                string += ' '
            string += "|"
            comp = 13 - len(str(dist[key]))
            if comp % 2 != 0:
                comp = int(comp / 2)
                comp1 = comp + 1
            else:
                comp = int(comp / 2)
                comp1 = comp
            for i in range(comp):
                string += ' '
            string += str(dist[key])
            for i in range(comp1):
                string += ' '
            print(string + "|")
        print("----------------------------------")

    def printTabelaC(self,dist):
        for key in dist:
            print("------------------------------------")
            string = '|'
            comp = int((13 - len(key)) / 2)
            for i in range(comp):
                string += ' '
            string += str(key)
            for i in range(comp):
                string += ' '
            string += "|"
            comp = 13 - len(str(dist[key]))
            if comp % 2 != 0:
                comp = int(comp / 2)
                comp1 = comp + 1
            else:
                comp = int(comp / 2)
                comp1 = comp
            for i in range(comp):
                string += ' '
            string += str(dist[key])
            for i in range(comp1):
                string += ' '
            print(string + "|")
        print("------------------------------------")

    def criaGrafico(self, param, ttl, xname, yname, col, sexo):
        if sexo:
            x = list(param.keys())
            y = []
            for t in param.values():
                y.append(t[1])
                y = list(y)
        else:
            x = []
            for t in param.keys():
                aux = "[" + str(t[0]) + "-" + str(t[1]) + "]"
                x.append(aux)
            y = list(param.values())

        pyplot.bar(x,y,color = col)
        pyplot.xlabel(xname)
        pyplot.ylabel(yname)
        pyplot.title(ttl)
        pyplot.show()
