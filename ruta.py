def cargarMapa(ruta):
	return [x.split() for x in open(ruta, 'r')]

def inicio(mapa, x, y):
	if mapa[x][y]=='I':
		return (x, y)
	elif y < (len(mapa[x])-1):
		return inicio(mapa,x,y+1)
	elif x < (len(mapa)-1):
		return inicio(mapa,x+1,0)
	else:
		return "No se encontró inicio"

"""def fin(mapa, x, y):
	if mapa[x][y]=='F':
		return (x, y)
	elif y < (len(mapa[x])-1):
		return inicio(mapa,x,y+1)
	elif x < (len(mapa)-1):
		return inicio(mapa,x+1,0)
	else:
		return "No se encontró fin"
	"""
	
print(inicio(cargarMapa('lab.txt'),0,0))


