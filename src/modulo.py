#!/usr/bin/python
#!encoding: UTF-8
import sys
import math

PI35DT=3.14159265358979311599796346854418516

def calcular_pi (n):
  
  PI35= 3.14159265358979311599796346854418516
  iniciointervalo=0
  suma=0
  intervalos=1.0/float(n)
  for i in range(n):
        x_i=((i+1)-1.0/2.0)/n
        fx_i=4.0/(1.0 + x_i*x_i)
        iniciointervalo+=intervalos
        suma+=fx_i
  aproximacion_pi=suma/n
  return(aproximacion_pi)
     
if(__name__=="__main__"):
  
  argumentos=sys.argv[1:]
  if(len(argumentos)==2):
      n=int(argumentos[0])
      aproxima=int(argumentos[1])
  else:
      print"Introduzca el nº de intervalos (n>0) : "
      n=int(raw_input())
      print"introduzca el nº de aproximaciones : "
      aproxima=int(raw_input())
      
  if(n>0):
    
    intervalo=n
    lista=[]
    for i in range(aproxima):
      valor=calcular_pi(intervalo)
      lista.append(valor)
      intervalo +=n
    
    print lista
    diferencia= []
    for i in range(aproxima):
      dif=abs(PI35DT-lista[i])
      diferencia.append(dif)
    print "i\tPI35DT\tlista i\tPI35DT-lista i"
    for i in range (aproxima):
      print"%d\t%1.10f\t%1.10f\t%1.10f" %(i+1,PI35DT,lista[i],diferencia[i])
    
    
  
  else:
    print "El valor de los intervalos debe ser mayor que 0"