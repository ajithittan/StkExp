import spacy
#from spacy.lang.en import English

class runNLPonText:

    def analyzeText(self,inpData):
        nlp = spacy.load('en')
        doc = nlp(inpData)
        for ent in doc.ents:
            print(ent.text, ent.label_)

objRunNLP = runNLPonText()
objRunNLP.analyzeText("Humans are social animals and language is our primary tool to communicate with the society. But, what if machines could understand our language and then act accordingly? Natural Language Processing (NLP) is the science of teaching machines how to understand the language we humans speak and write.We recently launched an NLP skill test on which a total of 817 people registered. This skill test was designed to test your knowledge of Natural Language Processing. If you are one of those who missed out on this skill test, here are the questions and solutions.")
