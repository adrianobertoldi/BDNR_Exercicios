### Redisingo

Para rodar esse código, foi utilizado o Python 3 em ambiente Anaconda juntamente com o módulo Redis para python. Tudo isso em um computador com windows 10.

Além disso, o Redis deve estar instalado na máquina e tanto o server (redis-server.exe) quanto o client (redis-cli.exe) devem estar rodando em terminais distintos.

#### Código Python

```python

import redis
import random

r = redis.Redis(host='localhost', port=6379, db=1, decode_responses=True) #decode_responses=True
n_users = 50
r.flushdb() # Limpa a base de dados em cada inicializacao (evitar duplicidade ou dados errados)


for i in range(1,99): # gera o set com os numeros possiveis para serem adicionados as cartelas
    r.sadd('listaNumeros', str(i))

for i in range(n_users): # gera as hashs de cada usuario
    r.hset('user%02d'% (i+1), 'name', 'user%02d'% (i+1))
    r.hset('user%02d'% (i+1), 'bcartela', 'cartela:%02d'% (i+1)) # cria a cartela para determinado usuario
    r.hset('user%02d'% (i+1), 'cartela:%02d'% (i+1), str(r.srandmember('listaNumeros', number=15))) # atribui 15 numeros aleatorios do set anterior para as cartelas de cada usuario
    r.hset('user%02d'% (i+1), 'bscore', 'score:%02d'% (i+1)) # o campo para pontuacao
  
            
def sorteio(): # funcao para determinar o sorteio
    sorteioNumeros = random.sample(range(1,99),98) # cria conjunto de numeros randomicos de 1 a 99
    for j in range(len(sorteioNumeros)):
        numSorteado = str(sorteioNumeros[j]) # sorteia um numero por vez
        for i in range(n_users):
            cartelaUsuario = r.hget('user%02d'% (i+1),'cartela:%02d'% (i+1)) #abre a cartela de cada usuario
            if numSorteado in cartelaUsuario: # verifica se o numero sorteado esta na cartela
                r.hincrby('user%02d'% (i+1), 'score:%02d'% (i+1), 1) # se o numero estiver, incrementa 1 ao campo score          
                pontuacao = r.hget('user%02d'% (i+1), 'score:%02d'% (i+1)) # le a pontuacao do usuario
                if pontuacao == str(15): # verifica se a pontuacao chegou a 15, se chegou entao tem-se o vencedor
                    print ('Bingo!', cartelaUsuario)
                    return i+1
vencedor = sorteio()
print ('Vencedor =', 'user%02d'% vencedor)

```

Saída terminal:
![Saída terminal](https://octodex.github.com/images/yaktocat.png)