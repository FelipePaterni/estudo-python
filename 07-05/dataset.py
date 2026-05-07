import pandas as pd
from google.colab import drive
drive.mount('/content/drive')

path = '/content/drive/MyDrive/aula_ia/melbourn_csv.csv'
data = pd.read_csv(path, encoding='latin-1', sep =',')


print(data.describe())

data.columns

# Tratando Dados
data = data.dropna(axis=0)

print(data)

# definindo alvo
y = data.Preco

print(y)


features = ['Quartos','Banheiro','TamanhoTerreno','Latitude','Longitude']

X = data[features]


# criar modelo

from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor(random_state=1)

model.fit(X, y)