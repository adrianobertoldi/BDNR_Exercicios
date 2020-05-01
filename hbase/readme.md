# Exercícios HBase

abrir terminal docker e executar: 
docker start hbase-furb

abrir outro terminal e executar: 
docker exec -it hbase-furb /bin/bash
hbase shell

### Exercício 1)


#### 1. Crie a tabela com 2 famílias de colunas:
##### a. personal-data
##### b. professional-data
#### 2. Importe o arquivo via linha de comando

#### 1. Adicione mais 2 italianos mantendo adicionando informações como data de nascimento nas informações pessoais e um atributo de anos de experiência nas informações profissionais;
```
put 'italians', '11', 'personal-data:name',  'Enzo Ferrari'
put 'italians', '11', 'personal-data:city',  'Maranello'
put 'italians', '11', 'personal-data:born',  '01-01-1920'
put 'italians', '11', 'professional-data:role',  'Mecanico'
put 'italians', '11', 'professional-data:salary',  '100000'
put 'italians', '11', 'professional-data:yearsExperience',  '50'
put 'italians', '12', 'personal-data:name',  'Ferrucio Lamborghini'
put 'italians', '12', 'personal-data:city',  'Sicilia'
put 'italians', '12', 'personal-data:born',  '01-01-1922'
put 'italians', '12', 'professional-data:role',  'Mecanico'
put 'italians', '12', 'professional-data:salary',  '90000'
put 'italians', '12', 'professional-data:yearsExperience',  '48'

```
#### 2. Adicione o controle de 5 versões na tabela de dados pessoais.
```
 alter 'italians', {NAME => 'personal-data',VERSIONS => '5'}

```
#### 3. Faça 5 alterações em um dos italianos;
```
hbase(main):057:0> put ???table name???,???row ???,'Column family:column name',???new value???
PS C:\WINDOWS\syste
hbase(main):002:0* put 'italians', '11', 'personal-data:city', 'Modena'
Took 0.9714 seconds
hbase(main):003:0> put 'italians', '11', 'personal-data:born', '18-02-1898'
Took 0.0071 seconds
hbase(main):004:0> put 'italians', '11', 'personal-data:name',  'Enzo Anselmo Ferrari'
Took 0.0192 seconds
hbase(main):006:0* put 'italians', '11', 'personal-data:name',  'Enzo Anselmo Giuseppe Ferrari'
Took 0.0076 seconds
hbase(main):007:0> put 'italians', '11', 'personal-data:name',  'Enzo Anselmo Giuseppe Maria Ferrari'
Took 0.0057 seconds

```
#### 4. Com o operador get, verifique como o HBase armazenou o histórico.
```
hbase(main):008:0> get 'italians', '11', {COLUMN => 'personal-data:name', VERSIONS => 5}
COLUMN                          CELL
 personal-data:name             timestamp=1588293107826, value=Enzo Anselmo Giuseppe Maria Ferrari
 personal-data:name             timestamp=1588293093105, value=Enzo Anselmo Giuseppe Ferrari
 personal-data:name             timestamp=1588293070720, value=Enzo Anselmo Ferrari
 personal-data:name             timestamp=1588291375805, value=Enzo Ferrari
1 row(s)
Took 0.1352 seconds

```

#### 5. Utilize o scan para mostrar apenas o nome e profissão dos italianos.
```
hbase(main):014:0> scan 'italians', {COLUMNS =>['personal-data:name','professional-data:role']}
ROW                             COLUMN+CELL
 1                              column=personal-data:name, timestamp=1588290623396, value=Paolo Sorrentino
 1                              column=professional-data:role, timestamp=1588290623557, value=Gestao Comercial
 10                             column=personal-data:name, timestamp=1588290625424, value=Giovanna Caputo
 10                             column=professional-data:role, timestamp=1588290625509, value=Comunicacao Institucional
 11                             column=personal-data:name, timestamp=1588293107826, value=Enzo Anselmo Giuseppe Maria Fe
                                rrari
 11                             column=professional-data:role, timestamp=1588291375907, value=Mecanico
 12                             column=personal-data:name, timestamp=1588291376000, value=Ferrucio Lamborghini
 12                             column=professional-data:role, timestamp=1588291376126, value=Mecanico
 2                              column=personal-data:name, timestamp=1588290623708, value=Domenico Barbieri
 2                              column=professional-data:role, timestamp=1588290623816, value=Psicopedagogia
 3                              column=personal-data:name, timestamp=1588290623917, value=Maria Parisi
 3                              column=professional-data:role, timestamp=1588290624022, value=Optometria
 4                              column=personal-data:name, timestamp=1588290624144, value=Silvia Gallo
 4                              column=professional-data:role, timestamp=1588290624272, value=Engenharia Industrial Made
                                ireira
 5                              column=personal-data:name, timestamp=1588290624417, value=Rosa Donati
 5                              column=professional-data:role, timestamp=1588290624528, value=Mecatronica Industrial
 6                              column=personal-data:name, timestamp=1588290624626, value=Simone Lombardo
 6                              column=professional-data:role, timestamp=1588290624711, value=Biotecnologia e Bioquimica
 7                              column=personal-data:name, timestamp=1588290624838, value=Barbara Ferretti
 7                              column=professional-data:role, timestamp=1588290624935, value=Libras
 8                              column=personal-data:name, timestamp=1588290625033, value=Simone Ferrara
 8                              column=professional-data:role, timestamp=1588290625163, value=Engenharia de Minas
 9                              column=personal-data:name, timestamp=1588290625273, value=Vincenzo Giordano
 9                              column=professional-data:role, timestamp=1588290625350, value=Marketing
12 row(s)

```
#### 6. Apague os italianos com row id ímpar
```
base(main):015:0> deleteall 'italians', 1
Took 0.0167 seconds
hbase(main):016:0> deleteall 'italians', 3
Took 0.0043 seconds
hbase(main):017:0> deleteall 'italians', 5
Took 0.0038 seconds
hbase(main):018:0> deleteall 'italians', 7
Took 0.0050 seconds
hbase(main):019:0> deleteall 'italians', 9
Took 0.0039 seconds
hbase(main):020:0> deleteall 'italians', 11
Took 0.0040 seconds

```
#### 7. Crie um contador de idade 55 para o italiano de row id 5
```
hbase(main):033:0> create 'newcounter', 'id5', 'personal-data'
Created table newcounter
Took 0.9271 seconds
=> Hbase::Table - newcounter
hbase(main):034:0> incr 'newcounter', 'id5', 'personal-data', 55
COUNTER VALUE = 55

```
#### 8. Incremente a idade do italiano em 1
```
hbase(main):035:0> incr 'newcounter', 'id5', 'personal-data', 1
COUNTER VALUE = 56
Took 0.0061 seconds

```
