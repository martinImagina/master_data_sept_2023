import pandas as pd

# Leer CSV con Pandas

pokemon_csv_df = pd.read_csv('pokemon_data.csv', 
                             dtype= {
                                 "Name": str,
                                 "Type 1": str,
                                 "Speed": int,
                                 "Generation": int
                             } )

# Imprimir Data Frame
# print(pokemon_csv_df)


# Imprimir los primeros 5
# print(pokemon_csv_df.head(5))

# Imprimir los últimos 5
# print(pokemon_csv_df.tail(5))



# Obtener las columnas de un Data Frame
# print(pokemon_csv_df.columns)


# Obtener los nombres del Data Frame
# print(pokemon_csv_df['Name'])


# Obtener los Nombres y las Velocidades
# print(pokemon_csv_df[['Name','Speed']])

# Definimos la lista de columnas que queremos
# lista_columnas = ['Name', 'Speed', 'Generation']
# print(pokemon_csv_df[lista_columnas])


# Obtener una Fila Concreta
# print(pokemon_csv_df.iloc[0])

# Obtener un rango de Filas Concretas
# print(pokemon_csv_df.iloc[2:11])


# Bucle para iterar por datos

# for i, pokemon in pokemon_csv_df.iterrows():
#     print(f'{i} - {pokemon["Name"]}')


# Buscar por valor
# print( pokemon_csv_df.loc [ pokemon_csv_df ['Type 1'] == 'Fire' ] )


# Sacar estadísticas de los datos
# print(pokemon_csv_df.describe())


# Ordenación
# print(pokemon_csv_df.sort_values('Name', ascending=True))


# Ordenación más compleja
# print(pokemon_csv_df.sort_values(['Type 1', 'HP'], ascending=[True, False])[['Name','Type 1', 'HP' ]])


# Creación de una columna calculada
# pokemon_csv_df['Total'] = pokemon_csv_df['Attack'] + pokemon_csv_df['Defense']
# print(pokemon_csv_df.sort_values('Total', ascending=True).head(5)[['Name', 'Total']])

# Eliminar Columnas
# pokemon_csv_df.drop(columns=['Total'])
# print(pokemon_csv_df)


pokemon_csv_df['Total'] = pokemon_csv_df.iloc[:, 4: 10].sum(axis=1)
print(pokemon_csv_df)










































