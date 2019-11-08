# importem els moduls necessaris. El bs4 importa la llibraria Beautiful Soup
#
import requests
import bs4

# Primer importem les dades de la web seleccionada
resposta = requests.get('https://www.pkparaiso.com/pokemon/lista-pokemon.php')

# Si les imprimim veiem que tenen un format poc comprensible
print(resposta.text) 

sopa  =  bs4.BeautifulSoup ( resposta.text ,  "html.parser" ) 
print ( sopa.prettify ())  # Imprimeix la sortida mitjançant la funció "prettify"

print(soup.find('td', attrs = {'Nom':'row1'}))
