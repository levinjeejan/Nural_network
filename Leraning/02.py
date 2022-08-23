Inputs = [1,2,3,2.5]

weights1 = [0.2,0.8,-0.5,1.0]
weights2 = [0.5,-0.9,0.26,-0.5]
weights3 = [-0.26,-0.27,0.17,0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5

output = [Inputs[0]*weights1[0]+  Inputs[1]*weights1[1]+  Inputs[2]*weights1[2]+ Inputs[3]*weights1[3]+ bias1,
          Inputs[0]*weights2[0]+  Inputs[1]*weights2[1]+  Inputs[2]*weights2[2]+ Inputs[3]*weights2[3]+ bias2,
          Inputs[0]*weights3[0]+  Inputs[1]*weights3[1]+  Inputs[2]*weights3[2]+ Inputs[3]*weights3[3]+ bias3]
print(output)
