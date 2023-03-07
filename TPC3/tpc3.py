import re

class Database:
    def __init__(self):
        self.properties = {
            "pasta": {},
            "data": {},
            "nome" : {},
            "pai": {},
            "mae": {},
            "obs": {}
        }

    def __str__(self):
        return "Pasta: " + str(self.properties["pasta"]) + "\n" + \
               "Data: " + str(self.properties["data"]) + "\n" + \
               "Nome: " + str(self.properties["nome"]) + "\n" + \
               "Pai: " + str(self.properties["pai"]) + "\n" + \
               "Mae: " + str(self.properties["mae"]) + "\n" + \
               "Observações: " + str(self.properties["obs"]) + "\n"

    def printPessoa(self,id):
        res = ""
        """
        for p in self.properties["pasta"].values():
            if p[0] == id:
                res += "Pasta: " + str(p[1]) + "\n"
                break

        for p in self.properties["data"].values():
            if p[0] == id:
                res += "Data: " + str(p[1]) + "\n"
                break

        for p in self.properties["nome"].values():
            if p[0] == id:
                res += "Nome: " + str(p[1]) + "\n"
                break

        for p in self.properties["pai"].values():
            if p[0] == id:
                res += "Pai: " + str(p[1]) + "\n"
                break

        for p in self.properties["mae"].values():
            if p[0] == id:
                res += "Mae: " + str(p[1]) + "\n"
                break

        for p in self.properties["obs"].values():
            if p[0] == id:
                res += "Observacoes: " + str(p[1]) + "\n"
                break
    """
        res += "Pasta: " + str(self.properties["pasta"].get(id)) + "\n"
        res += "Data: " + str(self.properties["data"].get(id)) + "\n"
        res += "Nome: " + str(self.properties["nome"].get(id)) + "\n"
        res += "Pai: " + str(self.properties["pai"].get(id)) + "\n"
        res += "Mae: " + str(self.properties["mae"].get(id)) + "\n"
        res += "Observacoes: " + str(self.properties["obs"].get(id)) + "\n"
        print(res)

    def notExists(self,nome,mae):
        if nome in self.properties["nome"].values():
            



    def parseFile(self):
        file1 = open('processos.txt', 'r')
        lines = file1.readlines()
        i = 0
        for l in lines:
            splited = re.split(r"::",l)
                if self.notExists(splited[2],splited[4]):
                self.properties["pasta"].update({i: splited[0]})
                self.properties["data"].update({i: splited[1]})
                self.properties["nome"].update({i: splited[2]})
                self.properties["pai"].update({i: splited[3]})
                self.properties["mae"].update({i: splited[4]})
                if splited[5]:
                    self.properties["obs"].update({i:{splited[5]}})
                i += 1



