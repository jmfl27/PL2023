import tpc3

def main():

    db = tpc3.Database()
    db.parseFile()

    print("")
    print("|                                TPC 3                                             |")
    print("1 - Frequência de processos por ano")
    print("2 - Frequência de nomes próprios e apelidos por séculos e apresenta os 5 mais usados")
    print("3 - Frequência dos vários tipos de relação: irmão, sobrinho, etc.")
    print("4 - Primeiros 20 registos escritos num ficheiro em formato json")
    print("q - Sair")
    choice = ""
    print("")

    while(choice != "q"):
        choice = input("Escolha o exercicio: ")
        inp = int(choice)
        if inp == 1:
            db.ex1()

        elif inp == 2:
            db.ex2()

        elif inp == 3:
            db.ex3()

        elif inp == 4:
            db.ex4(20)
    quit()

if __name__ == "__main__":
        main()