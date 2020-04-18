# Atividade prática Neo4j

## Lista de comandos para resolução dos exercícios.

### Exercício 1)

#### Exercise 1.1: Retrieve all nodes from the database:
match (n) return n

#### Exercise 1.2: Examine the data model for the graph:
call db.schema.visualization()

#### Exercise 1.3: Retrieve all Person nodes:
match (p:Person) return p

#### Exercise 1.4: Retrieve all Movie nodes:
match (n:Movie) return n

### Exercício 2)

#### Exercise 2.1: Retrieve all movies that were released in a specific year:
match (m:Movie{released: 2003}) return m

#### Exercise 2.2: View the retrieved results as a table:
match (m:Movie{released: 2003}) return m.title as alias, m.rating as rating, m.roles as roles

#### Exercise 2.3: Query the database for all property keys:
call db.propertyKeys

#### Exercise 2.4: Retrieve all Movies released in a specific year, returning their titles:
match (m:Movie{released: 2006}) return m.title as Title

#### Exercise 2.5: Display title, released, and tagline values for every Movie node in the graph:
match (m:Movie) return m.title as Title, m.released as Released, m.tagline as Tagline

#### Exercise 2.6: Display more user-friendly headers in the table:
match (m:Movie) return m.title as Movie_Title, m.released as Release_Year, m.tagline as Tagline

### Exercício 3)

#### Exercise 3.1: Display the schema of the database:
call db.schema.visualization()

#### Exercise 3.2: Retrieve all people who wrote the movie Speed Racer:
match (p:Person)-[w:WROTE]->(m:Movie {title: 'Speed Racer'}) return p, w, m

#### Exercise 3.3: Retrieve all movies that are connected to the person, Tom Hanks:
match (p:Person {name: 'Tom Hanks'})-->(m:Movie) return m

#### Exercise 3.4: Retrieve information about the relationships Tom Hanks had with the set of movies retrieved earlier:
match (p:Person {name: 'Tom Hanks'})-[r]->(m:Movie) return p.name, type(r), m.title

#### Exercise 3.5: Retrieve information about the roles that Tom Hanks acted in:
match (p:Person {name:'Tom Hanks'})-[r:ACTED_IN]->(m:Movie) return p.name, r.roles, m.title




