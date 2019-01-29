'''

1 1 1 1 1 1 1 1 1
1 I 1 0 0 0 0 0 1
1 0 1 1 0 1 1 F 1
1 0 1 0 0 1 1 1 1
1 0 1 1 0 1 1 1 1
1 0 0 0 0 0 0 1 1
1 1 1 1 1 1 1 1 1


'''

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
		

def fin(mapa, x, y):
	if mapa[x][y]=='F':
		return (x, y)
	elif y < (len(mapa[x])-1):
		return fin(mapa,x,y+1)
	elif x < (len(mapa)-1):
		return fin(mapa,x+1,0)
	else:
		return "No se encontró fin"
	

def ruta(mapa, ini, ant, rec):
	print(mapa[ini[0]][ini[1]])
	print(mapa[ini[0]][ini[1]-1])
	print(mapa[ini[0]][ini[1]+1])
	print(mapa[ini[0]-1][ini[1]])
	print(mapa[ini[0]+1][ini[1]])
	print(rec)
	if mapa[ini[0]][ini[1]]=='F':
		print("primer if")
		print(ini)
		print(rec)
		return True
	#Movimiento hacia la izquierda
	elif (mapa[ini[0]][ini[1]-1]=='0' or mapa[ini[0]][ini[1]-1]=='F') and (ini[0],ini[1]-1) != ant:
		print("segundo if")
		print(ini)
		rec.append(ini)
		return ruta(mapa, (ini[0],ini[1]-1), ini, rec)
	#Movimiento hacia la derecha
	elif (mapa[ini[0]][ini[1]+1]=='0' or mapa[ini[0]][ini[1]+1]=='F') and (ini[0],ini[1]+1) != ant:
		print("tercer if")
		print(ini)
		rec.append(ini)
		return ruta(mapa, (ini[0],ini[1]+1), ini, rec)
	#Movimiento hacia arriba
	elif (mapa[ini[0]-1][ini[1]]=='0' or mapa[ini[0]-1][ini[1]]=='F') and (ini[0]-1,ini[1]) != ant:
		print("cuarto if")
		print(ini)
		rec.append(ini)
		return ruta(mapa, (ini[0]-1,ini[1]), ini, rec)
	#Movimiento hacia abajo
	elif (mapa[ini[0]+1][ini[1]]=='0' or mapa[ini[0]+1][ini[1]]=='F') and (ini[0]+1,ini[1]) != ant:
		print("quinto if")
		print(ini)
		rec.append(ini)
		return ruta(mapa, (ini[0]+1,ini[1]), ini, rec)
	else:
		print("else")
		print(ini)
		print(rec)
		return False


#print(inicio(cargarMapa('lab.txt'),0,0))
print(ruta(cargarMapa('lab.txt'),inicio(cargarMapa('lab.txt'),0,0),(0,0),[]))


