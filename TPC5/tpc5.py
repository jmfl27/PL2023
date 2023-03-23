import re
import ply.lex as lex

class Cabine:
    def __init__(self):
        self.ativa = False
        self.saldo = 0

    def saldo(self,line):
        # moedas validas: euro , centimos
        validas = [{"e": [1, 2]},{"c": [1, 2, 5, 10, 20, 50]}]

        moedas = re.findall(r'(?:(\d+)([cCeE]))',line)

        for m in moedas:
            if m[1] in "cC":
                if m[0] in validas["c"]:
                    self.saldo += int(m[0])
                else:
                    print("Moeda Inválida: " + m[0])

            elif m[1] in "eE":
                if m[0] in validas["e"]:
                    self.saldo += int(m[0]) * 100
                else:
                    print("Moeda Inválida: " + m[0])

            else: print("Moeda Inválida: " + m[0])

        print("Saldo = " + self.saldo())

    def chamada(self,inicio):
        # RECEBER inicio da chamada e fazer custo conforme

def main():
    rgxLev = r'^LEVANTAR$'
    rgxPou = r'^POUSAR$'
    rgxAbort = r'^ABORTAR$'
    #rgxMoeda = r'MOEDA+\s((\d+[ce][,\.]\s*)+)'
    rgxMoeda = r'^MOEDA((?:\s+\d+[ce][,\.])+)$'
    rgxTBloq= r'^T=(601|641)(\d{6})$'
    rgxTInter = r'^T=(00)(\d{9,13})$'
    rgxTNacio = r'^T=(2)(\d{8})$'
    rgxTVerde = r'^T=(800)(\d{6})$'
    rgxTAzul = r'^T=(808)(\d{6})$'

    print("ihihihi")

if __name__ == "__main__":
    main()