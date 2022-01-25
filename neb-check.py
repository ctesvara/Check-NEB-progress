import pandas as pd
import numpy as np
import os
import subprocess
import matplotlib.pyplot as plt

print(os.getcwd())

subprocess.run(["sh", "get-fe-neb.sh"])

raw_1=pd.read_csv('01/fe-image-01.dat', names=['Steps','Forces','E','dE'], sep='\s+', engine='python')
raw_2=pd.read_csv('02/fe-image-02.dat', names=['Steps','Forces','E','dE'], sep='\s+', engine='python')
raw_3=pd.read_csv('03/fe-image-03.dat', names=['Steps','Forces','E','dE'], sep='\s+', engine='python')
raw_4=pd.read_csv('04/fe-image-04.dat', names=['Steps','Forces','E','dE'], sep='\s+', engine='python')
raw_5=pd.read_csv('05/fe-image-05.dat', names=['Steps','Forces','E','dE'], sep='\s+', engine='python')
raw_6=pd.read_csv('06/fe-image-06.dat', names=['Steps','Forces','E','dE'], sep='\s+', engine='python')
raw_7=pd.read_csv('07/fe-image-07.dat', names=['Steps','Forces','E','dE'], sep='\s+', engine='python')
raw_8=pd.read_csv('08/fe-image-08.dat', names=['Steps','Forces','E','dE'], sep='\s+', engine='python')

########################## CALCULATE BARRIERS ###########################

E_image0 = input('what is the initial E?')
ini_E = float(E_image0)

def normalize(x):
  return x-ini_E

raw_name = [raw_1, raw_2, raw_3, raw_4, raw_5, raw_6, raw_7, raw_8]

for raw in raw_name:
    raw['Barrier']=raw['E'].transform(normalize)


raw_comb = pd.concat(raw_name, keys=["1", "2", "3", "4", "5", "6", "7", "8"])

print(raw_comb)

raw_comb['Image'] = raw_comb.index.get_level_values(0)
raw_comb['Runs'] = raw_comb.index.get_level_values(1)

################## Retrieve Last step information #####################
last_run = pd.concat([raw_1.tail(1), raw_2.tail(1), raw_3.tail(1), raw_4.tail(1), raw_5.tail(1), raw_6.tail(1), raw_7.tail(1), raw_8.tail(1)])
last_run['Barrier']  = last_run['E'].transform(normalize)
last_run['Image'] = np.linspace(1,8,num=8)
last_run['Image'] = last_run['Image'].astype(str)

############################ ENERGY DATAFRAME #########################

ax = raw_comb.plot.scatter(x='Image', y='Barrier', c='Runs', colormap='viridis', linestyle='solid', title='Energy convergence')

plt.tight_layout()
plt.savefig("energy-neb.png")

ax2 = raw_comb.plot.scatter(x='Image', y='Forces', c='Runs', colormap='viridis', linestyle='-', title='Forces convergence', ylim=(0,1))

###################### PLOT THE LAST STEP OF NEB ####################
last_run.plot.line(x='Image', y='Barrier', ax=ax)
last_run.plot.line(x='Image', y='Forces', ax=ax2)


plt.tight_layout()
plt.show()

plt.savefig("forces-neb.png")
