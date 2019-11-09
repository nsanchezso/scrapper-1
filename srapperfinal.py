# importem els moduls necessaris. El bs4 importa la llibraria Beautiful Soup
#
import requests
import bs4

# Primer importem les dades de la web seleccionada
resposta = requests.get('https://www.pkparaiso.com/pokemon/lista-pokemon.php')

# Si les imprimim veiem que tenen un format poc comprensible
#print(resposta.text)

sopa = bs4.BeautifulSoup(resposta.text, "html.parser")
#print(sopa.prettify())  # Imprimeix la sortida mitjançant la funció "prettify"

table = sopa.find('table', attrs={'class':'dex sortable'})          #Amb aquest nom seleccione la taula de dades que conté la informació dels pokemons
elementList = [["Nombre","Nom","Salud","Atac","Defensa","Velositat","Arac_Especial","Defensa_Especial"]]
currentIndex = 0

for row in table.findAll("tr"):                                     #Itere entre les files de la taula
    cells = row.findAll('td')                                       #Obtinc tots els elements que conformen les celes de la fila
    if currentIndex > 0:                                            #Omet la capçalera
        nombre = cells[0].find(text=True)
        #imatge = cells[1].find(text=True)
        nom = cells[2].find(text=True)
        #tipus = cells[3].find(text=True)                           # l'he comentat pk em creava un salt de linia
        salud = cells[4].find(text=True)
        atac = cells[5].find(text=True)
        defensa = cells[6].find(text=True)
        velocitat = cells[7].find(text=True)
        AtacEspecial = cells[8].find(text=True)
        DefensaEspecial = cells[9].find(text=True)
        Total = cells[10].find(text=True)
        element = [nombre, nom, salud, atac, defensa, velocitat, AtacEspecial, DefensaEspecial, Total]
        elementList.append(element)
    currentIndex = currentIndex+1

import pandas as pd 

# Creem un df a partir de la llista elementList
dfPok =pd.DataFrame(elementList)


# Fem un cop d'ull al df
print(dfPok)

# Aqui exportem les dades a .csv
dfPok.to_csv (r'Pokemon.csv', index = None, header=False)

# Anem a estudiar l'estructura de les dades extretes

# Primer fem un cop d'ull al df creat
dfPok.head()
