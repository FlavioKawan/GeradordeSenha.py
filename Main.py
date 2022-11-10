import random , string

tamanho = int(input('Digite o tamanho da senha maior que 4: '))
sen = string.ascii_letters + string.digits + '@#$%&*'
aleatorio = random.SystemRandom()
if(tamanho >= 4):
    print('' .join(aleatorio.choice(sen)for l in range(tamanho)))
else:
    print("senha menor que 4")