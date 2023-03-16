import tpc4

def main():

    db = tpc4.Database()
    cam = input("Insira o caminho do ficheiro .csv que pretende transformar em .json: ")
    db.parseLines(cam)
    print(db.properties)
    #alunos2.txt

if __name__ == "__main__":
        main()