A = int(input())
M = int(input())

quantidadeMaxPessoas = 50

if (1 <= A <= quantidadeMaxPessoas) and (1 <= M <= quantidadeMaxPessoas):
    if A + M <= quantidadeMaxPessoas:
        print("S")
    else:
        print("N")
