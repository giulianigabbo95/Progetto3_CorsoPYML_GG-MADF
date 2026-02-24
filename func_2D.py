# Analisi su array multidimensionali (2D o superiori)

# Analisi per assi (somme, medie, aggregazioni)
# In array multi-dimensione è possibile calcolare aggregazioni lungo assi specifici:

# np.sum(matrix, axis=0) → somma per colonne

# np.sum(matrix, axis=1) → somma per righe

# np.mean(matrix, axis=0) → media colonnare

# np.mean(matrix, axis=1) → media riga per riga


# Operazioni matriciali e algebriche (dot, transpose, norme)
# Gli array multidimensionali permettono analisi strutturali complesse:

# np.dot(A, B) → prodotto matriciale

# np.transpose(A) → trasposizione

# np.linalg.norm(A) → norma della matrice

# np.cov(A.T) → matrice di covarianza
import numpy as np
        

def operazioni(r,c, matrice: np.ndarray, operazione:str):
    r, c = matrice.shape
    
    if operazione == "axis_sum_cols":
        # Restituisce un array: [somma_col0, somma_col1, somma_col2...]
        risultato = np.sum(matrice, axis=0)
        print("Somme di tutte le colonne:", risultato)
        return risultato, "Tutte le colonne"

    elif operazione == "axis_sum_rows":
        # Restituisce un array: [somma_riga0, somma_riga1, somma_riga2...]
        risultato = np.sum(matrice, axis=1)
        print("Somme di tutte le righe:", risultato)
        return risultato, "Tutte le righe"

    elif operazione == "axis_mean_cols":
        risultato = np.mean(matrice, axis=0)
        return risultato, "Medie colonne"

    elif operazione == "axis_mean_rows":
        risultato = np.mean(matrice, axis=1)
        return risultato, "Medie righe"
    
    else:
        print("Operazione non riconosciuta.")
        return None
        