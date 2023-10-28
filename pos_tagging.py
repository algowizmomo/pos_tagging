import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp("monisha loves vishnu and vishnu loves to eat momos in delhi")
print(doc.text)
print(doc[2])
print(doc[2].pos_)
