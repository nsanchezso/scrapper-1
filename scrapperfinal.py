# importem els moduls necessaris. El bs4 importa la llibraria Beautiful Soup
#
import requests
import bs4
import pandas as pd
import matplotlib.pyplot as plt

# Primer importem les dades de la web seleccionada
resposta = requests.get('https://www.pkparaiso.com/pokemon/lista-pokemon.php')

# Si les imprimim veiem que tenen un format poc comprensible
# print(resposta.text)

sopa = bs4.BeautifulSoup(resposta.text, "html.parser")
# print(sopa.prettify())  # Imprimeix la sortida mitjançant la funció "prettify"

table = sopa.find('table', attrs={
    'class': 'dex sortable'})  # Amb aquest nom seleccione la taula de dades que conté la informació dels pokemons

elementList = []
currentIndex = 0

for row in table.findAll("tr"):  # Itere entre les files de la taula
    cells = row.findAll('td')  # Obtinc tots els elements que conformen les celes de la fila
    if currentIndex > 0:  # Omet la capçalera
        nombre = cells[0].find(text=True)
        nom = (cells[2].find(text=True).lstrip())[5:]
        salud = cells[4].find(text=True)
        atac = cells[5].find(text=True)
        defensa = cells[6].find(text=True)
        velocitat = cells[7].find(text=True)
        AtacEspecial = cells[8].find(text=True)
        DefensaEspecial = cells[9].find(text=True)
        Total = cells[10].find(text=True)
        element = [nombre, nom, salud, atac, defensa, velocitat, AtacEspecial, DefensaEspecial, Total]
        elementList.append(element)
    currentIndex = currentIndex + 1

# Creem un df a partir de la llista elementList
dfPok = pd.DataFrame(elementList)
dfPok.columns = ['Nombre', 'Nom', 'Salud', 'Atac', 'Defensa', 'Velositat', 'Atac_Especial', 'Defensa_Especial', 'Total']

# Aqui exportem les dades a .csv
dfPok.to_csv(r'Caracteristiques_de_Pokemons.csv', index=None, header=True)

# Anem a estudiar l'estructura de les dades extretes

# Primer fem un cop d'ull al df creat
print(dfPok.head())

# Fem un primer analisis descriptiu, primer estabilim el format de les dades
dfPok = dfPok.astype({'Salud': 'int'})
dfPok = dfPok.astype({'Atac': 'int'})
dfPok = dfPok.astype({'Defensa': 'int'})
dfPok = dfPok.astype({'Velositat': 'int'})
dfPok = dfPok.astype({'Atac_Especial': 'int'})
dfPok = dfPok.astype({'Defensa_Especial': 'int'})
dfPok = dfPok.astype({'Total': 'int'})

# Ara veiem que les dades estan en format adequat:

print(dfPok.dtypes)

# En la següent taula veiem un resum de les estadistiques, valor central, desviaciom max, min i quantils
print(dfPok.describe())

# Conjunt de boxplots per descripcio gràfica
dfPok.boxplot(return_type='axes', grid=False, patch_artist=True, vert=False,
              column=['Salud', 'Atac', 'Defensa', 'Velositat', 'Atac_Especial', 'Defensa_Especial'])

plt.show()