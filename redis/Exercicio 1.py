# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 15:23:52 2020

@author: adria
"""

import redis
r = redis.Redis(host='localhost', port=6379, db=1)

n_users = 50

# model user:01 -> name: "user01", bcartela: "cartela:01", bscore: "score:01"
# hset(name, key=None, value=None, mapping=None)[source]
# Set key to value within hash name, Use mappings keyword args to set multiple key/value pairs for a hash name.
# Returns the number of fields that were added.


for i in range(n_users):
    
    
    r.hset('user%02d'% (i+1), 'name': 'user%02d'% (i+1))
    r.hset('user%02d'% (i+1), 'bcartela': 'cartela:%02d'% (i+1))
    r.hset('user%02d'% (i+1), 'bscore': 'score:%02d'% (i+1))
    
    r.srandmember('cartela:%02d'% (i+1), number=15)
    
    #r.set()
    
    


#o que fazer:
    # criar hash para 50 pessoas
    # usar SRANDMEMBER de 1 a 99 para criar as cartelas com 15 numeros
    # (atrbuir ao valor cartela01 etc)
    # set score sera para pontuacao de cada usuario
    # criar uma lista com as pedras do jogo - retirando uma a uma
    # contabiliza e adiciona o score a cada jogador
    # quem acertar 15 numeros primeiro vence