#!/usr/bin/env python2
#encoding: UTF-8

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import sys
import pylab
import cPickle
from Patrick_Fisher import Patrick_Fisher
from chi_square import chi_square
from dkl import D_KL
from hellinger import He
from jsd import jsd
from skimage import io
import matplotlib.pyplot as PLT
from matplotlib.offsetbox import AnnotationBbox, OffsetImage

distances = {"Hellinger":He,"Patrick Fisher":Patrick_Fisher,
             "chi square":chi_square,"Jensen Shannon":jsd,
             "Kulback Leiben":D_KL}
subplots = [231,232,233,234,235]
path = "../leaves_160_png/"
images = ["1281.png","1283.png","1300.png","1303.png","1319.png","1386.png","1397.png","1409.png","1412.png","1429.png"]
#images=["1062.png","1073.png","1097.png","1103.png","1114.png","1146.png","1172.png","1186.png","1188.png","1189.png"]
#images=["3451.png","3462.png","3469.png","3480.png","3496.png","1146.png","1172.png","1186.png","1188.png","1189.png"]
coords_l = [(0,10),(1,10),(2,10),(3,10),(4,10),(5,10),(6,10),(7,10),(8,10),(9,10),(10,10)]
coords_c = [(10,0),(10,1),(10,2),(10,3),(10,4),(10,5),(10,6),(10,7),(10,8),(10,9),(10,10)]
def plota(ax,data,distance,distance_name):
 p = pdist(data,distance)
 p = (127*(p/p.max())+0).astype(int)
 p = pylab.vstack((p,pylab.full((1,p.shape[0]),127)))
 p = pylab.hstack((p,pylab.full((p.shape[0],1),127)))

 PLT.gray()
 PLT.imshow(p)
 for im,cl,cc in zip(images,coords_l,coords_c):
 # add a first image
  img = io.imread(path+im)
  imagebox = OffsetImage(pylab.array(img), zoom=.25)
  xy = [cl[0],cl[1]]               # coordinates to position this image
  ab = AnnotationBbox(imagebox, xy,
      xybox=(5., -5.),
      xycoords='data',
      boxcoords="offset points",
	  frameon = False)                                  
  ax.add_artist(ab)
  xy = [cc[0],cc[1]]               # coordinates to position this image
  ab = AnnotationBbox(imagebox, xy,
      xybox=(5., -5.),
      xycoords='data',
      boxcoords="offset points",
	  frameon = False)                                  
  ax.add_artist(ab)

 ax.grid(False)
 ax.set_title(distance_name,{'verticalalignment':'center'})
 ax.axis("off") 
 PLT.draw()

def pdist(data,dist_func):
 N = data.shape[0]
 p = pylab.zeros((N,N))
 for i,a in zip(pylab.arange(N),data):
   for j,b in zip(pylab.arange(N),data):
    # Curvatura
    d1 = dist_func(a[0],b[0])
    # angle signature
    d2 = dist_func(a[1],b[1])
    # Centroid distance
    d3 = dist_func(a[2],b[2])
    # Area integral invariant
    d4 = dist_func(a[3],b[3])
    # distância da forma i para a forma j
    #p[i,j] = d1+d2+d3+d4
    p[i,j] = 0.4*d1+0.4*d2+0.2*d3+0.*d4
 return p

if __name__ == "__main__":
# curvature signature    
  db1 = cPickle.load(open(sys.argv[1]))
# Angle sequence signature
  db2 = cPickle.load(open(sys.argv[2]))
# Centroid distance
  db3 = cPickle.load(open(sys.argv[3]))
# Area integral invariant
  db4 = cPickle.load(open(sys.argv[4]))  

data = pylab.array([(db1[i][1:],db2[i][1:],db3[i][1:],db4[i][1:]) for i in images])

fig = PLT.figure(figsize=(10,10), dpi = 300)
fig.clf()
PLT.subplots_adjust(left=0.0, right=1., bottom=0.05, top=.95)
for aux,d,dname in zip(subplots,distances.values(),distances.keys()):
 ax = PLT.subplot(aux)
 plota(ax,data,d,dname)

PLT.savefig(sys.argv[5],bbox_inches='tight' )
#PLT.show()

