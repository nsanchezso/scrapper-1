# Pràctica 1: Web scraping

## Descripció

L'objectiu és crecar un data set a partir de dades d'una web. En el nostre cas la web que hem escollit enumera un llistat de Pokemons amb les seves característiques, per tant el que volem es extreure aquesta informació

### 1. Context. 

La infromació que s'ha recolectat, com ja s'ha comentant, és informació realativa a un conjunt de pokemons, el que obtenim son puntuacions referents a unes característiques descriptives. 

La pàgina web seleccionada d'on extraiem les dades per aquesta pràctica és: https://www.pkparaiso.com/pokemon/lista-pokemon.php.

És una web on es recull molta informació referent als jocs, personatges, events... relacionats amb els Pokemons.

A més, amb l'estudi previ realitzat del seu fitxer robots.txt, ens es possible realitzar aquest scrapper.

### 2. Definir un títol pel dataset.

Un títol descriptiu per aquest dataset ha de portar el nom de Pokemon, en aquest cas són característiques que permeten classificar els diferents tipus de Pokemons, per tant possibles titols serien:

- Pokemons
- Tipus de Pokemons
- Caracteristiques de Pokemons
- Classificació de Pokemons

D'entre aquets titols ens decidim per : "Caracteristiques de Pokemons"

### 3. Descripció del dataset. Desenvolupar una descripció breu del conjunt de dades que s'ha extret (és necessari que aquesta descripció tingui sentit amb el títol triat).

El dataset contindrà la informació referent als 802 pokemons existents fins al moment en la història del anime. Aquesta llista es trobará ordenada per nombre, i per cada fila es s'assenyalaràn els trets més importants del pokemon respecte al seu desenvolupament en el combat. Aquest ordre, també indicarà ordre cronològic, ja que els primers en apareixer seràn els més antics, creats en les primeres temporades de la història, i com es vaja avançant cada vegada seràn de creació més recent.

### 4. Representació gràfica. Presentar una imatge o esquema que identifiqui el dataset visualment

La imatge que millor representa el nostre dataset és la següent:

![alt text](https://vignette.wikia.nocookie.net/eswikia/images/d/df/Pok%C3%A9mon.png/revision/latest?cb=20170308220152)

És una imatge on podem veure un grup de pokemos, a simple vista ja veiem que tots són diferents i per tant ja s'intuiex a simple vista que cada un te característiques distintives respecte els altres.


### 5. Contingut. Explicar els camps que inclou el dataset, el període de temps de les dades i com s'ha recollit.

El dataset que obtenim consta de 10 atributs:

nombre : el nombre identificador.
nom : nom del pokemon.
tipus : quin tipus de pokemon és.
salut : punts de salut.
defensa : punts de defensa.
velocitat : la velocitat que pot aconseguir el pokemon.
AtacEspecial : punts d'atac especial.
DefensaEspecial: punts de defensa especial.

Aquestes no són dades temporals, es a dir és simplement un recull caractaristic dels diferents pokemons. En aquesta taula hem recollit infomracio de 802 Pokemons.


### 6. Agraïments.

Els propietaris de la web amb la que treballem són l'empresa Pokemon, el funcador fou Satoshi Tajiri. 


### 7. Inspiració.

L'interés del conjunt de dades és basicament per millorar el coneixement sobre aquesta empresa i els diferents jocs que son possibles amb els seus personatges. Amb les dades que hem obtingut podriem estudiar les diferents característiques dels pokemons així com quan es millor utilitzar cada un d'ells i quins pokemons combaten a quins altres.

### 8. Llicència. 

Seleccionem la llicència "Released Under CC BY-NC-SA 4.0", ja que aquesta llicència ens permet desenvolupar el projecte en un marc colaboratiu no comercial, atribuïnt l'orige de dades a la pàgina web proveïdora i no permetent a tercers el desenvolupament d'activitats comercials a partir d'aquest dataset, ja que no es la finalitat de la pràctica i no em estudiat quins requisits legals pot demandar la pàgina web origen de les dades, a pesar de permeter l'accés mitjançant el fitxer robots.txt.

### 9. Codi. 

El codi amb el que hem treballat esta disponible al enllac a GitHub que es proporciona a l'entrega. 

### 10. Dataset

També adjuntat a aquesta entrega proporcionem el dataset obtingut en fromat csv, les dades estan guardades en un fitxer amb el seguent nom: Pokemon.csv

|   Contribucions	|  Signa 	| 
| ------------- | ------------- |
| Recerca prèvia	|  Noé Sánchez	|
| Redacció de les respostes  	|  Noé Sánchez 	|  
| Desenvolupament codi 	|  Noé Sánchez 	|
