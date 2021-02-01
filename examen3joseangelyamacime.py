

importar  matplotlib . pyplot  como  plt
importar  numpy  como  np
de  la  importación  matemática sin , cos , radianes , sqrt

#NOTAS: Andaba media perdida con el examen pero mi compañero Daniel me ayudó y fue lo que me salió.

plt . eje ([ 0 , 150 , 100 , 0 ])
plt . eje ( 'encendido' )
plt . cuadrícula ( verdadero )
x = [ 40 , 30 , 80 , 75 ] # ——— avión
y = [ 60 , 10 , 60 , 40 ]
z = [ 0 , 0 , 0 , 0 ]

plt . plot ([ x [ 0 ], x [ 1 ]], [ y [ 0 ], y [ 1 ]], color = 'r' ) # —— plano de trazado A
plt . trama ([ x [ 1 ], x [ 2 ]], [ y [ 1 ], y [ 2 ]], color = 'r' )
plt . trama ([ x [ 2 ], x [ 0 ]], [ y [ 2 ], y [ 0 ]], color = 'r' )
plt . dispersión ( x [ 3 ], y [ 3 ], s = 20 , color = 'k' )
plt . plot ([ x [ 0 ], x [ 3 ]], [ y [ 0 ], y [ 3 ]], linestyle = ':' , color = 'k' ) #plot planes
plt . trama ([ x [ 1 ], x [ 3 ]], [ y [ 1 ], y [ 3 ]], estilo de línea = ':' , color = 'k' )
plt . trama ([ x [ 2 ], x [ 3 ]], [ y [ 2 ], y [ 3 ]], estilo de línea = ':' , color = 'k' )
plt . text ( 35 , 63 , '0' ) # —— etiquetar esquinas
plt . texto ( 25 , 10 , '1' )
plt . texto ( 83 , 63 , '2' )
plt . texto ( x [ 3 ] + 2 , y [ 3 ], '3' )
a = x [ 1 ] - x [ 0 ] # —— calcular dimensiones
b = y [ 1 ] - y [ 0 ]
c = z [ 1 ] - z [ 0 ]
Q01 = raíz cuadrada ( a * a + b * b + c * c )
a = x [ 2 ] - x [ 1 ]
b = y [ 2 ] - y [ 1 ]
c = z [ 2 ] - z [ 1 ]
Q12 = raíz cuadrada ( a * a + b * b + c * c )

a = x [ 2 ] - x [ 0 ]
b = y [ 2 ] - y [ 0 ]
c = z [ 2 ] - z [ 0 ]
Q02 = raíz cuadrada ( a * a + b * b + c * c )
a = x [ 1 ] - x [ 3 ]
b = y [ 1 ] - y [ 3 ]
c = z [ 1 ] = z [ 3 ]

Q13 = raíz cuadrada ( a * a + b * b + c * c )

a = x [ 2 ] - x [ 3 ]
b = y [ 2 ] - y [ 3 ]
c = z [ 2 ] - z [ 3 ]
Q23 = raíz cuadrada ( a * a + b * b + c * c )

a = x [ 0 ] - x [ 3 ]
b = y [ 0 ] - y [ 3 ]
c = z [ 0 ] - z [ 3 ]
Q03 = raíz cuadrada ( a * a + b * b + c * c )

s = ( Q01 + Q12 + Q02 ) / 2  # —— calcular las áreas A, A1 y A2
A = raíz cuadrada ( s * ( s - Q01 ) * ( s - Q12 ) * ( s - Q02 ))
s1 = ( Q01 + Q03 + Q13 ) / 2
A1 = raíz cuadrada ( s1 * ( s1 - Q01 ) * ( s1 - Q03 ) * ( s1 - Q13 ))

s2 = ( Q02 + Q23 + Q03 ) / 2
A2 = raíz cuadrada ( s2 * ( s2 - Q02 ) * ( s2 - Q23 ) * ( s2 - Q03 ))
plt . flecha ( 70 , 55 , 10 , 15 , ancho de línea = .5 , color = 'blue' ) # —— área de etiqueta A
plt . texto ( 82 , 73 , 'A' , color = 'k' )
plt . text ( 100 , 40 , 'A =' ) # —— salida del gráfico
dle = '% 7.0f' % ( A )
dls = str ( dle )
plt . texto ( 105 , 40 , dls )

plt . texto ( 100 , 45 , 'A1 =' , color = 'r' )
dle = '% 7.0f' % ( A1 )
dls = str ( dle )
plt . texto ( 105 , 45 , dls )
plt . texto ( 100 , 50 , 'A2 =' , color = 'r' )
dle = '% 7.0f' % ( A2 )
dls = str ( dle )
plt . texto ( 105 , 50 , dls )
plt . texto ( 91 , 55 , 'A1 + A2 =' , color = 'r' )
dle = '% 7.0f' % ( A1 + A2 )
dls = str ( dle )
plt . texto ( 106 , 55 , dls )
plt . texto ( 100 , 40 , 'A =' )
dle = '% 7.0f' % ( A )
dls = str ( dle )
plt . texto ( 105 , 40 , dls )
plt . texto ( 100 , 45 , 'A1 =' , color = 'r' )
dle = '% 7.0f' % ( A1 )
dls = str ( dle )
plt . texto ( 105 , 45 , dls )

plt . texto ( 100 , 50 , 'A2 =' , color = 'r' )
dle = '% 7.0f' % ( A2 )
dls = str ( dle )
plt . texto ( 105 , 50 , dls )

plt . texto ( 91 , 55 , 'A1 + A2 =' , color = 'r' )
dle = "% 7.0f" % ( A1 + A2 )
dls = str ( dle )
plt . texto ( 106 , 55 , dls )

si  A1 + A2  >  A :
    plt . texto ( 90 , 63 , 'FUERA DEL HOYO' , color = 'yellow' )
otra cosa :
    plt . texto ( 90 , 63 , 'DENTRO DEL HOYO' , color = 'yellow' )

plt . mostrar ()