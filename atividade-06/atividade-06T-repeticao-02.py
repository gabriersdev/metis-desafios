# https://neps.academy/br/exercise/268
import math


def main():
    A, B, C, D = map(int, input().split())

    if (1 <= A <= 10 ** 8) and (1 <= B <= 10 ** 8) and (1 <= C <= 10 ** 8) and (1 <= D <= 10 ** 8):
        numerador = A * D + C * B
        denominador = B * D

        mdc = math.gcd(numerador, denominador)

        dividendo = numerador // mdc
        divisor = denominador // mdc

        print(dividendo, divisor)


if __name__ == "__main__":
    main()
