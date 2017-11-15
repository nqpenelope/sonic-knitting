import numpy as np

a = np.array([0.00, 440.00])
b = np.array([0.00, 493.88])

knit = np.tile(a, 8)
purl = np.tile(b, 8)

stitches = np.append(knit, purl)

row = np.tile(stitches, 4)

#generate pattern
row_twenty = np.resize(row,(20, 126))

#prep 2D arrays
for x, y in enumerate(row_twenty):
	rowy = np.tile(y, 20)
	if x>0:
		c = x*126
		rowy[:c] = 0
	rowyv = np.transpose(rowy)
	filename = "row"+str(x+1)+".csv"
	np.savetxt(filename, rowyv, delimiter = ",")
