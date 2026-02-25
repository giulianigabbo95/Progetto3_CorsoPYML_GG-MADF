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
from func_1D import calcolaStatisticheBase, performaAnalisiPosizionale
from func_2D import operazioni


FILE_OUTPUT = "operazioni.txt"
FILE_INPUT = "matrici.txt"

def salvaFile(nome_file, operazione, dati):
    with open(nome_file, "a", encoding="utf-8") as f:
        f.write(f"\n--- Operazione: {operazione} ---\n{dati}\n")
        
def caricaListaMatrici(nome_file):
    matrici_trovate = []
    try:
        with open(nome_file, "r", encoding = "utf-8") as file:
            contenuto = file.read()
            pattern = r"\[[\d, \s\[\]]+\]"
            match = re.findall(pattern, contenuto, re.DOTALL)
        for m in match:
            try:
                matrice_pulita = np.array(ast.literal_eval(m))
                matrici_trovate.append(matrice_pulita)
            except:
                continue
        return matrici_trovate
    except FileNotFoundError:
        return []
    
def analizzaArray1D(matrice): 
    risultato  = {}  
    print("Hai scelto 1D")
    print("1. Statistiche Base")
    print("2. Analisi Posizionale")
    print("6. Cambia Matrice")
    print("0. Esci")
    scelta = input("Scelta: ")
    match scelta:
        case "0":
            return
        case "1":
            risultato = calcolaStatisticheBase(matrice)
            print("Le Statistiche Base sono:", risultato)
            salvaFile(FILE_OUTPUT, "Statistiche Base:", risultato)
            return risultato
        case "2":
            risultato = performaAnalisiPosizionale(matrice)
            print("L'Analisi Posizionale è:", risultato)
            salvaFile(FILE_OUTPUT, "Analisi Posizionale:", risultato)
            return risultato
        case '6':
            return None
        case _:
            print("Scelta Sbagliata")
            
def analizzaArray2D(matrice):    
    print("Hai scelto 2D")
    print("1. Somma Colonne")
    print("2. Somma Righe")
    print("3. Media Colonne")
    print("4. Media Righe")
    print("5. Media Totale")
    print("6. Cambia Matrice")
    print("0. Esci")
    
    scelta = input("Seleziona un'opzione: ")
    matrice
    match scelta:
        case "0":
            return
        case '1':
            print(matrice, "\n")
            risultato_somma = operazioni(matrice,"axis_sum_cols")
            if risultato_somma is not None:
                salvaFile(FILE_OUTPUT, "Somma Colonne", risultato_somma)
            return risultato_somma
        case '2':
            print(matrice, "\n")
            risultato_somma = operazioni(matrice,"axis_sum_rows")
            if risultato_somma is not None:
                salvaFile(FILE_OUTPUT, "Somma Righe", risultato_somma)
            return risultato_somma
        case '3':
            print(matrice, "\n")
            risultato_media = operazioni(matrice,"axis_mean_cols")
            if risultato_media is not None:
                salvaFile(FILE_OUTPUT, "Media Colonne", risultato_media)
            return risultato_media
        case '4':
            print(matrice, "\n")
            risultato_media = operazioni(matrice,"axis_mean_rows")
            if risultato_media is not None:
                salvaFile(FILE_OUTPUT, "Media Righe", risultato_media)
            return risultato_media
        case '6':
            return None
        case _:
            print("Operazione non riconosciuta.")
            return None
            
def play():
    matrice = None
    r, c = 0, 0
    dimensione = "" 
    
    while True:
        if matrice is None:
            print("\n--- BENVENUTO ---")
            print("1. Scegli una Matrice dal file di log")
            print("0. Esci")
            scelta_iniziale = input("Cosa vuoi fare? ")
            
            if scelta_iniziale == '1':
                lista = caricaListaMatrici(FILE_INPUT)
                if not lista:
                    print("Nessuna matrice trovata!")
                    continue
                
                print("\n--- MATRICI DISPONIBILI ---")
                for i, m in enumerate(lista):
                    tipo_visual = "2D" if m.ndim == 2 else "1D"
                    print(f"{i}) Matrice {tipo_visual} - Shape {m.shape}")
                
                try:
                    indice = int(input("\nInserisci il numero della matrice: "))
                    if 0 <= indice < len(lista):
                        # --- ASSEGNAZIONE DINAMICA ---
                        matrice = lista[indice]
                        
                        if matrice.ndim == 2:
                            dimensione = "2D"
                            r, c = matrice.shape
                        else:
                            dimensione = "1D"
                            r, c = 1, matrice.shape[0] 
                        
                        print(f"-> Caricata Matrice {dimensione}: {r}x{c}")
                    else:
                        print("Indice errato.")
                        continue
                except ValueError:
                    print("Errore: inserisci un numero intero.")
                    continue
            
            elif scelta_iniziale == '0':
                break
            else: continue
            
        if matrice is not None:  
            match dimensione:
                case "1D":
                    if analizzaArray1D(matrice) == None:
                        matrice = None
                        dimensione = ""
                case "2D":
                    if analizzaArray2D(matrice) == None:
                        matrice = None
                        dimensione = ""
                case _:
                    matrice = None
                    dimensione = ""
                    continue
            
play()