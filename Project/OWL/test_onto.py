from owlready import *

onto_path.append("./ontology")
onto = get_ontology("http://www.semanticweb.org/randhirsingh/ontologies/2017/4/retail.owl")
onto.load()

# per=[]
class Person(Thing):
	ontology = onto

class Actions(Thing):
	ontology = onto

class Appears_At_Exit(Actions):
	pass

class Appears_At_Entrance(Actions):
	pass

class act(Property):
	ontology = onto
	domain = [Person]
	range = [Actions]


per = Person("RandhirSingh")

action = Actions("sing")

per.act.append(action)

onto.save()