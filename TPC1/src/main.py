# This is a sample Python script.
import tpc1

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():
    db = tpc1.Database()
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
    db.criaGrafico(sex,"Distribuição da doença por Sexo","Género","Número de pessoas com a doença","green",True)
    print()
    print("----------------------------------")
    print("|     Distribuição Por Idade     |")
    print("----------------------------------")
    db.printTabelaA(age)
    db.criaGrafico(age, "Distribuição da doença por Idade", "Escalões Etários", "Número de pessoas com a doença","red",False)
    print()
    print("------------------------------------")
    print("|   Distribuição Por Colestrol     |")
    print("------------------------------------")
    db.printTabelaC(col)
    db.criaGrafico(col, "Distribuição da doença por Colestrol", "Intervalos de Colestrol", "Número de pessoas com a doença", "blue",False)

if __name__ == "__main__":
    main()