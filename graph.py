import ast
from matplotlib import pyplot

puntajes = []

with open('puntajes.dat') as puntajes_file:
    for line in puntajes_file:
        puntajes.append(ast.literal_eval(line))

for persona in puntajes:
    D = persona[list(persona.keys())[0]]
    if D['Total'] > 0:
        del(D['Total'])
        pyplot.bar(range(len(D)), D.values(), align='center')
        pyplot.xticks(range(len(D)), list(D.keys()))
        pyplot.title(list(persona.keys())[0])
        pyplot.savefig(list(persona.keys())[0])
        pyplot.clf()


