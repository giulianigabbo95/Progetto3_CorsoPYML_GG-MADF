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

import re
import ast
import numpy as np


FILE_OUTPUT = "operazioni.txt"
FILE_INPUT = "matrici.txt"


def calcolaStatisticheBase(array):
    return {
            "minimo": np.min(array),
            "massimo": np.max(array),
            "media": np.mean(array),
            "devizione": np.std(array)
        }

def performaAnalisiPosizionale(array):
    return {
            "argmin": np.argmin(array),
            "argmax": np.argmax(array),
            "mediana": np.percentile(array, 50)
        }

def calcolaSommaColonne(arrei):
    risultato = np.sum(arrei, axis = 0)
    print("Somme di tutte le colonne:", risultato)
    return risultato, "Somma colonne"

def calcolaSommaColonne(arrei):
    risultato = np.sum(arrei, axis = 1)
    print("Somme di tutte le righe:", risultato)
    return risultato, "Somma righe"

def calcolaMediaColonne(arrei):
    risultato = np.mean(matrice, axis = 0)
    return risultato, "Medie colonne"

def calcolaMediaRighe(arrei):
    risultato = np.mean(arrei, axis = 1)
    return risultato, "Medie righe"

def analizzaArray1D(arrei): 
    risultato  = {}  
    print("Hai scelto 1D")
    print("1. Statistiche Base")
    print("2. Analisi Posizionale")
    print("0. Torna Indietro")
    scelta = input("Scelta: ")
    match scelta:
        case "0":
            return
        case "1":
            risultato = calcolaStatisticheBase(arrei)
            print("Le Statistiche Base sono:", risultato)
            salvaFile(FILE_OUTPUT, "Statistiche Base:", risultato)
        case "2":
            risultato = performaAnalisiPosizionale(arrei)
            print("L'Analisi Posizionale è:", risultato)
            salvaFile(FILE_OUTPUT, "Analisi Posizionale:", risultato)
        case _:
            print("Scelta Sbagliata")

def salvaFile(nome_file, operazione, dati):
    with open(nome_file, "a", encoding = "utf-8") as file:
        file.write("Operazione:", operazione, "-", dati,"\n")

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


def analizzaArray2D(matrice):
    righe, colonne = matrice.shape
    
    print("Hai scelto 2D")
    print("1. Somma Colonne")
    print("2. Somma Righe")
    print("3. Media Colonne")
    print("4. Media Righe")
    print("5. Media Totale")
    print("6. Cambia Matrice")
    print("0. Torna Indietro")
    
    scelta = input("Seleziona un'opzione: ")
    
    match scelta:
        case "0":
            return
        case '1':
            print(matrice, "\n")
            risultato_somma = calcolaSommaColonne(matrice)
            if risultato_somma is not None:
                salvaFile(FILE_OUTPUT, "Somma Colonne", risultato_somma)
        case '2':
            print(matrice, "\n")
            risultato_somma = calcolaSommaColonne(matrice)
            if risultato_somma is not None:
                salvaFile(FILE_OUTPUT, "Somma Righe", risultato_somma)
        case '3':
            print(matrice, "\n")
            risultato_media = calcolaMediaColonne(matrice)
            if risultato_media is not None:
                salvaFile(FILE_OUTPUT, "Media Colonne", risultato_media)
        case '4':
            print(matrice, "\n")
            risultato_media = calcolaMediaRighe(matrice)
            if risultato_media is not None:
                salvaFile(FILE_OUTPUT, "Media Righe", risultato_media)
        case'5':
            media = matrice.mean()
            print("Media Totale:", media)
            salvaFile(FILE_OUTPUT, "Media Totale", media)
        case '6':
            matrice = None
        case _:
            print("Operazione non riconosciuta.")
            return None

def apriMenu(metrix): # -> dimensione
    # 158 - if matrice is None:
    # ...
    # 209 - break
    pass


# MAIN
r, c = 0, 0
matrice = None
dimensione = "" 

while True:
    if matrice is None:
        print("Menu")
        print("1. Scegli una Matrice dal file di log")
        print("0. Esci")
        scelta_iniziale = input("Cosa vuoi fare? ")
        
        match scelta_iniziale:
            case '0':
                break
            
            case '1':
                lista = caricaListaMatrici(FILE_INPUT)
                if not lista:
                    print("Nessuna matrice trovata nel file!")
                    continue
                
                print("Matrici nel file")
                for i, m in enumerate(lista):
                    if m.ndim != 2:
                        tipo = "1D"
                    else:
                        tipo ="2D"
                    print(i, "- Matrice", tipo, "- Shape", m.shape, "\n", m, "\n")
                
                try:
                    indice = int(input("Inserisci il numero della matrice da usare: "))
                    if 0 <= indice < len(lista):
                        matrice = lista[indice]
                        if m.ndim != 2:
                            tipo = "1D"
                        else:
                            tipo ="2D"
                        if dimensione == "1D":
                            r, c = 1, matrice.shape[0]
                            print("Hai selezionato una matrice 1D", c, "elementi")
                        else:
                            r, c = matrice.shape
                            print("Hai selezionato una matrice 2D", r, "x", c)
                        continue
                    else:
                        print("Indice non valido.")
                        matrice = None
                except ValueError:
                    print("Inserisci un numero valido!")
                    continue
            
            case _:
                continue
    else:
        print("Dimensione dove è stato definito per continuare?")
        print("Va a Loop senza BREAK")
        break
    
    match dimensione:
        case "1D":
            analizzaArray1D(matrice)
        case "2D":
            analizzaArray2D(matrice)
        case _:
            print("Da Implementare!")