"""
You will be supplied with two data files in CSV format. The first file contains
statistics about various dinosaurs. The second file contains additional data.

Given the following formula,

speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (gravitational constant)

Write a program to read in the data files from disk, it must then print the names
of only the bipedal dinosaurs from fastest to slowest. Do not print any other information.

$ cat dataset1.csv
NAME,LEG_LENGTH,DIET
Hadrosaurus,1.2,herbivore
Struthiomimus,0.92,omnivore
Velociraptor,1.0,carnivore
Triceratops,0.87,herbivore
Euoplocephalus,1.6,herbivore
Stegosaurus,1.40,herbivore
Tyrannosaurus Rex,2.5,carnivore

$ cat dataset2.csv
NAME,STRIDE_LENGTH,STANCE
Euoplocephalus,1.87,quadrupedal
Stegosaurus,1.90,quadrupedal
Tyrannosaurus Rex,5.76,bipedal
Hadrosaurus,1.4,bipedal
Deinonychus,1.21,bipedal
Struthiomimus,1.34,bipedal
Velociraptor,2.72,bipedal
"""

#!/usr/local/bin/python3 
import math

d1 = open('dataset1.csv')
d1.readline()
d2 = open('dataset2.csv')
d2.readline()

H1 = {}

for line in d2:
    line = line.strip()
    line = line.split(',')
    if line[2] == 'bipedal':
        H1.setdefault(line[0], [float(line[1])])

for line in d1:
    line = line.strip()
    line = line.split(',')
    try:
        H1[line[0]].append(float(line[1]))
    except Exception as e:
        pass

G = 9.8
speed = lambda x, y: (x / y - 1) * math.sqrt(y * G)

# H2 = {speed(v[0], v[1]): k for (k, v) in H1.items() if len(v) is 2}
# for i in sorted(H2.items(),reverse=True):
#     print(i[1],i[0])

H2 = {k: speed(v[0], v[1]) for (k, v) in H1.items() if len(v) is 2}

for dino in sorted(H2.items(), key=lambda x: x[1], reverse=True):
    print(dino[0])
