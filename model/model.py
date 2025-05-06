import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self.idMap={}
        for c in DAO.getAllCountries():
            self.idMap[c.CCode]=c
        self.grafo=nx.Graph()

    def buildGraph(self, anno):
        self.grafo.clear()
        listaNodi=DAO.getCountriesAnno(anno)
        for s in listaNodi:
            oggetto=self.idMap[s]
            self.grafo.add_node(oggetto)

        listaArchi=DAO.getEdges(anno)
        for tupla in listaArchi:
            self.grafo.add_edge(self.idMap[tupla[0]],self.idMap[tupla[1]])

        gradi=self.getGrado()
        numConnesse=self.getInfoConnesse(self.grafo)

        return self.grafo, numConnesse, gradi

    def getInfoConnesse(self,grafo):
        conn=list(nx.connected_components(grafo))
        return len(conn)

    def getGrado(self):
        res=[]
        for node in self.grafo.nodes():
            tupla=(node,self.grafo.degree(node))
            res.append(tupla)
        res.sort(key=lambda x: x[0].StateAbb)
        return res

    def getNodiRaggiungibili(self,soruce):
        conn=nx.node_connected_component(self.grafo,soruce)
        conn.remove(soruce)
        return conn

