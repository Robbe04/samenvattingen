# Dit zijn alle packages die we zullen gebruiken
import numpy as np                                  # "Scientific computing"
import scipy.stats as stats                         # Statistical tests
import pandas as pd                                 # Data Frame
from pandas.api.types import CategoricalDtype
import matplotlib.pyplot as plt                     # Basic visualisation
from statsmodels.graphics.mosaicplot import mosaic  # Mosaic diagram
import seaborn as sns                               # Advanced data visualisation

# Inlezen van een bestand
titanic = pd.read_csv('https://raw.githubusercontent.com/DataRepo2019/Data-files/master/titanic.csv')

# Toon de 1e 5 regels van een dataset
# - parameter om meer regels te tonen
print(titanic.head())

# Toon het het aantal rijen in de dataset
len(titanic)

# Toon het het aantal kolommen in de dataset
len(titanic.columns)

# Toon het aantal rijen en kolommen in één commando
titanic.shape

# Toon de algemene info van een dataset
titanic.info()

# Geef de datatypes van elke velden
titanic.dtypes

# Hoeveel kolommen van elk verschillend datatype is er?
titanic.dtypes.value_counts()

# De index van een kolom is hier toch een variabele dus jij mij moet nu specifiek specificiëren dat dit de index is
titanic.set_index(['PassengerId'])

# Describe the variable Survived -> is considered to be quantitative
titanic.Survived.describe()

# Convert to a categorical variable
titanic.Survived = titanic.Survived.astype('category')

# Ask to describe once more -> now it is considered to be qualitative
titanic.Survived.describe()

# Toon alle unieke waarden 
titanic.PassengerId.unique()

# Tonen van 1 veld
titanic.Age
titanic['Age']

# Tonen van meerdere velden 
titanic[['Age', 'Name', 'Cabin']]

# Tonen van een bepaald aantal kolommen - 2 tot 3
titanic.iloc[:, 2:4]

# Toon alle rijen waarvan de leeftijd >= 18
titanic[titanic.Age >= 18]

# Toon enkel de naam van alle rijen waarbij de leeftijd >= 18
titanic[titanic.Age >= 18].Name

# Hetzelfde maar toon meerdere rijen
titanic[titanic.Age >= 18]['Name', 'PassengerId']

# Droppen van een rij
titanic = titanic.drop("PassengerId", axis="columns")

# Verwijder alle data waarvan één rij minstens één lege waarde heeft
titanicZonderLegeWaarden = titanic.dropna(how="all")

# Toon alle rijen die ingevuld zijn
titanicNotNull = titanic.notnull()
titanicNotNull.sum()

# Lege velden toch opvullen met een bepaalde waarde
gemiddeldeLeeftijd = titanic['Age'].mean()
titanic = titanic.fillna(value={'Age' : gemiddeldeLeeftijd})

# Veranderen van de manier hoe iets wordt opgeslagen
sexVerandering = {'male' : 0, 'female' : 1}
titanic['Sex'] = titanic['Sex'].map(sexVerandering)

