# Python Program to Calculate Time Response of a Second-Order System
#
# Standard Transfer Function:
# G(s) = wn^2 / (s^2 + 2*zeta*wn*s + wn^2)

import numpy as np
import matplotlib.pyplot as plt

print("========================================")
print("   SECOND-ORDER SYSTEM TIME RESPONSE")
print("========================================")

# Input values
wn = float(input("Enter natural frequency wn (rad/s): "))
zeta = float(input("Enter damping ratio ζ: "))
t_final = float(input("Enter simulation time (seconds): "))

# Time array
t = np.linspace(0, t_final, 1000)

# Determine system type
if zeta < 1:
    system_type = "Underdamped"
    
    wd = wn * np.sqrt(1 - zeta**2)
    
    response = 1 - (
        np.exp(-zeta * wn * t) *
        (
            np.cos(wd * t) +
            (zeta / np.sqrt(1 - zeta**2)) * np.sin(wd * t)
        )
    )

elif zeta == 1:
    system_type = "Critically Damped"
    
    response = 1 - (1 + wn * t) * np.exp(-wn * t)

else:
    system_type = "Overdamped"
    
    s1 = -wn * (zeta - np.sqrt(zeta**2 - 1))
    s2 = -wn * (zeta + np.sqrt(zeta**2 - 1))
    
    response = 1 - (
        (s2 * np.exp(s1 * t) - s1 * np.exp(s2 * t))
        / (s2 - s1)
    )

# Display results
print("\n------------- RESULTS ----------------")
print(f"Natural Frequency       : {wn:.2f} rad/s")
print(f"Damping Ratio            : {zeta:.2f}")
print(f"System Type              : {system_type}")
print("--------------------------------------")

# Plot time response
plt.figure(figsize=(8, 5))
plt.plot(t, response)
plt.axhline(1, linestyle="--", label="Final Value")

plt.title("Time Response of Second-Order System")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()
