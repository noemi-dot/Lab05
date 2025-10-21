class Automobile:
    def __init__(self, codice, marca, modello, anno, posti, disponibile=True):
        self.codice = codice
        self.marca = marca
        self.modello = modello
        self.anno = int(anno)
        self.posti = int(posti)
        self.disponibile = disponibile

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Noleggiata"
        return f"{self.codice} | {self.marca} {self.modello} ({self.anno}) | {self.posti} posti | {stato}"

    def __repr__(self):
        stato = "Disponibile" if self.disponibile else "Noleggiata"
        return f"{self.codice} | {self.marca} {self.modello} ({self.anno}) | {self.posti} posti | {stato}"