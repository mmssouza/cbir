
dataset_path = '../datasets/1400_mpeg7/'
temp_path = "/dev/shm/"

N_Threads = 4 

#distancia = "Hellinger"
#distancia = "Jensen Shannon"
#distancia = "Patrick Fisher"
distancia = "Chi Square"

Niter = 220


#algo = "sa"
#params = (90,0.95,4,2)

algo = "de"
params = (50,0.35,0.65)

Nretr = 20
