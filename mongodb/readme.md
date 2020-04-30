# Exercícios MongoDB

Iniciar comando em terminal mongod (servidor)
Iniciar em outro terminal mongo

### Exercício 1)

#### 1) Adicione outro Peixe e um Hamster com nome Frodo:

> db.pets.insert({name: "Nemo", species: "Peixe"})
WriteResult({ "nInserted" : 1 })
> db.pets.insert({name: "Frodo", species: "Hamster"})
WriteResult({ "nInserted" : 1 })

#### 2) Faça uma contagem dos pets na coleção:
> db.pets.count()
8

#### 3) Retorne apenas um elemento o método prático possível:
> db.pets.findOne()
{
        "_id" : ObjectId("5ea774f757ed5258a55909d1"),
        "name" : "Mike",
        "species" : "Hamster"
}

#### 4) Identifique o ID para o Gato Kilha:
> db.pets.find({name:"Kilha"})
{ "_id" : ObjectId("5ea7750257ed5258a55909d3"), "name" : "Kilha", "species" : "Gato" }

#### 5) Faça uma busca pelo ID e traga o Hamster Mike:
> db.pets.find(ObjectId("5ea774f757ed5258a55909d1"))
{ "_id" : ObjectId("5ea774f757ed5258a55909d1"), "name" : "Mike", "species" : "Hamster" }

#### 6) Use o find para trazer todos os Hamsters:
> db.pets.find({species: "Hamster"})
{ "_id" : ObjectId("5ea774f757ed5258a55909d1"), "name" : "Mike", "species" : "Hamster" }
{ "_id" : ObjectId("5ea775af57ed5258a55909d8"), "name" : "Frodo", "species" : "Hamster" }

#### 7) Use o find para listar todos os pets com nome Mike:
> db.pets.find({name: "Mike"})
{ "_id" : ObjectId("5ea774f757ed5258a55909d1"), "name" : "Mike", "species" : "Hamster" }
{ "_id" : ObjectId("5ea7750257ed5258a55909d4"), "name" : "Mike", "species" : "Cachorro" }

#### 8) Liste apenas o documento que é um Cachorro chamado Mike:
> db.pets.find({name: "Mike", species: "Cachorro"})
{ "_id" : ObjectId("5ea7750257ed5258a55909d4"), "name" : "Mike", "species" : "Cachorro" }


### Exercício 2)

executar comando ***mongo italian-people.js --shell***

#### 1. Liste/Conte todas as pessoas que tem exatamente 99 anos. Você pode usar um count para indicar a quantidade:
> db.italians.find({"age": 99}).count()
0

#### 2. Identifique quantas pessoas são elegíveis atendimento prioritário (pessoas com mais de 65 anos)
> db.italians.find({"age": {$gt: 65}}).count()
8620

#### 3. Identifique todos os jovens (pessoas entre 12 a 18 anos)
> db.italians.find({"age": {$gte: 12, $lte: 18}}).count()
4433

#### 4. Identifique quantas pessoas tem gatos, quantas tem cachorro e quantas não tem nenhum dos dois
> db.italians.find({"cat": {$exists: true}}).count()
30079
> db.italians.find({"dog": {$exists: true}}).count()
19993
> db.italians.find({"dog": {$exists: false}, "cat": {$exists: false}}).count()
11910

#### 5. Liste/Conte todas as pessoas acima de 60 anos que tenham gato
> db.italians.find({"age": {$gte: 65},"cat": {$exists: true}}).count()
5554

#### 6. Liste/Conte todos os jovens com cachorro
> db.italians.find({"age": {$gte: 12, $lte: 18}, "dog": {$exists: true}}).count()
1828

#### 7. Utilizando o $where, liste todas as pessoas que tem gato e cachorro
> db.italians.find({$where: "this.cat == this.dog"}).count()
14322

#### 8. Liste todas as pessoas mais novas que seus respectivos gatos.
> db.italians.find({$and: [{ cat: { $exists: true}}, { $where: "this.age < this.cat.age"}]}).count()
3769

#### 9. Liste as pessoas que tem o mesmo nome que seu bichano (gato ou cachorro)
> db.italians.find({$and: [{ dog: { $exists: true}}, { $where: "this.firstname == this.dog.name"}]}).count()
241

#### 10. Projete apenas o nome e sobrenome das pessoas com tipo de sangue de fator RH negativo
> db.italians.find({ bloodType: /(A|B|AB|O)[-]/}, { firstname: 1, surname: 1})
{ "_id" : ObjectId("5ea7805017490ace92e34242"), "firstname" : "Paola", "surname" : "Cattaneo" }
{ "_id" : ObjectId("5ea7805017490ace92e34245"), "firstname" : "Veronica", "surname" : "Piras" }
{ "_id" : ObjectId("5ea7805017490ace92e34247"), "firstname" : "Alessio", "surname" : "Mazza" }
{ "_id" : ObjectId("5ea7805017490ace92e34249"), "firstname" : "Giorgio", "surname" : "Barone" }
{ "_id" : ObjectId("5ea7805017490ace92e3424b"), "firstname" : "Rosa", "surname" : "Benedetti" }
{ "_id" : ObjectId("5ea7805017490ace92e3424d"), "firstname" : "Giorgio", "surname" : "Amato" }
{ "_id" : ObjectId("5ea7805017490ace92e3424e"), "firstname" : "Michela", "surname" : "Caruso" }
{ "_id" : ObjectId("5ea7805017490ace92e34252"), "firstname" : "Claudia", "surname" : "Palumbo" }
{ "_id" : ObjectId("5ea7805017490ace92e34254"), "firstname" : "Roberta", "surname" : "D’Angelo" }
{ "_id" : ObjectId("5ea7805017490ace92e34255"), "firstname" : "Rita", "surname" : "Orlando" }
{ "_id" : ObjectId("5ea7805017490ace92e34256"), "firstname" : "Alberto", "surname" : "Mazza" }
{ "_id" : ObjectId("5ea7805017490ace92e34258"), "firstname" : "Marta", "surname" : "Bianchi" }
{ "_id" : ObjectId("5ea7805017490ace92e34259"), "firstname" : "Alex", "surname" : "Sanna" }
{ "_id" : ObjectId("5ea7805017490ace92e3425d"), "firstname" : "Alex", "surname" : "Damico" }
{ "_id" : ObjectId("5ea7805017490ace92e3425e"), "firstname" : "Angela", "surname" : "Messina" }
{ "_id" : ObjectId("5ea7805017490ace92e3425f"), "firstname" : "Emanuela", "surname" : "De Santis" }
{ "_id" : ObjectId("5ea7805017490ace92e34261"), "firstname" : "Fabrizio", "surname" : "Bruno" }
{ "_id" : ObjectId("5ea7805017490ace92e34262"), "firstname" : "Cinzia", "surname" : "Costatini" }
{ "_id" : ObjectId("5ea7805017490ace92e34263"), "firstname" : "Giuseppe", "surname" : "Grasso" }
{ "_id" : ObjectId("5ea7805017490ace92e34264"), "firstname" : "Sergio", "surname" : "Fabbri" }

#### 11. Projete apenas os animais dos italianos. Devem ser listados os animais com nome e idade. Não mostre o identificado do mongo (ObjectId) ****
> db.italians.find( { $or: [ { "dog": { $exists: true } } , { "cat": { $exists: true } } ] ,  '_id': 0, "dog": {"name": 1}, "cat": {"name": 1 }})

#### 12. Quais são as 5 pessoas mais velhas com sobrenome Rossi?
> db.italians.find({"surname": "Rossi"}).sort({age:-1}).limit(5)
{ "_id" : ObjectId("5ea7805817490ace92e353c6"), "firstname" : "Maurizio", "surname" : "Rossi", "username" : "user4584", "age" : 79, "email" : "Maurizio.Rossi@hotmail.com", "bloodType" : "O-", "id_num" : "824186015735", "registerDate" : ISODate("2012-06-03T17:39:00.140Z"), "ticketNumber" : 5681, "jobs" : [ "Eletrotécnica Industrial", "Agronomia" ], "favFruits" : [ "Pêssego", "Kiwi", "Laranja" ], "movies" : [ { "title" : "Harakiri (1962)", "rating" : 1.4 }, { "title" : "O Poderoso Chefão (1972)", "rating" : 0.39 }, { "title" : "Clube da Luta (1999)", "rating" : 4.27 } ], "cat" : { "name" : "Salvatore", "age" : 15 } }
{ "_id" : ObjectId("5ea7806117490ace92e36714"), "firstname" : "Paola", "surname" : "Rossi", "username" : "user9526", "age" : 79, "email" : "Paola.Rossi@yahoo.com", "bloodType" : "AB-", "id_num" : "341676584168", "registerDate" : ISODate("2020-04-20T10:21:21.605Z"), "ticketNumber" : 7669, "jobs" : [ "Biblioteconomia", "Optometria" ], "favFruits" : [ "Melancia", "Maçã", "Uva" ], "movies" : [ { "title" : "A Origem (2010)", "rating" : 1.24 } ], "cat" : { "name" : "Giovanni", "age" : 11 } }
{ "_id" : ObjectId("5ea7823477e378fcc35d7f0b"), "firstname" : "Chiara", "surname" : "Rossi", "username" : "user1913", "age" : 79, "email" : "Chiara.Rossi@uol.com.br", "bloodType" : "B-", "id_num" : "306165042631", "registerDate" : ISODate("2019-08-02T04:14:37.344Z"), "ticketNumber" : 5219, "jobs" : [ "Agroecologia" ], "favFruits" : [ "Maçã" ], "movies" : [ { "title" : "O Senhor dos Anéis: A Sociedade do Anel (2001)", "rating" : 2.7 }, { "title" : "12 Homens e uma Sentença (1957)", "rating" : 1.11 } ], "cat" : { "name" : "Giorgia", "age" : 13 }, "dog" : { "name" : "Roberta", "age" : 16 } }
{ "_id" : ObjectId("5ea7823b77e378fcc35d8d69"), "firstname" : "Daniela", "surname" : "Rossi", "username" : "user5591", "age" : 79, "email" : "Daniela.Rossi@outlook.com", "bloodType" : "AB-", "id_num" : "315736860707", "registerDate" : ISODate("2009-05-08T01:20:45.024Z"), "ticketNumber" : 2587, "jobs" : [ "Engenharia de Materiais" ], "favFruits" : [ "Maçã" ], "movies" : [ { "title" : "À Espera de um Milagre (1999)", "rating" : 2.99 }, { "title" : "Guerra nas Estrelas (1977)", "rating" : 1.63 } ], "father" : { "firstname" : "Lucia", "surname" : "Rossi", "age" : 94 }, "cat" : { "name" : "Salvatore", "age" : 10 }, "dog" : { "name" : "Manuela", "age" : 12 } }
{ "_id" : ObjectId("5ea783d72db3eb272d87f856"), "firstname" : "Fabrizio", "surname" : "Rossi", "username" : "user4777", "age" : 79, "email" : "Fabrizio.Rossi@hotmail.com", "bloodType" : "AB-", "id_num" : "560865334284", "registerDate" : ISODate("2016-07-26T21:31:05.459Z"), "ticketNumber" : 2687, "jobs" : [ "Teologia" ], "favFruits" : [ "Tangerina" ], "movies" : [ { "title" : "A Vida é Bela (1997)", "rating" : 3.61 } ], "cat" : { "name" : "Angelo", "age" : 5 }, "dog" : { "name" : "Angela", "age" : 1 } }

#### 13. Crie um italiano que tenha um leão como animal de estimação. Associe um nome e idade ao bichano
> db.italians.insert({firstname: "Romeo", surname: "Ferrari", "lion": {name: "Gatinho", "age": 2 }})
WriteResult({ "nInserted" : 1 })

#### 14. Infelizmente o Leão comeu o italiano. Remova essa pessoa usando o Id.
> db.italians.deleteOne( {"_id" : ObjectId("5ea8d92e5b57620712a6f365") } )
{ "acknowledged" : true, "deletedCount" : 1 }

#### 15. Passou um ano. Atualize a idade de todos os italianos e dos bichanos em 1.
> db.italians.update({}, { $inc: { "age": 1, "dog.age":1, "cat.age":1} }, {multi: true} )
WriteResult({ "nMatched" : 60000, "nUpserted" : 0, "nModified" : 60000 })

#### 16. O Corona Vírus chegou na Itália e misteriosamente atingiu pessoas somente com gatos e de 66 anos. Remova esses italianos.
> try {
...    db.italians.deleteMany( { "age" : 66, "cat" : { $exists : true} } );
... } catch (e) {
...    print (e);
... }
{ "acknowledged" : true, "deletedCount" : 765 }

#### 17. Utilizando o framework agregate, liste apenas as pessoas com nomes iguais a sua respectiva mãe e que tenha gato ou cachorro.
> db.italians.aggregate([
... {'$match': { mother: { $exists: 1}, cat: { $exists: 1}, dog: { $exists: 1} }},
... {'$project': {
... "firstname": 1,
... "mother": 1,
... "isEqual": { "$cmp": ["$firstname","$mother.firstname"]}
... }},
... {'$match': {"isEqual": 0}}
... ])
{ "_id" : ObjectId("5ea7805017490ace92e34278"), "firstname" : "Stefano", "mother" : { "firstname" : "Stefano", "surname" : "Farina", "age" : 105 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea7805317490ace92e34966"), "firstname" : "Giacomo", "mother" : { "firstname" : "Giacomo", "surname" : "Barbieri", "age" : 25 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea7805417490ace92e34a0b"), "firstname" : "Manuela", "mother" : { "firstname" : "Manuela", "surname" : "Neri", "age" : 33 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea7805917490ace92e3545f"), "firstname" : "Giovanni", "mother" : { "firstname" : "Giovanni", "surname" : "Fiore", "age" : 44 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea7805b17490ace92e358a5"), "firstname" : "Daniele", "mother" : { "firstname" : "Daniele", "surname" : "Lombardi", "age" : 68 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea7805e17490ace92e360f8"), "firstname" : "Giovanni", "mother" : { "firstname" : "Giovanni", "surname" : "Villa", "age" : 42 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea7806017490ace92e364fb"), "firstname" : "Laura", "mother" : { "firstname" : "Laura", "surname" : "Bruno", "age" : 57 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea7806117490ace92e365d9"), "firstname" : "Sara", "mother" : { "firstname" : "Sara", "surname" : "Piras", "age" : 57 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea7806217490ace92e36886"), "firstname" : "Cristina", "mother" : { "firstname" : "Cristina", "surname" : "Conte", "age" : 52 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea7823477e378fcc35d7fe2"), "firstname" : "Daniele", "mother" : { "firstname" : "Daniele", "surname" : "Donati", "age" : 34 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea7823777e378fcc35d8529"), "firstname" : "Davide", "mother" : { "firstname" : "Davide", "surname" : "Bernardi", "age" : 65 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea7823777e378fcc35d8626"), "firstname" : "Emanuele", "mother" : { "firstname" : "Emanuele", "surname" : "Villa", "age" : 30 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea7823a77e378fcc35d8b9f"), "firstname" : "Giusy", "mother" : { "firstname" : "Giusy", "surname" : "Lombardi", "age" : 65 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea7823b77e378fcc35d8dc6"), "firstname" : "Carlo", "mother" : { "firstname" : "Carlo", "surname" : "Bernardi", "age" : 102 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea7823c77e378fcc35d9041"), "firstname" : "Eleonora", "mother" : { "firstname" : "Eleonora", "surname" : "Fontana", "age" : 89 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea783cf2db3eb272d87e632"), "firstname" : "Alessia", "mother" : { "firstname" : "Alessia", "surname" : "Costa", "age" : 61 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea783d12db3eb272d87eb6e"), "firstname" : "Barbara", "mother" : { "firstname" : "Barbara", "surname" : "Rinaldi", "age" : 53 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea783d22db3eb272d87ec72"), "firstname" : "Enrico", "mother" : { "firstname" : "Enrico", "surname" : "Sanna", "age" : 58 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea783d52db3eb272d87f291"), "firstname" : "Mario", "mother" : { "firstname" : "Mario", "surname" : "Sorrentino", "age" : 46 }, "isEqual" : 0 }
{ "_id" : ObjectId("5ea783d52db3eb272d87f2b7"), "firstname" : "Chiara", "mother" : { "firstname" : "Chiara", "surname" : "Rossetti", "age" : 44 }, "isEqual" : 0 }
Type "it" for more

#### 18. Utilizando aggregate framework, faça uma lista de nomes única. Faça isso usando apenas o primeiro nome
> db.italians.aggregate([
...    { $match: { firstname: {$exists : true} } },
...    { $group: { _id: "$firstname"} }
... ])
{ "_id" : "Luigi" }
{ "_id" : "Massimo" }
{ "_id" : "Giulia" }
{ "_id" : "Fabrizio" }
{ "_id" : "Martina" }
{ "_id" : "Giusy" }
{ "_id" : "Valentina" }
{ "_id" : "Massimiliano" }
{ "_id" : "Fabio" }
{ "_id" : "Ilaria" }
{ "_id" : "Lucia" }
{ "_id" : "Daniele" }
{ "_id" : "Mauro" }
{ "_id" : "Paolo" }
{ "_id" : "Vincenzo" }
{ "_id" : "Patrizia" }
{ "_id" : "Carlo" }
{ "_id" : "Maria" }
{ "_id" : "Federico" }
{ "_id" : "Federica" }
Type "it" for more

#### 19. Agora faça a mesma lista do item acima, considerando nome completo.
> db.italians.aggregate([    { $match: { firstname: {$exists : true} } },    { $group: { _id: "$firstname", _id: "$surname" } }  ])
{ "_id" : "Vitale" }
{ "_id" : "Negri" }
{ "_id" : "Cattaneo" }
{ "_id" : "Conti" }
{ "_id" : "Orlando" }
{ "_id" : "Rizzo" }
{ "_id" : "Piras" }
{ "_id" : "Fabbri" }
{ "_id" : "De Luca" }
{ "_id" : "Moretti" }
{ "_id" : "Gatti" }
{ "_id" : "Testa" }
{ "_id" : "Carbone" }
{ "_id" : "Serra" }
{ "_id" : "Villa" }
{ "_id" : "Grassi" }
{ "_id" : "Bruno" }
{ "_id" : "Silvestri" }
{ "_id" : "Russo" }
{ "_id" : "Fiore" }

#### 20. Procure pessoas que gosta de Banana ou Maçã, tenham cachorro ou gato, mais de 20 e menos de 60 anos.
db.italians.find( {
    $and : [
        { $or: [ { "dog": { $exists: true } } , {"cat": { $exists: true } } ] },
        { favFruits: { $in: ["Banana", "Maçã"] }},
        { $or: [ { "age" : { $gt : 20}} , {"age" : { $lt : 60}}]}])

### Exercício 3)

mongoimport --db stocks --collection stocks --file stock.json


#### 1. Liste as ações com profit acima de 0.5 (limite a 10 o resultado)
> db.stocks.find({"Profit Margin": {$gte: 0.5}}).limit(10).pretty()

#### 2. Liste as ações com perdas (limite a 10 novamente)
> db.stocks.find({"Profit Margin": {$lt: 0.0000}}).limit(10).pretty()

#### 3. Liste as 10 ações mais rentáveis
> db.stocks.find().sort({"Profit Margin": -1}).limit(10).pretty()

#### 4. Qual foi o setor mais rentável?
> db.stocks.aggregate([
...     {
...       "$group": {
...         "_id": {
...           "Industry": "$Industry",
...           "name": "$name"
...         },
...         "count": {
...           "$sum": 1
...         }
...       }
...     },
...     {
...       "$sort": {
...         "Profit Margin": -1,
...         "count": 1
...       }
...     },
...     {"$limit": 10}
...   ])
{ "_id" : { "Industry" : "Toy & Hobby Stores" }, "count" : 1 }
{ "_id" : { "Industry" : "Photographic Equipment & Supplies" }, "count" : 1 }
{ "_id" : { "Industry" : "Medical Practitioners" }, "count" : 1 }
{ "_id" : { "Industry" : "Wholesale, Other" }, "count" : 1 }
{ "_id" : { "Industry" : "Personal Computers" }, "count" : 1 }
{ "_id" : { "Industry" : "Foreign Utilities" }, "count" : 2 }
{ "_id" : { "Industry" : "Building Materials Wholesale" }, "count" : 2 }
{ "_id" : { "Industry" : "Manufactured Housing" }, "count" : 2 }
{ "_id" : { "Industry" : "Tobacco Products, Other" }, "count" : 2 }
***{ "_id" : { "Industry" : "Music & Video Stores" }, "count" : 3 }***

#### 5. Ordene as ações pelo profit e usando um cursor, liste as ações.
> var cursor = db.stocks.find().sort({ "Profit Margin": 1}).limit(10)
> cursor.hasNext()

#### 6. Renomeie o campo “Profit Margin” para apenas “profit”.
> db.stocks.updateMany({}, {$rename: { "Profit Margin": "profit"}})
{ "acknowledged" : true, "matchedCount" : 6756, "modifiedCount" : 4302 }

#### 7. Agora liste apenas a empresa e seu respectivo resultado
db.stocks.aggregate([     {       "$group": {         "_id": {           "Company": "$Company",           "profit": "$profit"         },         "count": {           "$sum": 1         }       }     },     {       "$sort": {         "profit": -1,         "count": 1       }     }   ])

#### 8. Analise as ações. É uma bola de cristal na sua mão... Quais as três ações você investiria?
> db.stocks.aggregate([     {       "$group": {         "_id": {           "Company": "$Company",           "name": "$name"         },         "count": {           "$sum": 1         }       }     },     {       "$sort": {         "profit": -1,         "count": 1       }     },     {"$limit": 3}   ])
{ "_id" : { "Company" : "Dynex Capital Inc." }, "count" : 1 }
{ "_id" : { "Company" : "MannKind Corp." }, "count" : 1 }
{ "_id" : { "Company" : "BlackRock Muni Intermediate Duration Fund, Inc." }, "count" : 1 }

#### 9. Liste as ações agrupadas por setor
 db.stocks.aggregate([     {       "$group": {         "_id": {           "Company": "$Company",           "Industry": "$Industry"              } } } ])

### Exercício 4)

mongoimport --db enron --collection enron --file enron.json


#### 1. Liste as pessoas que enviaram e-mails (de forma distinta, ou seja, sem repetir). Quantas pessoas são?
> db.enron.aggregate(   {     $group: {       _id: '$sender'     }   },   {     $group: {       _id: 1,       count: {         $sum: 1       }     }   } )
{ "_id" : 1, "count" : 2200 }

#### 2. Contabilize quantos e-mails tem a palavra “fraud”
> db.enron.aggregate( [
...   {
...     "$group": {
...       "_id": {
...         "$text": {
...           "$search": "fraud"
...         }
...       }
...     },
...     "$group": {
...       "_id": 1,
...       "count": {
...         "$sum": 1
...       }
...     }
...   }
... ])
{ "_id" : 1, "count" : 5929 }

