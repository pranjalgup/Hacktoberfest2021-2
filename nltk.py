import nltk
from nltk import CFG

grammar = CFG.fromstring("""
 NP -> Art Nm | PN
 Nm -> Aj Nm | N
 VP -> V Aj | V NP | V S | V NP PP
 PP -> P NP
 PN -> 'Homer' | 'Abe' | 'Lisa'
 Art-> 'the' | 'a'
 N -> 'cat' | 'rat' | 'tree' | 'dolphin' | 'rope'
 Aj -> 'clever' | 'afraid' | 'small' | 'long'
 V -> 'tracked' | 'see' | 'said' | 'told' | 'is' | 'assumed'
 P -> 'in'
 """)
 
from nltk.parse import RecursiveDescentParser
rd = RecursiveDescentParser(grammar)
sentence = "Homer said Abe assumed the rope is small".split()
for t in rd.parse(sentence):
  print(t)
