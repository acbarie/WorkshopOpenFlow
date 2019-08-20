from pylive import live_plotter
import numpy as np
import time, sys
import redis

rd = redis.Redis(host='localhost', port=6379, db=0)
argval = sys.argv[1]
prmval = int(sys.argv[2])
size = 100
x_vec = np.linspace(0,1,size+1)[0:-1]
y_vec = np.random.randn(len(x_vec))
line1 = []

while True:
	yval = []
	xval = []
	maxlist = rd.llen(argval)
	for i in range(maxlist-10,maxlist):
		strval = rd.lindex(argval,i)
		print strval
		yval.append(int( strval.split(",")[prmval] ))
		xval.append(i)
	#rand_val = np.random.randn(1)
	#y_vec[-1] = rand_val
	x_vec = np.array(xval)
	y_vec = np.array(yval)
	line1 = live_plotter(x_vec,y_vec,line1)
	y_vec = np.append(y_vec[1:],0.0)
	time.sleep(0.5)