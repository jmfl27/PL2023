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
        #res += "Pasta: " + str(self.properties["pasta"].get(id)) + "\n"
        res += "Data: " + str(self.properties["data"].get(id)) + "\n"
        res += "Nome: " + str(self.properties["nome"].get(id)) + "\n"
        res += "Pai: " + str(self.properties["pai"].get(id)) + "\n"
        res += "Mae: " + str(self.properties["mae"].get(id)) + "\n"
        res += "Observacoes: " + str(self.properties["obs"].get(id)) + "\n"
        print(res)


    def parseFile(self):
        file1 = open('processos.txt', 'r')
        lines = file1.readlines()

        i = 0
        val = 0

        # regex para linha valida
        model = re.compile(r'^(?P<pasta>[0-9]+)::(?P<data>\d{4}-\d{2}-\d{2})::(?P<nome>[a-zA-Z ]+)::(?P<pai>[a-zA-Z ]+)?::(?P<mae>[a-zA-Z ,]+)?::(?P<obs>.+)[:]+$')
        check = set()

        for l in lines:
            val += 1
            if l.strip():
                r = model.match(l)
                if r:
                    # se par de mae e filho ja existe na db, ignora essa linha
                    c = (r.group("nome"),r.group("mae"))
                    if c not in check:
                        self.properties["pasta"].update({i : r.group("pasta")})
                        self.properties["data"].update({i:r.group("data")})
                        self.properties["nome"].update({i: r.group("nome")})
                        self.properties["pai"].update({i: r.group("pai")})
                        self.properties["mae"].update({i: r.group("mae")})
                        if r.group("obs"):
                            self.properties["obs"].update({i:{r.group("obs")}})
                        check.add(c)
                        i += 1

        print("Li " + str(val) + " linhas.")
        print("Li " + str(i) + " linhas validas.")

