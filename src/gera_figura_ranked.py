#!/usr/bin/python
from PIL import Image

sz = (1200,1200)
tsize = (25,25)
x_spacing = 5
y_spacing = 5
loc_x = 20
loc_y = 20
diretorio = "../Artigo/gerar_caracteristicas/99shapes/"

l = [a.split() for a in open("ranked_kimia99.txt")]

im = Image.new("L",sz,"white")

x = loc_x
y = loc_y
i = 0
for aa in l:
 i = i + 1
 for nome in aa[1:]: 
  aux = Image.open(diretorio+nome)
  aux.thumbnail(tsize,Image.ANTIALIAS)
  im.paste(aux,(x,y))
  x = x + aux.size[0] + x_spacing
 y = y + aux.size[1] + y_spacing
 if (i == 40) or (i == 79):
  y = loc_y

 if i in range(40):
  x = loc_x
 elif i in range(40,80):
  x = loc_x + sz[0]/3
 else:
  x = loc_x + 2*sz[0]/3
     
im.save("Resultado_Kimia99.eps")
im.show()
