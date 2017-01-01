from owlready import *

onto_path.append("./ontology")
onto = get_ontology("http://www.semanticweb.org/randhirsingh/ontologies/2017/4/retail.owl")
onto.load()

per_count = 0
per = []

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


while True:
	data = sys.stdin.readline().strip()
	if data == "":
		break
	ev = data.split(" ")

	if ev[0] == "Person":
		per_num = int(ev[1])
		if len(per) < per_num:
			per.append(Person())
		action = None
		if ev[2] == "at":
			print(data)
			action = Actions(" ".join(ev[3:]))
		elif ev[2] == "direction":
			print(data)
			action = Actions(" ".join(ev[3:]))
		elif ev[2] == "moving":
			print(data)
			action = Actions(" ".join(ev[3:]))
			

		if action != None:
			(per[per_num-1]).act.append(action)



onto.save()
	
