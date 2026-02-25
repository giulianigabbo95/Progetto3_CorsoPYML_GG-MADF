import numpy as np

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

# def analizzaArray1D(arrei):
    
#     risultato  = {}
    
#     print("Hai scelto 1D")
#     print("1. Statistiche base")
#     print("2. Analisi posizionale")
#     print("0. Torna indietro")

#     scelta = input("Scelta: ")
    
#     match scelta:
#         case "0":
#             return
#         case "1":
#             risultato = calcolaStatisticheBase(arrei)
#             print("Le statistiche base sono:", risultato)
#         case "2":
#             risultato = performaAnalisiPosizionale(arrei)
#             print("L'Analisi Posizionale è:", risultato)
#         case _:
#             print("")