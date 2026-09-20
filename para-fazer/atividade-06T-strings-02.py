# https://neps.academy/br/exercise/118

def main():
    # TEM que ter 1 vogal minúscula, sem acentuação

    string = input()
    vogais = ["a", "e", "i", "o", "u"]

    vogaisEncontradas = ""

    if len(string) > 50:
        return

    for letra in list(string):
        if letra in vogais:
            vogaisEncontradas += letra

    if len(vogaisEncontradas) == 0:
        print("N")
        return

    vogaisInvertidas = ""
    for letra in reversed(vogaisEncontradas):
        vogaisInvertidas += letra

    if vogaisEncontradas == vogaisInvertidas:
        print("S")
    else:
        print("N")


if __name__ == "__main__":
    main()
