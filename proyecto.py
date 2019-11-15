import random
newMapa = []
for x in range(10):
  newMapa.append(["O"]*10)

def imprimirMapa(newMapa):
  for fila in newMapa: 
    print (" ".join(fila))

print ("Bienvenido a batalla naval!")
print ("")
imprimirMapa(newMapa)
opcion=eval(input("1.Para comenzar a jugar\n2.Salir\n"))

while(opcion<2 and opcion>=1):
  mapaPC=[]
  for x in range(10):
    mapaPC.append(["O"]*10)
  mapaDisparos = []

  for x in range(10):
    mapaDisparos.append(["O"]*10)
 
  def ubicarPortaAviones(newMapa):
    seUbico=False
    oriCorrecta=False
    ori=eval(input("En que orientacion desea ubicar el porta aviones? \n1.Vertical\n2.Horizontal\n")) 
    if(ori!=1 and ori!=2):
      ori=eval(input("Opcion no valida, intentalo de nuevo\n1.Vertical\n2.Horizontal\n"))
    if(ori==1 or ori==2):
      oriCorrecta=True
    if(oriCorrecta==True):
      while(seUbico==False):
        posx=eval(input("Ingrese la posicion x:\n"))
        posy=eval(input("Ingrese la posicion y:\n"))
        if(newMapa[posx][posy]==1):
          print("No puedes poner dos barcos en el mismo lugar")
        seUbico=False 
        if(posx>5 or posy>5):
          print("Esta ubicacion esta por fuera del mapa")
          seUbico=False
        if(newMapa[posx][posy]=="O"):
          if( ori==1):
                newMapa[posx][posy]=1
                newMapa[posx+1][posy]=1            
                newMapa[posx+2][posy]=1
                newMapa[posx+3][posy]=1
                newMapa[posx+4][posy]=1
                seUbico=True
          if(ori==2):         
                newMapa[posx][posy]=1
                newMapa[posx][posy+1]=1
                newMapa[posx][posy+2]=1
                newMapa[posx][posy+3]=1
                newMapa[posx][posy+4]=1
                seUbico=True  
    for x in newMapa:
      print(x)    

  def ubicarBuqueDeGuerra(newMapa):
    seUbico=False
    oriCorrecta=False
    ori=eval(input("En que orientacion desea ubicar el buque de guerra? \n1.Vertical\n2.Horizontal\n")) 
    if(ori!=1 and ori!=2):
      ori=eval(input("Opcion no valida, intentalo de nuevo\n1.Vertical\n2.Horizontal\n"))
    if(ori==1 or ori==2):
      oriCorrecta=True
    if(oriCorrecta==True):
      while(seUbico==False):
        posx=eval(input("Ingrese la posicion x:\n"))
        posy=eval(input("Ingrese la posicion y:\n"))
        if(newMapa[posx][posy]==1):
          print("No puedes poner dos barcos en el mismo lugar")
        seUbico=False 
        if(posx>6 or posy>6):
          print("Esta ubicacion esta por fuera del mapa")
          seUbico=False
        if(newMapa[posx][posy]=="O"):
          if( ori==1):
                newMapa[posx][posy]=1
                newMapa[posx+1][posy]=1            
                newMapa[posx+2][posy]=1
                newMapa[posx+3][posy]=1
                seUbico=True
          if(ori==2):         
                newMapa[posx][posy]=1
                newMapa[posx][posy+1]=1
                newMapa[posx][posy+2]=1
                newMapa[posx][posy+3]=1
                seUbico=True  
    for x in newMapa:
      print(x)

  def ubicarCrucero(newMapa):
    seUbico=False
    oriCorrecta=False
    ori=eval(input("En que orientacion desea ubicar el crucero? \n1.Vertical\n2.Horizontal\n")) 
    if(ori!=1 and ori!=2):
      ori=eval(input("Opcion no valida, intentalo de nuevo\n1.Vertical\n2.Horizontal\n"))
    if(ori==1 or ori==2):
      oriCorrecta=True
    if(oriCorrecta==True):
      while(seUbico==False):
        posx=eval(input("Ingrese la posicion x:\n"))
        posy=eval(input("Ingrese la posicion y:\n"))
        if(newMapa[posx][posy]==1):
          print("No puedes poner dos barcos en el mismo lugar")
        seUbico=False 
        if(posx>7 or posy>7):
          print("Esta ubicacion esta por fuera del mapa")
          seUbico=False
        if(newMapa[posx][posy]=="O"):
          if( ori==1):
                newMapa[posx][posy]=1
                newMapa[posx+1][posy]=1            
                newMapa[posx+2][posy]=1
                seUbico=True
          if(ori==2):         
                newMapa[posx][posy]=1
                newMapa[posx][posy+1]=1
                newMapa[posx][posy+2]=1
                seUbico=True  
    for x in newMapa:
      print(x)
   
  def ubicarSubmarino(newMapa):
    seUbico=False
    oriCorrecta=False
    ori=eval(input("En que orientacion desea ubicar el submarino? \n1.Vertical\n2.Horizontal\n")) 
    if(ori!=1 and ori!=2):
      ori=eval(input("Opcion no valida, intentalo de nuevo\n1.Vertical\n2.Horizontal\n"))
    if(ori==1 or ori==2):
      oriCorrecta=True
    if(oriCorrecta==True):
      while(seUbico==False):
        posx=eval(input("Ingrese la posicion x:\n"))
        posy=eval(input("Ingrese la posicion y:\n"))
        if(newMapa[posx][posy]==1):
          print("No puedes poner dos barcos en el mismo lugar")
        seUbico=False
        if(posx>7 or posy>7):
          print("Esta ubicacion esta por fuera del mapa")
          seUbico=False 
        if(newMapa[posx][posy]=="O"):
          if( ori==1):
                newMapa[posx][posy]=1
                newMapa[posx+1][posy]=1            
                newMapa[posx+2][posy]=1
                seUbico=True
          if(ori==2):         
                newMapa[posx][posy]=1
                newMapa[posx][posy+1]=1
                newMapa[posx][posy+2]=1
                seUbico=True  
    for x in newMapa:
      print(x)
   

  def ubicarDestructor(newMapa):
    seUbico=False
    oriCorrecta=False
    ori=eval(input("En que orientacion desea ubicar el destructor? \n1.Vertical\n2.Horizontal\n")) 
    if(ori!=1 and ori!=2):
      ori=eval(input("Opcion no valida, intentalo de nuevo\n1.Vertical\n2.Horizontal\n"))
    if(ori==1 or ori==2):
      oriCorrecta=True
    if(oriCorrecta==True):
      while(seUbico==False):
        posx=eval(input("Ingrese la posicion x:\n"))
        posy=eval(input("Ingrese la posicion y:\n"))
        if(newMapa[posx][posy]==1):
          print("No puedes poner dos barcos en el mismo lugar")
        seUbico=False 
        if(posx>8 or posy>8):
          print("Esta ubicacion esta por fuera del mapa")
          seUbico=False
        if(newMapa[posx][posy]=="O"):
          if( ori==1):
                newMapa[posx][posy]=1
                newMapa[posx+1][posy]=1            
                
                seUbico=True
          if(ori==2):         
                newMapa[posx][posy]=1
                newMapa[posx][posy+1]=1
                
                seUbico=True  
    for x in newMapa:
      print(x)
   
  
  def ubicarPortaAvionesPC(mapaPC):
    ori=random.randint(1,2)
    if(ori==1 or ori==2):
      posx=random.randint(0,5)
      posy=random.randint(0,5)
      if( ori==1):
          mapaPC[posx][posy]=1
          mapaPC[posx+1][posy]=1
          mapaPC[posx+2][posy]=1
          mapaPC[posx+3][posy]=1
          mapaPC[posx+4][posy]=1
         
      if(ori==2):
        mapaPC[posx][posy]=1
        mapaPC[posx][posy+1]=1
        mapaPC[posx][posy+2]=1
        mapaPC[posx][posy+3]=1
        mapaPC[posx][posy+4]=1
    for x in mapaPC:
        print(x)

  def ubicarBuqueDeGuerraPC(newMapa):
    ori=random.randint(1,2)
    if(ori==1 or ori==2):
      posx=random.randint(0,6)
      posy=random.randint(0,6)
      if( ori==1):
          mapaPC[posx][posy]=1
          mapaPC[posx+1][posy]=1
          mapaPC[posx+2][posy]=1
          mapaPC[posx+3][posy]=1
                  
      if(ori==2):
        mapaPC[posx][posy]=1
        mapaPC[posx][posy+1]=1
        mapaPC[posx][posy+2]=1
        mapaPC[posx][posy+3]=1
    for x in mapaPC:
        print(x)

  def ubicarCruceroPC(newMapa):
    ori=random.randint(1,2)
    if(ori==1 or ori==2):
      posx=random.randint(0,7)
      posy=random.randint(0,7)
      if( ori==1):
          mapaPC[posx][posy]=1
          mapaPC[posx+1][posy]=1
          mapaPC[posx+2][posy]=1
          
                  
      if(ori==2):
        mapaPC[posx][posy]=1
        mapaPC[posx][posy+1]=1
        mapaPC[posx][posy+2]=1
    for x in mapaPC:
        print(x)
  
  def ubicarSubmarinoPC(newMapa):
    ori=random.randint(1,2)
    if(ori==1 or ori==2):
      posx=random.randint(0,7)
      posy=random.randint(0,7)
      if( ori==1):
          mapaPC[posx][posy]=1
          mapaPC[posx+1][posy]=1
          mapaPC[posx+2][posy]=1
          
                  
      if(ori==2):
        mapaPC[posx][posy]=1
        mapaPC[posx][posy+1]=1
        mapaPC[posx][posy+2]=1
    for x in mapaPC:
        print(x)

  def ubicarDestructorPC(newMapa):
    
    ori=random.randint(1,2)
    if(ori==1 or ori==2):
      posx=random.randint(0,8)
      posy=random.randint(0,8)
      if( ori==1):
          mapaPC[posx][posy]=1
          mapaPC[posx+1][posy]=1
          
                  
      if(ori==2):
        mapaPC[posx][posy]=1
        mapaPC[posx][posy+1]=1
    for x in mapaPC:
        print(x)

  def disparar(newMapa):
    cantDisparos=0
    hayGanador=False
    tusBarcos=5
    barcosPC=5
    while (hayGanador==False):
      disparo=False
      disparoPC=False
      while(disparo==False):
        posx= eval(input("Digita la fila a la que quieres disparar\n"))
        posy = eval(input("Digita la columna a la que quieres disparar\n"))
        print("'X' representa los tiros acertados")
        print("'@' representa los tiros fallidos")
        if (mapaDisparos[posx][posy]=="x" or mapaDisparos[posx][posy]=="@" ):
            print("Ya disparaste en este lugar")
            disparo=False
        else:
          try:
            if(mapaPC[posx][posy]==1):
              mapaDisparos[posx][posy]="x"
              print("PC:Hundiste mi barco!")
              barcosPC-=1
              disparo=True
            else:
              mapaDisparos[posx][posy]="@"
              print("PC:Le diste!....pero al agua")
              disparo=True
          
          except IndexError:
            print("PC:Tu disparo fue tan potente que se salio del mapa!")
          except NameError:
            print("Esta coordenada no es valida, intentalo nuevamente")
      while(disparoPC==False):
        posx=random.randint(0,9)
        posy=random.randint(0,9)
        if(newMapa[posx][posy]==1):
          print("El PC hundio tu barco")
          tusBarcos-=1
          disparoPC=True
        else:
          print("El PC falló")
          disparoPC=True
      tusPartidasGanadas=0
      partidasPC=0
      if(barcosPC==0):
        print("Felicidades, ganaste la partida")
        tusPartidasGanadas+=1
        hayGanador=True
      if(tusBarcos==0):
        print("El PC ha ganado la partida")
        partidasPC+=1
        hayGanador=True
      print("Tus barcos "+str(tusBarcos))
      print("Los barcos rivales"+str(barcosPC))
    for fila in mapaDisparos: 
      print (" ".join(fila))
  
  print(ubicarPortaAviones(newMapa))
  print(ubicarBuqueDeGuerra(newMapa))
  print(ubicarCrucero(newMapa))
  print(ubicarSubmarino(newMapa))
  print(ubicarDestructor(newMapa))
  print(disparar(newMapa))
  print("Llevas "+str(tusPartidasGanadas)+ "y el PC lleva "+str(partidasPC))
  