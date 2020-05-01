# Atividade prática Neo4j

## Lista de comandos para resolução dos exercícios.

## Start :play intro-neo4j-exercises

### Exercício 1)

#### Exercise 1.1: Retrieve all nodes from the database:
```
match (n) return n
```
#### Exercise 1.2: Examine the data model for the graph:
```
call db.schema.visualization()
```
#### Exercise 1.3: Retrieve all Person nodes:
```
match (p:Person) return p
```
#### Exercise 1.4: Retrieve all Movie nodes:
```
match (n:Movie) return n
```
### Exercício 2)

#### Exercise 2.1: Retrieve all movies that were released in a specific year:
```
match (m:Movie{released: 2003}) return m
```
#### Exercise 2.2: View the retrieved results as a table:
```
match (m:Movie{released: 2003}) return m.title as alias, m.rating as rating, m.roles as roles
```
#### Exercise 2.3: Query the database for all property keys:
```
call db.propertyKeys
```
#### Exercise 2.4: Retrieve all Movies released in a specific year, returning their titles:
```
match (m:Movie{released: 2006}) return m.title as Title
```
#### Exercise 2.5: Display title, released, and tagline values for every Movie node in the graph:
```
match (m:Movie) return m.title as Title, m.released as Released, m.tagline as Tagline
```
#### Exercise 2.6: Display more user-friendly headers in the table:
```
match (m:Movie) return m.title as Movie_Title, m.released as Release_Year, m.tagline as Tagline
```
### Exercício 3)

#### Exercise 3.1: Display the schema of the database:
```
call db.schema.visualization()
```
#### Exercise 3.2: Retrieve all people who wrote the movie Speed Racer:
```
match (p:Person)-[w:WROTE]->(m:Movie {title: 'Speed Racer'}) return p, w, m
```
#### Exercise 3.3: Retrieve all movies that are connected to the person, Tom Hanks:
```
match (p:Person {name: 'Tom Hanks'})-->(m:Movie) return m
```
#### Exercise 3.4: Retrieve information about the relationships Tom Hanks had with the set of movies retrieved earlier:
```
match (p:Person {name: 'Tom Hanks'})-[r]->(m:Movie) return p.name, type(r), m.title
```
#### Exercise 3.5: Retrieve information about the roles that Tom Hanks acted in:
```
match (p:Person {name:'Tom Hanks'})-[r:ACTED_IN]->(m:Movie) return p.name, r.roles, m.title
```
### Exercício 4)

#### Exercise 4.1: Retrieve all movies that Tom Cruise acted in:
```
match (p:Person)-[:ACTED_IN]->(m:Movie)
where p.name = 'Tom Cruise'
return m.title
```
#### Exercise 4.2: Retrieve all people that were born in the 70’s:
```
match (p:Person)
where p.born >= 1970 and p.born <= 1979
return p.name as Name, p.born as Year
```
#### Exercise 4.3: Retrieve the actors who acted in the movie The Matrix who were born after 1960:
```
match (p:Person)-[:ACTED_IN]->(m:Movie)
where m.title = 'The Matrix' and p.born > 1960
return p.name as Name, p.born as `Year Born`
```
#### Exercise 4.4: Retrieve all movies by testing the node label and a property:
```
match (m:Movie)
where m.released = 2000
return m.title as Title
```
#### Exercise 4.5: Retrieve all people that wrote movies by testing the relationship between two nodes:
```
match (p)-[r]->(m)
where type(r) = 'WROTE' and p:Person and m:Movie
return p.name, m.title
```
#### Exercise 4.6: Retrieve all people in the graph that do not have a property:
```
match (p)
where p:Person and exists(p.born) = false
return p.name as Name
```
#### Exercise 4.7: Retrieve all people related to movies where the relationship has a property:
```
match (m:Movie)<-[r]-(p:Person)
where exists(r.rating) = true
return p.name as Name, m.title as Title, r.rating as Rating
```
#### Exercise 4.8: Retrieve all actors whose name begins with James:
```
match (p:Person)-[:ACTED_IN]->(:Movie)
where p.name starts with 'James'
return p.name as Name
```
#### Exercise 4.9: Retrieve all all REVIEW relationships from the graph with filtered results:
```
match (:Person)-[r:REVIEWED]->(m:Movie)
where toLower(r.summary) contains 'fun'
return m.title as Title, m.rating as Rating, m.summary as Summary
```
#### Exercise 4.10: Retrieve all people who have produced a movie, but have not directed a movie:
```
match (p:Person)-[r]->(m:Movie)
where type(r) = 'PRODUCED' and type(r) <> 'DIRECTED'
return p.name as Name, m.title as `Movie Title`
```
#### Exercise 4.11: Retrieve the movies and their actors where one of the actors also directed the movie:
```
match (p1:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(p2)
where exists( (p1)-[:DIRECTED]->(m) )
return p1.name as `Director/Actor`, p2.name as Actor, m.title as Movie
```
#### Exercise 4.12: Retrieve all movies that were released in a set of years:
```
match (m:Movie)
where m.released in [2000, 2004, 2008]
return m.title as Title, m.released as Release_Year
```
#### Exercise 4.13: Retrieve the movies that have an actor’s role that is the name of the movie:
```
match (:Person)-[r:ACTED_IN]->(m:Movie)
where m.title in r.roles
return r.roles, m.title
```
### Exercício 5)

#### Exercise 5.1: Retrieve data using multiple MATCH patterns:
```
match (p1:Person {name: 'Gene Hackman'})-[:ACTED_IN]->(m:Movie)<-[:DIRECTED]-(p2:Person), (p3:Person)-[:ACTED_IN]->(m)
return m.title as Movie_Title, p2.name as Director, p3.name as Co_actors
```
#### Exercise 5.2: Retrieve particular nodes that have a relationship:
```
match (p1:Person)-[:FOLLOWS]-(p2:Person)
where p1.name = 'James Thompson'
return p1, p2
```
#### Exercise 5.3: Modify the query to retrieve nodes that are exactly three hops away:
```
match (p1:Person)-[:FOLLOWS*3]-(p2:Person)
where p1.name = 'James Thompson'
return p1, p2
```
#### Exercise 5.4: Modify the query to retrieve nodes that are one and two hops away:
```
match (p1:Person)-[:FOLLOWS*1..2]-(p2:Person)
where p1.name = 'James Thompson'
return p1, p2
```
#### Exercise 5.5: Modify the query to retrieve particular nodes that are connected no matter how many hops are required:
```
match (p1:Person)-[:FOLLOWS*]-(p2:Person)
where p1.name = 'James Thompson'
return p1, p2
```
#### Exercise 5.6: Specify optional data to be retrieved during the query:
```
match (p:Person)
where p.name starts with 'Tom'
optional match (p)-[r:DIRECTED]->(m:Movie)
return p.name, m.title
```
#### Exercise 5.7: Retrieve nodes by collecting a list:
```
match (p:Person)-[r:ACTED_IN]->(m:Movie)
return p.name as Actor, collect(m.title) as Movies_List
```
#### Exercise 5.9: Retrieve nodes as lists and return data associated with the corresponding lists:
```
match (p:Person)-[r:REVIEWED]->(m:Movie)
return m.title as Title, collect(p.name) as Reviewers, count(p) as Review_count
```
#### Exercise 5.10: Retrieve nodes and their relationships as lists:
```
match (d:Person)-[:DIRECTED]->(m:Movie)<-[:ACTED_IN]-(a:Person)
return d.name as Director, count(a.name) as Number_Actors, collect(a.name) as Actors
```
#### Exercise 5.11: Retrieve the actors who have acted in exactly five movies:
```
match (a:Person)-[:ACTED_IN]->(m:Movie)
with m, count(m) as numMovies, collect(m.title) as Movies
where numMovies = 5
return a.name as Actor, Movies
```
#### Exercise 5.12: Retrieve the movies that have at least 2 directors with other optional data:
```
match (d:Person)-[:DIRECTED]->(m:Movie)<-[:REVIEWED]-(r:Person)
with d, count(d) as numDirector, collect(d.name) as Directors
where numDirector > 2
return m.title as Title, Directors, r.name as Reviewers
```
### Exercício 6)

#### Exercise 6.1: Execute a query that returns duplicate records:
```
match (p:Person)-[:ACTED_IN]->(m:Movie)
where m.released>=1990 and m.released < 2000
return m.released, m.title, collect(p.name)
```
#### Exercise 6.2: Modify the query to eliminate duplication:
```
match (p:Person)-[:ACTED_IN]->(m:Movie)
where m.released>=1990 and m.released < 2000
return m.released, collect(m.title), collect(p.name)
```
#### Exercise 6.3: Modify the query to eliminate more duplication:
```
match (p:Person)-[:ACTED_IN]->(m:Movie)
where m.released>=1990 and m.released < 2000
return m.released, collect(distinct m.title), collect(p.name)
```
#### Exercise 6.4: Sort results returned:
```
match (p:Person)-[:ACTED_IN]->(m:Movie)
where m.released>=1990 and m.released < 2000
return m.released, collect(distinct m.title), collect(p.name)
order by m.released desc
```
#### Exercise 6.5: Retrieve the top 5 ratings and their associated movies:
```
match (m:Movie)
return m.title, m.rating as rating 
order by rating desc limit 5
```

#### Exercise 6.6: Retrieve all actors that have not appeared in more than 3 movies:
```
match (p:Person)-[:ACTED_IN]->(m:Movie)
with p, count(p) as numMovies, collect(m.title) as listMovies
where numMovies <= 3
return p.name, listMovies

```
### Exercício 7)

#### Exercise 7.1: Collect and use lists:
```
match (a:Person)-[:ACTED_IN]->(m:Movie), (m)<-[:PRODUCED]-(p:Person)
with m,  collect(distinct a.name) as Actors, collect(distinct p.name) as Producers
return distinct m.title, Actors, Producers
order by size(Actors)

```
#### Exercise 7.2: Collect a list:
```
match (a:Person)-[:ACTED_IN]->(m:Movie)
with a, collect(m.title) as movies
where size(movies) > 5
return a.name as actors, movies

```
#### Exercise 7.3: Unwind a list:
```
match (a:Person)-[:ACTED_IN]->(m:Movie)
with a, collect(m) as movies
where size(movies) > 5
with a, movies unwind movies as movie
return a.name as actors, movie.title

```
#### Exercise 7.4: Perform a calculation with the date type:
```
match (a:Person)-[:ACTED_IN]->(m:Movie)
where a.name = 'Tom Hanks'
return m.title, m.released, date().year - m.released as Years_of_Release, m.released - a.born as Tom_Age
order by Tom_Age

```
### Exercício 8)

#### Exercise 8.1: Create a Movie node:
```
create (:Movie {title: 'Forrest Gump'})

```
#### Exercise 8.2: Retrieve the newly-created node:
```
match (m:Movie)
where m.title = 'Forrest Gump'
return m

```
#### Exercise 8.3: Create a Person node:
```
match (p:Person)
where p.name = 'Robin Wright'
return p

```
#### Exercise 8.4: Retrieve the newly-created node:
```
match (p:Person)
where p.name = 'Robin Wright'
return p

```
#### Exercise 8.5: Add a label to a node:
```
match (m:Movie)
where m.released < 2010
set m:OlderMovie
return m.title, labels(m)

```
#### Exercise 8.6: Retrieve the node using the new label:
```
match (m:OlderMovie)
return m.title, m.released

```
#### Exercise 8.7: Add the Female label to selected nodes:
```
match (p:Person)
where p.name starts with 'Robin'
set p:Female
return p.name

```
#### Exercise 8.8: Retrieve all Female nodes:
```
match (p:Female)
return p.name

```
#### Exercise 8.9: Remove the Female label from the nodes that have this label:
```
match (p:Person)
remove p:Female

```
#### Exercise 8.10: View the current schema of the graph:
```
call db.schema.visualization()

```
#### Exercise 8.11: Add properties to a movie:
```
match (m:Movie)
where m.title = 'Forrest Gump'
set m:OlderMovie, m.released = 1994, m.tagline = 'Life is like a box of chocolates... you never know what you`re gonna get', m.lenghtInMinutes = 142

```
#### Exercise 8.12: Retrieve an OlderMovie node to confirm the label and properties:
```
match (m:Movie)
where m.title = 'Forrest Gump'
return m

```
#### Exercise 8.13: Add properties to the person, Robin Wright:
```
match (p:Person)
where p.name = 'Robin Wright'
set p.born = 1966, p.birthPlace = "Dallas"
return p

```
#### Exercise 8.14: Retrieve an updated Person node:
```
match (p:Person)
where p.name = 'Robin Wright'
return p

```
#### Exercise 8.15: Remove a property from a Movie node:
```
match (m:OlderMovie)
where m.title = 'Forrest Gump'
remove m.lenghtInMinutes

```
#### Exercise 8.16: Retrieve the node to confirm that the property has been removed:
```
match (m:OlderMovie)
where m.title = 'Forrest Gump'
return m

```
#### Exercise 8.17: Remove a property from a Person node:
```
match (p:Person)
where p.name = 'Robin Wright'
set p.birthPlace = null

```
#### Exercise 8.18: Retrieve the node to confirm that the property has been removed:
```
match (p:Person)
where p.name = 'Robin Wright'
return p

```
### Exercício 9)

#### Exercise 9.1: Create ACTED_IN relationships:
```
match (p:Person), (m:OlderMovie)
where p.name = 'Robin Wright' or p.name = 'Tom Hanks' or p.name = 'Gary Sinise' and m.title = 'Forrest Gump'
create (p)-[:ACTED_IN]->(m)
return p, m

```
#### Exercise 9.2: Create DIRECTED relationships:
```
match (p:Person)
where p.name = 'Robert Zemeckis'
match (m:OlderMovie)
where m.title = 'Forrest Gump'
create (p)-[:DIRECTED]->(m)

```
#### Exercise 9.3: Create a HELPED relationship:
```
match (p1:Person)
where p1.name = 'Tom Hanks'
match (p2:Person)
where p2.name = 'Gary Sinise'
create (p1)-[:HELPED]->(p2)

```
#### Exercise 9.4: Query nodes and new relationships:
```
match (p:Person)-[r]->(m:OlderMovie)
where m.title = 'Forrest Gump'
return p, r, m

```
#### Exercise 9.5: Add properties to relationships:
```
match (p:Person)-[r:ACTED_IN]->(m:OlderMovie)
where m.title = 'Forrest Gump'
set r.roles =
case p.name
when 'Tom Hanks' then ['Forrest Gump']
when 'Robin Wright' then ['Jenny Curran']
when 'Gary Sinise' then ['Lieutenant Dan Taylor']
end

```
#### Exercise 9.6: Add a property to the HELPED relationship:
```
match (p1:Person)-[r:HELPED]->(p2:Person)
where p1.name = 'Tom Hanks' and p2.name = 'Gary Sinise'
set r.research = 'war history'

```
#### Exercise 9.7: View the current list of property keys in the graph:
```
call db.propertyKeys

```
#### Exercise 9.8: View the current schema of the graph:
```
call db.schema.visualization()

```
#### Exercise 9.9: Retrieve the names and roles for actors:
```
match (p:Person)-[r:ACTED_IN]->(m:OlderMovie)
where m.title = 'Forrest Gump'
return p.name, r.roles

```
#### Exercise 9.10: Retrieve information about any specific relationships:
```
match (p1:Person)-[r:HELPED]->(p2:Person)
return p1.name, r, p2.name

```
#### Exercise 9.11: Modify a property of a relationship:
```
match (p1:Person)-[r:ACTED_IN]->(m:OlderMovie)
where p1.name = 'Gary Sinise' and m.title = 'Forrest Gump'
set r.roles = 'Lt. Dan Taylor'

```
#### Exercise 9.12: Remove a property from a relationship:
```
match (p1:Person)-[r:HELPED]->(p2:Person)
where p1.name = 'Tom Hanks' and p2.name = 'Gary Sinise'
delete r

```
#### Exercise 9.13: Confirm that your modifications were made to the graph:
```
match (p:Person)-[r:ACTED_IN]->(m:Movie)
where m.title = 'Forrest Gump'
return p, r, m

```
### Exercício 10)

#### Exercise 10.1: Delete a relationship:
```
match (p1:Person)-[r:HELPED]->(p2:Person)
where p1.name = 'Tom Hanks' and p2.name = 'Gary Sinise'
delete r

```
#### Exercise 10.2: Confirm that the relationship has been deleted:
```
match (:Person)-[r:HELPED]->(p:Person)
return r

```
#### Exercise 10.3: Retrieve a movie and all of its relationships:
```
match (p:Person)-[r]->(m:OlderMovie)
where m.title = 'Forrest Gump'
return p, r, m

```
#### Exercise 10.4: Try deleting a node without detaching its relationships:
```
match (p:Person)-[r]->(m:OlderMovie)
where m.title = 'Forrest Gump'
delete m

```
#### Exercise 10.5: Delete a Movie node, along with its relationships:
```
match (m:OlderMovie)
where m.title = 'Forrest Gump'
detach delete m

```
#### Exercise 10.6: Confirm that the Movie node has been deleted:
```
match (m:OlderMovie)
where m.title = 'Forrest Gump'
return m
```