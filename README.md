# Práctica 1: Web scraping

## Descripció

L'objectiu és crecar un data set a partir de dades d'una web. En el nostre cas la web que hem escollit enumera un llistat de Pokemons amb les seves caracteristiques, per tant el que volem es extreure aquesta infomracio

### 1. Context. 


La infromació que s'ha recolectat, com ja s'ha comentant, és informacio realativa a un conjunt de pokemons, el que obtenim son puntuacions referents a unes caracteristiques descriptives. 

La pàgia web seleccionada d'on extraiem les dades per aquesta pràctica és: https://www.pkparaiso.com/pokemon/lista-pokemon.php.

És una web on es recull molta informació refenent als jocs, personatges, evetnts, ... relacionats amb els Pokemons

### 2. Definir un títol pel dataset.

Un títol descriptiu per aquest dataset ha de portar el nom de Pokemon, en auqest cas son caracterisitques que permeten classificar els difernts tipus de Pokemos per tant possibles titols serien:

- Pokemons
- Tipus de Pokemons
- Caracteristiques de Pokemons
- Classificació de Pokemons
- ... 

D'entre aquets titols ens decidim per : "Caracteristiques de Pokemons"

### 3. Descripció del dataset. Desenvolupar una descripció breu del conjunt de dades que s'ha extret (és necessari que aquesta descripció tingui sentit amb el títol triat).



### 4. Representació gràfica. Presentar una imatge o esquema que identifiqui el dataset visualment

La imatge que millor representa el nostre dataset és la següent:

![alt text](https://vignette.wikia.nocookie.net/eswikia/images/d/df/Pok%C3%A9mon.png/revision/latest?cb=20170308220152)

És una imatge on podem veure un grup de pokemos, a simple vista ja veiem que tots són diferents i per tant ja s'intuiex a simple vista que cada un te caracteristiques distintives respete els altres


### 5. Contingut. Explicar els camps que inclou el dataset, el període de temps de les dades i com s'ha recollit.


El dataset que obetnim consta de 10 atributs:


nombre :  el numero identificador
nom : nom del pokemon
tipus : quin tipus de pokemon és
salut : la salut
defensa : nivell de defensa
velocitat : la velocitat que pot aconseguir el pokemon
AtacEspecial :
DefensaEspecial:


Aquestes no són dades temporals, es a dir és simplement un recull caractaristic dels diferents pokemons. En aquesta taula hem recollit infomracio de 802 Pokemons.



### 6. Agraïments. Presentar el propietari del conjunt de dades. És necessari incloure cites de recerca o anàlisis anteriors (si n'hi ha).


7. Inspiració. Explicar per què és interessant aquest conjunt de dades i quines preguntes es pretenen respondre.
8. Llicència. Seleccionar una d'aquestes llicències pel dataset resultant i explicar el motiu de la seva selecció:
* Released Under CC0: Public Domain License
* Released Under CC BY-NC-SA 4.0 License
* Released Under CC BY-SA 4.0 License
* Database released under Open Database License, individual contentsunder Database Contents License
* Other (specified above)
* Unknown License
9. Codi. Adjuntar el codi amb el qual s'ha generat el dataset, preferiblement en Python o, alternativament, en R.
10. Dataset. Presentar el dataset en format CSV
