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

    def ex1(self):
        res = {}
        for d in self.properties["data"]:
            ano = re.match(r"\d{4}", self.properties["data"][d]).group()
            if ano not in res:
                res.update({ano:0})
            aux = res.get(ano)
            res.update({ano:aux + 1})

        print("-----------------------------------")
        print("|        PROCESSOS POR ANO        |")
        print("-----------------------------------")
        for r in res:
            print("|     " + str(r) + "      |      " + str(res.get(r)) + "       |")
            print("-----------------------------------")

    def printEx2(self,secs):
        print("-----------------------------------")
        print("|     TOP 5 NOMES POR SECULO      |")
        print("-----------------------------------")
        for s in secs:
            print("-----------------------------------")
            print("|            SECULO " + str(s) +"            |")
            print("-----------------------------------")
            print("|         NOMES PROPRIOS          |")
            print("-----------------------------------")
            for n in secs[s]["p"]:
                print(str(n) + " : " + str(secs[s]["p"][n]))
            print("-----------------------------------")
            print("|            APELIDOS             |")
            print("-----------------------------------")
            for n in secs[s]["a"]:
                print(str(n) + " : " + str(secs[s]["a"][n]))
            print("\n")

    def ex2(self):
        secs = {}
        for d in self.properties["data"]:
            ano = re.match(r"\d{4}", self.properties["data"][d]).group()
            sec = int(ano) // 100 + 1
            # ver se seculo ja esta no dicionario
            # { SECULO : { "p" : { {NOME PROPRIO : OCURRENCIAS} } , "a" : { APELIDO : OCURRENCIAS } }
            if sec not in secs:
                secs.update({ sec: { "p" : {},"a" : {} } })

            nomes = re.split(r"\s",self.properties["nome"][d])
            nomeP = nomes[0]

            # dict dos proprios
            if nomeP not in secs[sec]["p"]:
                secs[sec]["p"].update({nomeP:0})
            auxP = secs[sec]["p"][nomeP]
            secs[sec]["p"].update({nomeP:auxP+1})

            # dict dos apelidos
            if len(nomes) > 1:
                nomeA = nomes[len(nomes)-1]
                if nomeA not in secs[sec]["a"]:
                    secs[sec]["a"].update({nomeA: 0})
                auxA = secs[sec]["a"][nomeA]
                secs[sec]["a"].update({nomeA: auxA + 1})

        # ordenar
        print(secs)
        res = {}
        for s in secs:
            ordnP = dict(sorted(secs[s]["p"].items(), key=lambda x:x[1], reverse=True)[:5])
            ordnA = dict(sorted(secs[s]["a"].items(), key=lambda x:x[1], reverse=True)[:5])
            res.update({ s: { "p" : ordnP,"a" : ordnA } })

        self.printEx2(res)

    def trueStr(self,s):
        aux = str(s)[2:]
        return str(aux[:len(aux) - 2])

    def ex3(self):
        relacoes = {}
        for o in self.properties["obs"]:
            #EXPRESSAO REGEX BASE: ,+(.+?)(?=\.)
            #print(self.trueStr(self.properties["obs"][o]))
            regex = r",+(?P<parent>\w+\s?\w+\s?\w+?)(?=\.\s*(?i)Proc)"
            # A melhorar no futuro:
            # nao apanha os registos nem relacoes com mais de 4 palvaras, no entanto, as que apanha sao relacoes validas
            r = re.search(regex,self.trueStr(self.properties["obs"][o]))
            if r is not None:
                print(r.group("parent"))
                if r.group("parent") not in relacoes:
                    relacoes.update({r.group("parent") : 0})
                aux = relacoes[r.group("parent")]
                relacoes.update({r.group("parent"): aux + 1})

        print(relacoes)

        print("-----------------------------------")
        print("| FREQUENCIA DOS TIPOS DE RELAÇAO  |")
        print("-----------------------------------")
        for r in relacoes:
            print("|  "+str(r) + " :    " + str(relacoes.get(r)))
            print("-----------------------------------")

    def ex4(self):
        