import numpy as np
import scipy.optimize as scp
import matplotlib.pyplot as plt

temp = np.array([85, 72, 66, 60, 56, 52, 49, 47, 44, 42, 40, 38, 35, 33, 31, 29, 28, 27, 26, 25, 24, 24, 23, 23, 22])
spiseglede = np.array([20, 40, 70, 80, 75, 70, 65, 55, 35, 30, 28, 26, 25, 25, 25, 25, 25, 25, 25, 45, 40, 30, 20, 15, 15])
tidMaalt = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74])
C = temp[0] - 22
def diffLikning(tid, alpha, konstant, romTemp):
    return romTemp + konstant * np.exp(-alpha * tid)

optimalVerdier, kovarians = scp.curve_fit(diffLikning, tidMaalt, temp, p0=[0.04, C, 22]) #Så en youtube video hvor svaret hans for en tekopp ble 0.0409, så satte min verdi nært
alphaOpt, C_Opt, romTempOpt = optimalVerdier

tidslinje = range(0, 75)
temp_modell = diffLikning(tidslinje, alphaOpt, C_Opt, romTempOpt)

plt.figure(figsize=(10, 8))
plt.plot(tidMaalt, temp, 'bo-')
plt.plot(tidslinje, temp_modell, 'r-')
plt.plot(tidMaalt, spiseglede, 'g-')
plt.xlabel('Minutter')
plt.ylabel('Temperatur (°C)')
plt.title('Frossenpizzaens nedkjøling')
plt.grid(True)

print(f'alpha = {alphaOpt:.5f} min⁻¹')
plt.show()