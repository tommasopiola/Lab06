from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''


class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """
        cnx = get_connection()
        result = []
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = "SELECT codice, marca, modello, anno, posti, disponibile FROM automobile"

            try:
                cursor.execute(query)
                for row in cursor:
                    auto = Automobile(
                        codice=row["codice"],
                        marca=row["marca"],
                        modello=row["modello"],
                        anno=row["anno"],
                        posti=row["posti"],
                        disponibile=bool(row["disponibile"])
                    )
                    result.append(auto)
                cursor.close()
                cnx.close()
                return result
            except Exception as e:
                print(f"Errore durante l'esecuzione della query (get_automobili): {e}")
                cursor.close()
                cnx.close()
                return None
        else:
            print("Errore di connessione al database (get_automobili)")
            return None

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        cnx = get_connection()
        result = []
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = "SELECT codice, marca, modello, anno, posti, disponibile FROM automobile WHERE modello = %s"

            try:
                cursor.execute(query, (modello,))
                for row in cursor:
                    auto = Automobile(
                        codice=row["codice"],
                        marca=row["marca"],
                        modello=row["modello"],
                        anno=row["anno"],
                        posti=row["posti"],
                        disponibile=bool(row["disponibile"])
                    )
                    result.append(auto)
                cursor.close()
                cnx.close()
                return result
            except Exception as e:
                print(f"Errore durante l'esecuzione della query (cerca_automobili_per_modello): {e}")
                cursor.close()
                cnx.close()
                return None
        else:
            print("Errore di connessione al database (cerca_automobili_per_modello)")
            return None