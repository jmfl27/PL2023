class Somador:
    def __init__(self):
        self.soma = 0
        self.on = True

    def parseLine(self,line):
        num = False
        hasO = False
        on = ["on","ON","On","oN"]
        off = ["off","OFF","oFF","ofF","Off","OFf","OfF","oFf"]
        s = ""
        line += "/n"
        for d in line:
            # se for um digito, guarda-o no leitor
            if d.isdigit():
                num = True
                s += d
            # caso seja um carater
            else:
                # se não for um digito e caso se tenha começado a ler um numero antes, soma-o (caso on) e dá reset ao leitor
                if num:
                    if self.on:
                        self.soma += int(s)
                    num = False
                    s = ""

                # se for igual, imprime o resultado atual da soma
                if d == "=":
                    print("A soma é: " + str(self.soma))

                # se detetar um o, assinala como possivel on ou off
                if d == "o" or d == "O":
                    hasO = True

                # se tiver detetado um o e consequentemente on ou off, muda o somador para tal
                if hasO:
                    s += d
                    if len(s) == 2 and s in on:
                        self.on = True
                        hasO = False
                        s = ""
                    if len(s) == 3:
                        if s in off:
                            self.on = False
                        hasO = False
                        s = ""
