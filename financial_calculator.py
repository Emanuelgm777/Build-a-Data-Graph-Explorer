import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from io import StringIO

# 1. Cargar el archivo CSV
def load_csv():
    # Opción 1: Subir un archivo CSV desde la computadora local
    from google.colab import files
    uploaded = files.upload()
    for filename in uploaded.keys():
        return pd.read_csv(filename)

def load_csv_from_url(url):
    # Opción 2: Obtener un archivo CSV desde una URL proporcionada por el usuario
    response = requests.get(url)
    data = StringIO(response.text)
    return pd.read_csv(data)

def load_csv_from_code():
    # Opción 3: Cargar un archivo CSV desde una URL fija en el código
    url = "https://example.com/path/to/your/csvfile.csv"  # Reemplaza con la URL de tu archivo CSV
    return load_csv_from_url(url)

# 2. Interfaz para elegir cómo cargar el archivo CSV
def choose_csv_source():
    choice = input("Selecciona cómo cargar el archivo CSV: \n1. Subir archivo local \n2. Ingresar URL \n3. Cargar desde código (fija) \nSelecciona 1, 2 o 3: ")
    
    if choice == "1":
        return load_csv()
    elif choice == "2":
        url = input("Ingresa la URL del archivo CSV: ")
        return load_csv_from_url(url)
    elif choice == "3":
        return load_csv_from_code()
    else:
        print("Opción no válida. Intentando con opción 1.")
        return load_csv()

# 3. Mostrar los primeros datos y columnas
def display_data(df):
    print("\nPrimeras dos filas de datos:")
    print(df.head(2))
    print("\nColumnas disponibles:")
    print(df.columns)

    columns_list = df.columns.tolist()
    return columns_list

# 4. Convertir columnas a arrays de Numpy
def convert_to_numpy(df, column_names):
    # Convertir las columnas seleccionadas a arrays de Numpy
    data_arrays = {}
    for col in column_names:
        data_arrays[col] = np.array(df[col])
    return data_arrays

# 5. Graficar los datos
def plot_data(x_data, y_data, plot_type='scatter'):
    plt.figure(figsize=(8, 6))
    
    if plot_type == 'scatter':
        plt.scatter(x_data, y_data, c='blue', label='Datos')
        plt.title("Gráfico de Dispersión")
    elif plot_type == 'line':
        plt.plot(x_data, y_data, label='Datos', color='green')
        plt.title("Gráfico de Línea")
    
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.legend()
    plt.grid(True)
    plt.show()

# 6. Función principal para interactuar con el usuario
def main():
    # Cargar el archivo CSV
    df = choose_csv_source()
    
    # Mostrar las primeras filas y las columnas disponibles
    columns_list = display_data(df)
    
    # Elegir columnas para graficar
    print("\nLas columnas disponibles son:", columns_list)
    x_col = input("Selecciona la columna para el eje X: ")
    y_col = input("Selecciona la columna para el eje Y: ")
    
    # Convertir a arrays de Numpy
    data_arrays = convert_to_numpy(df, [x_col, y_col])
    
    # Graficar los datos
    plot_type = input("¿Qué tipo de gráfico deseas? (scatter/line): ").lower()
    plot_data(data_arrays[x_col], data_arrays[y_col], plot_type)

# Ejecutar la función principal
main()
