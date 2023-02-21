# This is a sample Python script.
import parse

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():
    db = parse.Database()
    db.parseFile()
    sex = db.doencaPorSexo()
    age = db.doencaPorEscaloes()
    col = db.doencaPorColestrol()
    print("-----------------------------")
    print("|   Distribuição Por Sexo   |")
    print("-----------------------------")
    print("| Sexo | [total, com doença]|")
    print("-----------------------------")
    db.printTabelaS(sex)
    print()
    print("----------------------------------")
    print("|     Distribuição Por Idade     |")
    print("----------------------------------")
    db.printTabelaA(age)
    print()
    print("------------------------------------")
    print("|   Distribuição Por Colestrol     |")
    print("------------------------------------")
    db.printTabelaC(col)

if __name__ == "__main__":
    main()