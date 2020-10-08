# Equations from:
# 2020
# Majhi, C. K., Nanda, S., Pradhan, R. C., & Mohapatra, B. G.
# An Approximate Cost Equation of Offshore Wind Turbine Blade
# In Recent Developments in Sustainable Infrastructure (pp. 973-983). Springer, Singapore.
# https://link.springer.com/chapter/10.1007%2F978-981-15-4577-1_81

import numpy as np
import exchange

# Input data
# rotor radius [m]
r = range(10, 41)


def cost():
    np_r = np.array(r)

    quantity_of_fiberglass = 0.1121 * (2 * np_r) ** 2.95
    quantity_of_core = 0.0083 * (2 * np_r) ** 2.95
    quantity_of_resin = 0.0509 * (2 * np_r) ** 2.97
    quantity_of_adhesive = 0.1541 * (2 * np_r) ** 1.84
    quantity_of_rootstud = 0.0006 * (2 * np_r) ** 3.41

    # in rupie_2020
    cost_fiberglass = 300
    cost_core = 775
    cost_resin = 1552
    cost_adhesive = 4146
    cost_rootstud = 350

    cost_calc = \
        (quantity_of_fiberglass * cost_fiberglass +
         quantity_of_core * cost_core +
         quantity_of_resin * cost_resin +
         quantity_of_adhesive * cost_adhesive +
         cost_rootstud * quantity_of_rootstud) / exchange.rupie2020_euro2020()

    return cost_calc

# plt.plot(R, blade_cost)
# plt.xlabel('Rotor radius [m]')
# plt.ylabel('Blade cost [€]')
# plt.show()
