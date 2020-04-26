# -*- coding: utf-8 -*-

import redis
import random

r = redis.Redis(host='localhost', port=6379, db=1, decode_responses=True) #decode_responses=True

n_users = 50

r.flushdb()

# model user:01 -> name: "user01", bcartela: "cartela:01", bscore: "score:01"
# hset(name, key=None, value=None, mapping=None)[source]
# Set key to value within hash name, Use mappings keyword args to set multiple key/value pairs for a hash name.
# Returns the number of fields that were added.

# Iniciar cmd com:
# cd c:\\ProgramData\chocolatey\lib\redis-64
# redis-server.exe
# redis-cli.exe

for i in range(1,99): # gera lista com cada valor possivel (cartela)
    r.sadd('listaNumeros', str(i))

for i in range(n_users):
    r.hset('user%02d'% (i+1), 'name', 'user%02d'% (i+1))
    r.hset('user%02d'% (i+1), 'bcartela', 'cartela:%02d'% (i+1))
    r.hset('user%02d'% (i+1), 'cartela:%02d'% (i+1), str(r.srandmember('listaNumeros', number=15)))
    r.hset('user%02d'% (i+1), 'bscore', 'score:%02d'% (i+1))
    #r.hset('user%02d'% (i+1), 'score:%02d'% (i+1), '0')
    
    #r.srandmember('cartela:%02d'% (i+1), number=15) # name tem que ser uma lista de números
    
    #r.set()
    
    ##### hget(cartela ....)
    
sorteioNumeros = random.sample(range(1,99),98) 

for j in range(len(sorteioNumeros)):
    numSorteado = str(sorteioNumeros[j])
    for i in range(n_users):
        #print (r.hget('user%02d'% (i+1),'cartela:%02d'% (i+1)), numSorteado)
        cartelaUsuario = r.hget('user%02d'% (i+1),'cartela:%02d'% (i+1))
        if numSorteado in cartelaUsuario:
            print ('Ponto!')
            r.hincrby('user%02d'% (i+1), 'score:%02d'% (i+1), 1)            
            pontuacao = r.hget('user%02d'% (i+1), 'score:%02d'% (i+1))
            print (type(pontuacao))
            if pontuacao == str(15):
                print ('Bingo! O candidato {} venceu!'.format(i))
                print ('Pontuacao do candidato {} é {}'.format(i, pontuacao))
                break
        

#o que fazer:
        # criar hash para 50 pessoas
        # usar SRANDMEMBER de 1 a 99 para criar as cartelas com 15 numeros
        # (atrbuir ao valor cartela01 etc)
    # set score sera para pontuacao de cada usuario
        # criar uma lista com as pedras do jogo - retirando uma a uma
    # contabiliza e adiciona o score a cada jogador
    # quem acertar 15 numeros primeiro vence