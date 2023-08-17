import Imagem

matriz = Imagem.getMatrizImagemCinza("olhos.jpg")

num_lin = len(matriz)
num_col = len(matriz[0])

negativa = []

## metodo append
for i in range(num_lin):
    negativa.append([0]*num_col)


for i in range(num_lin):
    for j in range(num_col):
        negativa [i][j] = 255 - matriz[i][j]


Imagem.salvaImagemCinza("olhos.jpg")        
