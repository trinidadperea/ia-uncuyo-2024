from CSP import*
import csv
import statistics
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    reinas = [4,8,10]

    encabezado = ['algorithm_name','n','prev_states','time']
    soluciones = []


    tiempos_backtracking = {}
    tiempos_forward_checking = {}

    states_backtracking = {}
    states_forward_checking = {}


    for n in reinas:
        tiempos_backtracking[n] = []
        states_backtracking[n] = []

        tiempos_forward_checking[n] = []
        states_forward_checking[n] = []

        for i in range(30):
            _, estados, tiempo = backtracking_n_reinas(n)
            tiempos_backtracking[n].append(tiempo)
            states_backtracking[n].append(estados)
            soluciones.append(("backtracking",n,estados,tiempo))

            _, estados_f, tiempo_f = forward_checking_n_reinas(n)
            tiempos_forward_checking[n].append(tiempo_f)
            states_forward_checking[n].append(estados_f)
            soluciones.append(("forward_checking",n,estados_f,tiempo_f))

    with open('tp6-Nreinas.csv', mode = 'w', newline='') as file:
        escritor_csv = csv.writer(file)

        escritor_csv.writerow(encabezado)

        escritor_csv.writerows(soluciones)
    
    #---MEDIAS Y DESVIACIONES ESTANDAR  
    print("Media y desviación estándar de tiempos")
    media_y_desviacion(tiempos_backtracking,"Backtracking")
    media_y_desviacion(tiempos_forward_checking,"Forward_checking")
    
    print("\nMedia y desviación estándar de estados visitados")
    media_y_desviacion(states_backtracking,"Backtracking")
    media_y_desviacion(states_forward_checking,"Forward_checking")

    #pandas permite cargar los datos del .csv
    df = pd.read_csv('tp6-Nreinas.csv')
    
    #plt.figure(figsize=(10,6))
    #seaborn genera el grafico de caja
    sns.boxplot(x = 'algorithm_name', y = 'time', data = df)

    plt.title('Distribución de tiempos de ejecución')
    plt.xlabel('Algoritmo')
    plt.ylabel('Tiempo de ejecución')
    plt.show()
    plt.savefig('Dist_tiempos_boxplot.png')

    #plt.figure(figsize=(10,6))
    sns.boxplot(x = 'algorithm_name', y = 'prev_states', data = df, showfliers = True)

    plt.title('Distribución de estados previos visitados')
    plt.xlabel('Algoritmo')
    plt.ylabel('Estados previos visitados')
    plt.show()
    plt.savefig('Dist_estados_previos_boxplot.png')



def media_y_desviacion(tiempo_o_estados,algoritmo):
    # Media y desviacion estandar de tiempo
    
    for n, lista in tiempo_o_estados.items():
        mean = statistics.mean(lista)
        desv = statistics.stdev(lista)
    
        print(f"{algoritmo} {n}-reinas")
        print(f"media = {mean}, desviacion estándar = {desv}")
    


if __name__ == "__main__":
    main()    




