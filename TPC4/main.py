import re

import tpc4

def main():

    db = tpc4.Database()
    cam = input("Insira o caminho do ficheiro .csv que pretende transformar em .json: ")
    linhas = db.parseLines(cam)
    print(db.properties)
    #finalF = re.sub(r'\.csv',".json",cam)
    finalF = re.sub(r'\.txt', ".json", cam)
    db.criaJson(finalF,linhas)
    #alunos2.txt

if __name__ == "__main__":
        main()