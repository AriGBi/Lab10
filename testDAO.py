from model.model import Model

mymodel = Model()
#print(mymodel.idMap)
grafo=mymodel.buildGraph(1980)
print(mymodel.getInfoConnesse(grafo))
