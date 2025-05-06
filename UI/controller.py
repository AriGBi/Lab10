import flet as ft
import networkx as nx

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.ddCountryValue=None

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        annoInput=self._view._txtAnno.value
        if annoInput=="" or annoInput==None:
            self._view._txt_result.controls.append(ft.Text("Inserire un anno", color="red"))
            self._view.update_page()
            return
        try:
            annoInt=int(annoInput)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Inserire un numero valido", color="red"))
            self._view.update_page()
            return

        if annoInt<1816 or annoInt>2006:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Inserire un numero compreso tra 1816-2006", color="red"))
            self._view.update_page()
            return

        grafo, numConnesse, gradi= self._model.buildGraph(annoInt)
        self._view._txt_result.controls.append(ft.Text("Grafo creato correttamente."))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {numConnesse} componenti connesse."))
        self._view._txt_result.controls.append(ft.Text(f"Di seguito il dettaglio sui nodi: "))
        for tupla in gradi:
            self._view._txt_result.controls.append(ft.Text(f"{tupla[0].StateNme} -- {tupla[1]} vicini."))

        self._view._ddStati.disabled = False
        self._view._btnraggiungibili.disabled = False
        self.fillDD(grafo)
        self._view.update_page()

    def fillDD(self,grafo):
        for node in grafo.nodes():
            self._view._ddStati.options.append(ft.dropdown.Option(key=node.CCode, text=node.StateNme, data=node, on_click=self.read_states))

        self._view._ddStati.options.sort(key=lambda x: x.data.StateNme)

    def read_states(self,e):
        self.ddCountryValue=e.control.data

    def handleRaggiungibili(self,e):
        statoScelto=self.ddCountryValue
        if statoScelto is None:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Scegli uno Stato"))
            self._view.update_page()
            return
        raggiungibili=self._model.getNodiRaggiungibili(statoScelto)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"I nodi raggiungibili a partire da {statoScelto.StateNme} sono:"))
        if len(raggiungibili)==0:
            self._view._txt_result.controls.append(ft.Text(f"Non ci sono stati raggiungibili"))
        for node in raggiungibili:
            self._view._txt_result.controls.append(ft.Text(f"- {node.StateNme}"))
        self._view.update_page()
        return

