#!/usr/bin/python3

import pickle
import re

nomes = {1:"apple",2:"bat",3:"beetle",4:"bell",5:"bird",6:"Bone",7:"bottle",8:"brick",9:"butterfly",10:"camel",
        11:"car",12:"carriage",13:"cattle",14:"cellular_phone",15:"chicken",16:"children",17:"chopper",18:"classic",19:"Comma",20:"crown",21:"cup",
        22:"deer",23:"device0",24:"device1",25:"device2",26:"device3",27:"device4",28:"device5",29:"device6",30:"device7" ,31:"device8",
        32:"device9",33:"dog",34:"elephant",35:"face",36:"fish",37:"flatfish",38:"fly",39:"fork",40:"fountain",41:"frog",
        42:"Glas",43:"guitar",44:"hammer",45:"hat",46:"HCircle",47:"Heart",48:"horse",49:"horseshoe",50:"jar",51:"key",52:"lizzard",53:"lmfish",
        54:"Misk",55:"octopus",56:"pencil",57:"personal_car",58:"pocket",59:"rat",60:"ray",61:"sea_snake",
        62:"shoe",63:"spoon",64:"spring",65:"stef",66:"teddy",67:"tree",68:"truck",69:"turtle",70:"watch"}

d = {}
flist = pickle.load(open("files.txt","rb"))
for c,n in nomes.items():
 r = re.compile("^"+n)
 for filename in flist:
  if r.search(filename):
   print(filename,c)
   d[filename] = c
f = open("classes.txt","wb")  
pickle.dump(d,f)
f.close()  
