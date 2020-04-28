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
