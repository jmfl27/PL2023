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

       # if not entry[0].isdigit() or not entry[2].isdigit() or not entry[3].isdigit() or not entry[4].isdigit():
       #     return False

        #if int(entry[5]) != 1 or int(entry[5]) != 0:
        #    return False

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
        for k in self.properties["temDoença"]:
            if self.properties["temDoença"][k] == 1:
                if self.properties["sexo"][k] not in res:
                    res.update({self.properties["sexo"][k]:0})
                num = res[self.properties["sexo"][k]]
                res.update({self.properties["sexo"][k]:num+1})

        print("DOENCAS POR SEXO:\n")
        for k in res:
            print("Sexo " + str(k) + " tem " + str(res[k]) + " doentes.\n")
