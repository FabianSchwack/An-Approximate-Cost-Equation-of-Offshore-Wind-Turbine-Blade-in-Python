# Equations from:
# 2020
# Majhi, C. K., Nanda, S., Pradhan, R. C., & Mohapatra, B. G.
# An Approximate Cost Equation of Offshore Wind Turbine Blade
# In Recent Developments in Sustainable Infrastructure (pp. 973-983). Springer, Singapore.
# https://link.springer.com/chapter/10.1007%2F978-981-15-4577-1_81

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import sys

# Input data
# rotor radius [m]
R=range(10,41)
np_R=np.array(R)

# quantities of material
quantity_of_fiberglass=0.1121*(2*np_R)**2.95
quantity_of_core=0.0083*(2*np_R)**2.95
quantity_of_resin=0.0509*(2*np_R)**2.97
quantity_of_adhesive=0.1541*(2*np_R)**1.84
quantity_of_rootstud=0.0006*(2*np_R)**3.41

# side calculation of weight
weight=quantity_of_fiberglass+quantity_of_rootstud+\
       quantity_of_resin+quantity_of_adhesive+\
       quantity_of_core

# costs given in rupie/kg (https://www.finanzen.net/devisen/euro-indische_rupie-kurs 29.09.2020)
rupie_2020=1
euro_2020=0.0116
course=rupie_2020/euro_2020

# material prices
cost_fiberglass=300/course
cost_core=775/course
cost_resin=1552/course
cost_adhesive=4146/course
cost_rootstud=350/course

blade_cost=(quantity_of_fiberglass*cost_fiberglass+\
           quantity_of_core*cost_core+\
           quantity_of_resin*cost_resin+\
           quantity_of_adhesive*cost_adhesive+\
           cost_rootstud*quantity_of_rootstud)

plt.plot(R, blade_cost)
plt.xlabel('Rotor radius [m]')
plt.ylabel('Blade cost [€]')
plt.show()

