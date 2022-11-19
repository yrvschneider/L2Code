largura_X = float(input('Largura da Sala: ')) # Entrada da largura da sala
comprimento_Y = float(input('Cumprimento da Sala: ')) # Entrada do cumprimento da sala
trajeto = str(input('Digite o trajeto: ')) # Entrada do trajeto que o robo tera que fazer
rotacao = { 90 : 'O', 180 : 'N', 270 : 'L', 0 : 'S'} # Angulo para se basear no trajeto que o robo tem que fazer
posicao = 180 # Posição que o robo já vai começar, que é virado para o Norte
roboX = 0 # Posição 0 do Robo
roboY = 0 # Posição 0 do Robo

for i in range(len(trajeto)): # Loop que vai verificar quantos index tem o trajeto para repetir.
    # Vai verificar se o i == D e somar mais 90 para rotacionar o robo
    if trajeto[i] == 'D':
        posicao += 90
    # Vai verificar se o i == E e subtrair 90 da rotação do robo
    if trajeto[i] == 'E':
        posicao -= 90
    # Vai verificar se o i == F para seguir em frente
    if trajeto[i] == 'F':
        # Rotação for igual posição atual % 360 == N e RoboY + 1 for menor que cumprimento, vai somar + 1.
        if rotacao[posicao%360] == 'N' and (roboY + 1) < comprimento_Y:
            roboY += 1
        # Rotação for igual posição atual % 360 == S e RoboY - 1 for maior ou igual a 0, vai subtrair - 1.
        if rotacao[posicao%360] == 'S' and (roboY - 1) >= 0:
            roboY -= 1
        # Rotação for igual posição atual % 360 == L e RoboY + 1 for menor que cumprimento, vai somar + 1.
        if rotacao[posicao%360] == 'L' and (roboX + 1) < largura_X:
            roboX += 1
        # Rotação for igual posição atual % 360 == O e RoboY - 1 for maior ou igual a 0, vai subtrair - 1.
        if rotacao[posicao%360] == 'O' and (roboX - 1) >= 0:
            roboX -= 1
    # Vai verificar se o i == T para andar pra trás
    if trajeto[i] == 'T':
        # Rotação for igual posição atual % 360 == N e RoboY - 1 for maior ou igual a 0, vai subtrair - 1.
        if rotacao[posicao%360] == 'N' and (roboY - 1) >= 0:
            roboY -= 1
        # Rotação for igual posição atual % 360 == S e RoboY + 1 for menor que cumprimento, vai somar + 1.
        if rotacao[posicao%360] == 'S' and (roboY + 1) < comprimento_Y:
            roboY += 1
        # Rotação for igual posição atual % 360 == L e RoboY - 1 for maior ou igual a 0, vai subtrair - 1.
        if rotacao[posicao%360] == 'L' and (roboX - 1) >= 0:
            roboX -= 1
        # Rotação for igual posição atual % 360 == O e RoboY + 1 for menor que cumprimento, vai somar + 1.
        if rotacao[posicao%360] == 'O' and (roboX + 1) < largura_X:
            roboX += 1
            
# Imprimir o resultado
print('{} {} {}'.format(rotacao[posicao%360], roboX, roboY))