# This is a sample Python script.
import parse

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():
    db = parse.Database()
    db.parseFile()
    db.doencaPorSexo()
    db.doencaPorEscaloes()
    db.doencaPorColestrol()

if __name__ == "__main__":
    main()