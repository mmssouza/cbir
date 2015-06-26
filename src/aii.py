import pylab
import scipy
import cv2
import matplotlib.pyplot as plt

def AreaIntegralInvariant2(name,q,bg = 1):
 im = cv2.imread(name,0)
# Descomente caso imagem seja fundo branco
 if bg:
  im = cv2.bitwise_not(im)
 cnt,h = cv2.findContours(im.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
 aa = cv2.contourArea(cnt[0])
 r = int(scipy.sqrt(q*aa/scipy.pi))
 im_aux = scipy.zeros((im.shape[0]+2*r,im.shape[1]+2*r),dtype=im.dtype)
 im_aux[r:im_aux.shape[0]-r,r:im_aux.shape[1]-r] = im
 im = im_aux.copy()
 cnt,h = cv2.findContours(im_aux,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
 l = []

 for a in cnt[0]:
  c=(a[0][0],a[0][1])
  ee = scipy.zeros((2*r+1,2*r+1),dtype = im.dtype)
  cv2.circle(ee,(r,r),r,255,-1)
  im_roi = im[c[1]-r:c[1]+r+1,c[0]-r:c[0]+r+1]
  aux2 =cv2.bitwise_and(im_roi,ee)
  # pylab.figure(1)
  # pylab.subplot(221)
  # pylab.imshow(ee, cmap = "gray")
  # pylab.subplot(222)
  # pylab.imshow(aux2,cmap = "gray")
  # pylab.subplot(223)
  # pylab.imshow(im,cmap ="gray")
  # pylab.show()
  
#  pylab.figure(3)
#  pylab.imshow(aux2,cmap = "gray")  
  cnt2,h = cv2.findContours(aux2,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
  # im_aux = im.copy()
  # cv2.drawContours(im_aux[c[1]-r:c[1]+r+1,c[0]-r:c[0]+r+1],cnt2,-1,(125,125,125),thickness=-1)
  # pylab.imshow(im_aux,cmap = "gray")
  # pylab.show()
  area = 0
  for c in cnt2:
   area = area + cv2.contourArea(c)
#  print area
  l.append(area)
 # pylab.show()
  
 return scipy.array(l)/(q*aa)

def AreaIntegralInvariant(name,r):
 im = cv2.imread(name,0)
# Descomente caso imagem seja fundo branco
 im = cv2.bitwise_not(im)
 im_aux = scipy.zeros((im.shape[0]+2*r,im.shape[1]+2*r),dtype=im.dtype)
 im_aux[r:im_aux.shape[0]-r,r:im_aux.shape[1]-r] = im
 im = im_aux.copy()
 cnt,h = cv2.findContours(im_aux,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
 l = []
 for a in cnt[0]:
  c = a[0][0],a[0][1]
  aux = scipy.zeros(im.shape,dtype = im.dtype)
  cv2.circle(aux,c,r,255,-1)
  aux2 = cv2.bitwise_and(aux,im)
  # pylab.figure(2)
  # pylab.subplot(221)
  # pylab.imshow(aux,cmap="gray")
  # pylab.subplot(222)
  # pylab.imshow(im,cmap="gray")
  # pylab.subplot(223)
  # pylab.imshow(aux2,cmap="gray")
  # pylab.show()
  cnt2,h = cv2.findContours(aux2,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
  area = 0
  for c in cnt2:
   area = area + cv2.contourArea(c)
  l.append(area)

 return scipy.array(l)


