import re
import ply.lex as lex

class Cabine:
    def __init__(self):
        self.ativa = False
        self.saldo = 0

    def printSaldo(self):
        return str((self.saldo - self.saldo%100)//100) + "e" + str(self.saldo%100) + "c"

    def aumentaSaldo(self,line):
        # moedas validas: euro , centimos
        validas = {"e": [1, 2],"c": [1, 2, 5, 10, 20, 50]}

        moedas = re.findall(r'(?:(\d+)([cCeE]))',line)

        for m in moedas:
            if m[1] in "cC":
                if int(m[0]) in validas["c"]:
                    self.saldo += int(m[0])
                else:
                    print("Moeda Inválida: " + m[0])

            elif m[1] in "eE":
                if int(m[0]) in validas["e"]:
                    self.saldo += int(m[0]) * 100
                else:
                    print("Moeda Inválida: " + m[0])

            else: print("Moeda Inválida: " + m[0])

        print("Saldo = " + self.printSaldo())

    def chamada(self,numero):
        rgxTAll = [r'^T=(601|641)(\d{6})$',
                   r'^T=(00)(\d{9,13})$',
                   r'^T=(2)(\d{8})$',
                   r'^T=(800)(\d{6})$',
                   r'^T=(808)(\d{6})$']

        found = []
        """
        rgxTBloq = r'^T=(601|641)(\d{6})$'
        rgxTInter = r'^T=(00)(\d{9,13})$'
        rgxTNacio = r'^T=(2)(\d{8})$'
        rgxTVerde = r'^T=(800)(\d{6})$'
        rgxTAzul = r'^T=(808)(\d{6})$'
        """

        for r in rgxTAll:
            found = re.findall(r,numero)
            if found != []: break

        if found == []:
            print("Esse número não é permitido neste telefone. Por favor insira outro número. Saldo Atual: " + self.printSaldo())
        else:
            inicio = found[0][0]
            match inicio:
                case "00":
                    if self.saldo >= 150:
                        self.saldo -= 150
                        print("Chamada efetuada com sucesso! Saldo Atual: " + self.printSaldo())
                    else:
                        print("Saldo Insuficinte! Insira mais dinheiro. Saldo Atual: " + self.printSaldo())
                case "2":
                    if self.saldo >= 25:
                        self.saldo -= 25
                        print("Chamada efetuada com sucesso! Saldo Atual: " + self.printSaldo())
                    else:
                        print("Saldo Insuficinte! Insira mais dinheiro. Saldo Atual: " + self.printSaldo())
                case "800":
                        print("Chamada efetuada com sucesso! Saldo Atual: " + self.printSaldo())
                case "808":
                    if self.saldo >= 10:
                        self.saldo -= 10
                        print("Chamada efetuada com sucesso! Saldo Atual: " +self.printSaldo())
                    else:
                        print("Saldo Insuficinte! Insira mais dinheiro. Saldo Atual: " + self.printSaldo())
                case _:
                    print("Esse número não é permitido neste telefone. Por favor insira outro número. Saldo Atual: " + self.printSaldo())

    def troco(self):
        validas = {"e": [2, 1], "c": [50, 20, 10, 5, 2, 1]}
        res = {}

        while self.saldo != 0:
            if self.saldo >= 100:
                for m in validas["e"]:
                    while self.saldo >= (m * 100):
                        self.saldo -= m*100
                        if str(m) + "e" not in res.keys():
                            res[str(m) + "e"] = 1
                        else:
                            res[str(m) + "e"] = res[str(m) + "e"] + 1

            for m in validas["c"]:
                while self.saldo >= m:
                    self.saldo -= m
                    if str(m) +"c" not in res.keys():
                        res[str(m) + "c"] = 1
                    else:
                        res[str(m) + "c"] = res[str(m) + "c"] + 1

            if res == {}:
                print("Troco = 0; Volte Sempre!")
            else:
                s = "Troco = "
                for m in res:
                    s += str(res[m]) + "x" + m + ","
                s = s[:-1] + ";"
                s += " Volte Sempre!"

                print(s)

        """      
        while self.saldo != 0:
            while self.saldo >= 200:
                self.saldo -= 200
                if "2e" not in res.keys():
                    res["2e"] = 1
                else:
                    res["2e"] = res["2e"] + 1
            while self.saldo >= 100:
                self.saldo -= 100
                if "1e" not in res.keys():
                    res["1e"] = 1
                else:
                    res["1e"] = res["1e"] + 1
            while self.saldo >= 50:
                self.saldo -= 50
                if "50c" not in res.keys():
                    res["50c"] = 1
                else:
                    res["2e"] = res["2e"] + 1
            while self.saldo >= 20:
                self.saldo -= 20
                if "20c" not in res.keys():
                    res["20c"] = 1
                else:
                    res["20c"] = res["20c"] + 1
            while self.saldo >= 10:
                self.saldo -= 10
                if "10c" not in res.keys():
                    res["10c"] = 1
                else:
                    res["10c"] = res["10c"] + 1
            while self.saldo >= 5:
                self.saldo -= 5
                if "5c" not in res.keys():
                    res["5c"] = 1
                else:
                    res["5c"] = res["5c"] + 1
            while self.saldo >= 2:
                self.saldo -= 2
                if "2c" not in res.keys():
                    res["2c"] = 1
                else:
                    res["2c"] = res["2c"] + 1
            while self.saldo >= 1:
                self.saldo -= 1
                if "1c" not in res.keys():
                    res["1c"] = 1
                else:
                    res["1c"] = res["1c"] + 1
    """

def main():
    rgxLev = r'^LEVANTAR$'
    rgxPou = r'^POUSAR$'
    rgxAbort = r'^ABORTAR$'
    #rgxMoeda = r'MOEDA+\s((\d+[ce][,\.]\s*)+)'
    rgxMoeda = r'^MOEDA((?:\s+\d+[cCeE][,\.])+)$'
    rgxT = r'^T=\d+'

    tele = Cabine()

    while True:
        action = input()
        if re.match(rgxAbort, action) is not None:
            tele.ativa = False
            print("Abortado com sucesso")
            break

        if tele.ativa == False:
            if re.match(rgxLev, action) is None:
                print("Operação inválida. Por favor, \"LEVANTAR\" o telefone primeiro")
            else:
                tele.ativa = True
                print("Introduza moedas.")

        elif tele.ativa == True:
            if re.match(rgxPou,action) is not None:
                tele.troco()
                break
            elif re.match(rgxMoeda,action) is not None:
                tele.aumentaSaldo(action)
            elif re.match(rgxT,action) is not None:
                tele.chamada(action)
            else:
                print("Operação não suportada! Por favor, insira uma operação válida.")

    print("ihihihi")

if __name__ == "__main__":
    main()