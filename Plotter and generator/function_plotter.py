import matplotlib.pyplot as plt

x,y = [],[]

arq_name = "dados.txt"
arq = open(arq_name,"r")
arq_full_data = arq.readlines()

for sample in arq_full_data:
    sample_x,sample_y = map(int,sample.split(","))
    x.append(sample_x)
    y.append(sample_y)

plt.plot(x,y)
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.savefig(arq_name.replace('.txt','.png'),dpi=300)
plt.clf()