import time
#Este enfoque permite reducir el espacio de búsqeuda al ir descartando opciones 
#inválidas de manera temprana 
def backtracking_n_reinas(N):
    inicio = time.perf_counter()
    posiciones = [-1] * N
    #soluciones = []
    solucion, previous_states = colocar_reina(N,0,posiciones,0)
    fin = time.perf_counter()
    tiempo_transcurrido = fin - inicio
    
    return solucion, previous_states, tiempo_transcurrido

def colocar_reina(N, fila, posiciones,previous_states):
    #caso base: si llego a la ultima columna posible dentro del rango    
    if fila == N:
        #soluciones.append(posiciones[:])
        return posiciones[:], previous_states
    
    for columna in range(N):
        previous_states += 1
        if is_pos_valida(posiciones, fila,columna):
            #si la posicion no es válida, luego se sobreescribe por una columna válida
            posiciones[fila] = columna
            solucion, states = colocar_reina(N, fila+1, posiciones,previous_states)
            if solucion:
                return solucion, states
            #marcar la columna como -1 no es necesario porque se sobreescriben los valores cuando se encuentra una pos válida
            posiciones[fila] = -1
    
    return None, 0

#Usamos las restricciones para filtrar el espacio de búsqueda
def is_pos_valida(posiciones, fila, columna):
    for i in range(fila):
        if posiciones[i] == columna:
            return False
        if abs(posiciones[i] - columna) == abs(i-fila):
            return False
    return True

print("backtracking")
#cont = 0
solucion, estados, tiempo = backtracking_n_reinas(8)
print(f"solución: {solucion}\n previous_states: {estados}\n tiempo: {tiempo}")
#for solucion in soluciones:
#    cont += 1
#print(cont)


def forward_checking_n_reinas(N):
    #soluciones = []
    inicio = time.perf_counter()
    dominios = [list(range(N)) for _ in range(N)]
    solucion, prev_states = colocar_reina_f(N,0,[],dominios,0)
    fin = time.perf_counter()
    tiempo_transcurrido = fin - inicio
    return solucion, prev_states, tiempo_transcurrido

def colocar_reina_f(N, fila, posiciones, dominios, prev_states):
    #caso base: si llego a la ultima columna posible dentro del rango    
    if fila == N:
        return posiciones[:], prev_states
    
    for columna in dominios[fila]:
        prev_states += 1
        if es_valida(posiciones, fila, columna):
            #agregamos la posicion
            posiciones.append(columna)
            #guardamos los dominios por si falla y hay que hacer backtracking
            dominios_backup = [dom.copy() for dom in dominios]
            #actualizamos los dominios teniendo en cuenta las restricciones de la posicion actual
            if actualizar_dominios(dominios, fila, columna, N):
                solucion, states = colocar_reina_f(N, fila+1, posiciones, dominios,prev_states)
            
                if solucion:
                    return solucion, states

        dominios = dominios_backup
        posiciones.pop()

    return None, 0

#Usamos las restricciones para filtrar el espacio de búsqueda
def es_valida(posiciones, fila, columna):
    for i in range(fila):
        #si hay otra reina en la misma columna o en la mima diagonal
        if posiciones[i] == columna or abs(posiciones[i] - columna) == abs(i - fila):
            return False
    return True

def actualizar_dominios(dominios, fila, columna, N):
    for i in range(fila+1,N):
        #sacamos la columna actual del dominio de la fila siguiente
        if columna in dominios[i]:
            dominios[i].remove(columna)

        main_diag = columna - (i-fila)
        sec_diag = columna + (i-fila)

        if main_diag in dominios[i]:
            dominios[i].remove(main_diag)
        if sec_diag in dominios[i]:
            dominios[i].remove(sec_diag)
        
        #si hay alguna fila que queda con dominio vacío, falla 
        #y tiene que hacer backtrack
        if not dominios[i]:
            return False
        
    return True


print("Forward Checking")
solucion, estados, tiempo = forward_checking_n_reinas(8)
print(f"solución: {solucion}\n previous_states: {estados}\n tiempo: {tiempo}")
# for solucion in soluciones:
#     cont += 1
# print(cont)