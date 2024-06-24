x = 1
y = 1
z = 1
n = 2
print([[i, j, k] for i in [ l for l in range(x+1) ] for j in [ m for m in range(y+1) ] for k in [ n for n in range(z+1) ] if i+j+k != n])
