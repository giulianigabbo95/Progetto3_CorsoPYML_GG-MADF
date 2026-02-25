'''
Realizzare un sistema Python in grado di:
    - Caricare file .txt o .csv
    - Riconoscere automaticamente se i dati sono:
        . monodimensionali (1D)
        . multidimensionali (2D o superiori)
    - Permettere all'utente di eseguire una o più analisi compatibili
    - Salvare il risultato:
        . nello stesso formato del file originale oppure in formato .txt
    - Ripetere il processo tramite menu interattivo
'''

import numpy as np
import re
import ast
from func_1D import *
from func_2D import *


FILE_OUTPUT = "operazioni.txt"
FILE_INPUT = "matrici.txt"

def salva_su_file(nome_file, operazione, dati):
    with open(nome_file, "a", encoding="utf-8") as f:
        f.write(f"\n--- Operazione: {operazione} ---\n{dati}\n")
        
def carica_lista_matrici(nome_file):
    matrici_trovate = []
    try:
        with open(nome_file, "r", encoding="utf-8") as f:
            contenuto = f.read()
            # Pattern aggiornato: cerca una sequenza che inizia con '[' 
            # e contiene numeri, virgole, spazi o altre parentesi quadre.
            pattern = r"\[[\d, \s\[\]]+\]"
            match = re.findall(pattern, contenuto, re.DOTALL)
            
            for m in match: #<----------------------------------------------------------- NON PUOI CICLARE NEL FILE
                try:
                    # Parsing str e cast in array NumPy
                    matrice_pulita = np.array(ast.literal_eval(m))
                    matrici_trovate.append(matrice_pulita)
                except:
                    continue
        return matrici_trovate
    except FileNotFoundError:
        return []
    
def operazioni(r, c, matrice, operazione):
    r, c = matrice.shape #<----------------------------------------------------------- NON LE USI
    match operazione:
        case "axis_sum_cols":
            risultato = np.sum(matrice, axis = 0)
            print("Somme di tutte le colonne:", risultato)
            return risultato, "Tutte le colonne" #<----------------------------------------------------------- NON HA SENSO
        case "axis_sum_rows":
            risultato = np.sum(matrice, axis = 1)
            print("Somme di tutte le righe:", risultato)
            return risultato, "Tutte le righe"
        case "axis_mean_cols":
            risultato = np.mean(matrice, axis = 0)
            return risultato, "Medie colonne"
        case "axis_mean_rows":
            risultato = np.mean(matrice, axis = 1)
            return risultato, "Medie righe"
        case _:
            print("Operazione non riconosciuta.")
            return None


def play():
    matrice = None
    r, c = 0, 0
    dimensione = "" #<----------------------------------------------------------- NON INIZIALIZZATA FUORI DAL SUCCESSIVO IF
    
    while True:
        if matrice is None: #<----------------------------------------------------------- NON CI STA ELSE
            print("\n--- BENVENUTO ---")
            print("1. Scegli una Matrice dal file di log")
            print("0. Esci")
            scelta_iniziale = input("Cosa vuoi fare? ")
            
            if scelta_iniziale == '1':
                lista = carica_lista_matrici(FILE_INPUT)
                if not lista:
                    print("Nessuna matrice trovata nel file!")
                    continue
                
                print("\n--- MATRICI DISPONIBILI NEL LOG ---")
                for i, m in enumerate(lista):
                    tipo = "2D" if m.ndim == 2 else "1D"
                    print(f"{i}) Matrice {tipo} - Shape {m.shape}:\n{m}\n")
                
                try:
                    indice = int(input("Inserisci il numero della matrice da usare: "))
                    if 0 <= indice < len(lista):
                        matrice = lista[indice]
                        dimensione = "2D" if matrice.ndim == 2 else "1D" #<----------------------------------------------------------- NON SERVE
                        
                        if dimensione == "2D": #<----------------------------------------------------------- NON SERVE
                            r, c = matrice.shape #<----------------------------------------------------------- NON SERVE
                            print(f"Hai selezionato una matrice 2D ({r}x{c}).") #<----------------------------------------------------------- NON SERVE
                        else: #<----------------------------------------------------------- NON SERVE
                            r, c = 1, matrice.shape[0] #<----------------------------------------------------------- NON SERVE
                            print(f"Hai selezionato una matrice 1D ({c} elementi).") #<----------------------------------------------------------- NON SERVE
                        continue # Torna al ciclo per entrare nei menu 1D/2D #<----------------------------------------------------------- NON SERVE
                    else:
                        print("Indice non valido.")
                        matrice = None #<----------------------------------------------------------- NON SERVE
                except ValueError:
                    print("Inserisci un numero valido!")
                    continue #<----------------------------------------------------------- NON SERVE
            
            elif scelta_iniziale == '0':
                break
            else:
                continue #<----------------------------------------------------------- NON HA SENSO

        # --- GESTIONE MATRICE 1D ---
        if dimensione == "1D": #<----------------------------------------------------------- NON INIZIALIZZATA SEMPRE
            print("NULLA")
            pass

        # --- GESTIONE MATRICE 2D ---
        elif dimensione == "2D":
            print("\n--- MENU MATRICE 2D ---")
            print("2. Somma colonne")
            print("3. Somma righe")
            print("4. Media colonne")
            print("5. Media righe")
            # print("7. Media totale")
            print("9. Cambia Matrice")
            print("0. Esci")
            
            scelta = input("Seleziona un'opzione: ")

            if scelta == '2':
                print(matrice,"\n")
                risultato_somma = operazioni(r,c, matrice, "axis_sum_cols") 
                if risultato_somma is not None:
                    salva_su_file(FILE_OUTPUT, "Somma Colonne", risultato_somma)
                    
            elif scelta == '3':
                print(matrice,"\n")
                risultato_somma = operazioni(r,c, matrice, "axis_sum_rows") #<----------------------------------------------------------- NON SERVONO TUTTI QUESTI PARAMETRI
                if risultato_somma is not None:
                    salva_su_file(FILE_OUTPUT, "Somma Righe", risultato_somma)
                    
            elif scelta == '4':
                print(matrice,"\n")
                risultato_media = operazioni(r,c, matrice, "axis_mean_cols")
                if risultato_media is not None:
                    salva_su_file(FILE_OUTPUT, "Media Colonne", risultato_media)
                    
            elif scelta == '5':
                print(matrice,"\n")
                risultato_media = operazioni(r,c, matrice, "axis_mean_rows")
                if risultato_media is not None:
                    salva_su_file(FILE_OUTPUT, "Media Righe", risultato_media)
            
            # elif scelta == '7':
            #     media = matrice.mean()
            #     print(f"Media Totale: {media}")
            #     # salva_su_file(FILE_OUTPUT, "Media Totale", media)
                    
            elif scelta == '9':
                matrice = None 

            elif scelta == '0':
                break

if __name__ == "__main__":
    play()