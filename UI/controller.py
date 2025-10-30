import flet as ft
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''


class Controller:
    def __init__(self, view: View, model: Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO
    def mostra_automobili(self, e):

        self._view.lista_auto.controls.clear()
        lista_auto = self._model.get_automobili()

        if lista_auto is None:
            self._view.show_alert("Errore di connessione al database o di lettura dei dati.")
        elif len(lista_auto) == 0:
            self._view.lista_auto.controls.append(
                ft.Text("Nessuna automobile trovata nel database.", weight=ft.FontWeight.BOLD))
        else:
            for auto in lista_auto:
                self._view.lista_auto.controls.append(
                    ft.Text(f"{auto}")
                )

        self._view.update()

    def cerca_automobili(self, e):

        modello_cercato = self._view.input_modello_auto.value
        self._view.lista_auto_ricerca.controls.clear()

        if not modello_cercato:
            self._view.show_alert("Inserisci un modello da cercare!")
            self._view.update()
            return

        lista_auto_cercate = self._model.cerca_automobili_per_modello(modello_cercato)

        if lista_auto_cercate is None:
            self._view.show_alert("Errore di connessione al database o di ricerca dei dati.")
        elif len(lista_auto_cercate) == 0:
            self._view.lista_auto_ricerca.controls.append(
                ft.Text(f"Nessuna automobile trovata per il modello '{modello_cercato}'.", weight=ft.FontWeight.BOLD)
            )
        else:
            for auto in lista_auto_cercate:
                self._view.lista_auto_ricerca.controls.append(
                    ft.Text(str(auto))
                )

        self._view.update()