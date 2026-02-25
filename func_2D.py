import numpy as np
        

def operazioni(matrice: np.ndarray, operazione:str):
    if operazione == "axis_sum_cols":
        risultato = np.sum(matrice, axis=0)
        print("Somme di tutte le colonne:", risultato)
        return risultato

    elif operazione == "axis_sum_rows":
        risultato = np.sum(matrice, axis=1)
        print("Somme di tutte le righe:", risultato)
        return risultato

    elif operazione == "axis_mean_cols":
        risultato = np.mean(matrice, axis=0)
        return risultato

    elif operazione == "axis_mean_rows":
        risultato = np.mean(matrice, axis=1)
        return risultato
    
    else:
        print("Operazione non riconosciuta.")
        return None
        
        
