

import sys
#input
summe = input(f'''Print the sum of the number of vertices, edges, and faces:''')
#is the number round?
try:
    summe = int(summe)
except ValueError:
    print('The input is not a valid integer.')
    sys.exit()

if (summe - 2) % 4 != 0:
    print('The number is not valid.')
    sys.exit()
∂
#the finding von N
#the finding von N
#the finding v
siedes_pyramid = (int(summe) - 2) / 4
print('N is :' + str(siedes_pyramid))
#sides and...
vertices = int(siedes_pyramid) + 1
print('Vertices:' + str(vertices))

edges = 2 * int(siedes_pyramid)
print('edges:' + str(edges))

faces = int(siedes_pyramid) + 1
print('faces:' + str(faces))
