import numpy as np
import matplotlib
from matplotlib import pyplot as plt

def plotme():

	x=[1,2,3,4,5]
	y1=[1,1.28,1.96,1.88,1.24] #Tr=1
	y2=[1,1.61,2.03,2.14,1.95] #Tr=0.8
	y3=[1,1.39,1.74,2.27,2.33] #Tr=0.6
	y4=[1,1.36,1.80,1.9,2.51] #Tr=0.4
	y5=[1,1.50,1.79,2.2,2.5] #Tr=0.2
	y6=[1,1.38,1.76,2.05,2.30] #Tr=0.1


	NVcount=[31.,40.,71.,205.,292.]
	NVnorm=np.ones(len(NVcount))
	for i in range(1, len(NVcount)):
		NVnorm[i]=NVcount[i]/NVcount[0]

	
	plt.plot(x,y1,'-yo', label='Tr=1')	
	plt.plot(x,y2,'-bo', label='Tr=0.8')
	plt.plot(x,y3,'-go', label='Tr=0.6')
	plt.plot(x,y4,'-co', label='Tr=0.4')
	plt.plot(x,y5,'-mo', label='Tr=0.2')
	plt.plot(x,y6,'-ko', label='Tr=0.1')
	plt.plot(x,NVnorm,'--ro', label='Image counts')	
	plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)
	plt.xlabel('$z_0,\mu m$',fontsize=50)
	plt.ylabel('P',fontsize=20)
	plt.rc('xtick',labelsize=15)
	plt.rc('ytick',labelsize=15)
	plt.show()


plotme()