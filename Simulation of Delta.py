import numpy as np
import matplotlib.pyplot as plt

# Function to calculate critical delta (discount factor)
def delta_crit(U_C, U_bar, U_P, p):
    numerator = U_C - U_bar
    denominator = p * (U_P - U_C) + (U_C - U_bar)
    return numerator / denominator

# Fixed parameters
U_C = 100       # Present value of the cooperative trajectory
U_bar = 120     # Short-term gain from deviation
U_P_base = 60   # Base punishment value for T=1

# Ranges for p and T
p_values = np.linspace(0.1, 1.0, 100)
T_values = np.arange(1, 21)

# ------------------ Visualization 1: Critical delta curves vs. p for different T ------------------
plt.figure(figsize=(10, 6))
for T in [3, 5, 10, 15, 20]:
    # More severe penalty with higher T: U_P decreases with T
    U_P = U_C - (U_C - U_P_base) * (T / max(T_values))
    delta_values = [delta_crit(U_C, U_bar, U_P, p) for p in p_values]
    plt.plot(p_values, delta_values, label=f'T = {T} years')

# Reference line delta = 1
plt.axhline(y=1, color='red', linestyle='--', linewidth=1, label=r'$\delta = 1$')

# Graph aesthetics
plt.xlabel('Detection probability (p)')
plt.ylabel(r'$\delta_{\mathrm{crit}}$')
plt.title(r'$\delta_{\mathrm{crit}}$ as a function of $p$ for different values of $T$')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("delta_crit_curves_en.png", dpi=300)
plt.show()

# ------------------ Visualization 2: Heatmap of critical delta as a function of p and T ------------------
# Matrix to store critical delta values
delta_matrix = np.zeros((len(T_values), len(p_values)))

# Fill the matrix with simulated values
for i, T in enumerate(T_values):
    U_P = U_C - (U_C - U_P_base) * (T / max(T_values))
    for j, p in enumerate(p_values):
        delta_matrix[i, j] = delta_crit(U_C, U_bar, U_P, p)

# Create the heatmap with contours
plt.figure(figsize=(10, 6))
cp = plt.contourf(p_values, T_values, delta_matrix, levels=50, cmap='viridis')
plt.colorbar(cp, label=r'$\delta_{\mathrm{crit}}$')
plt.contour(p_values, T_values, delta_matrix, levels=[1], colors='red', linestyles='--', linewidths=1)

# Graph aesthetics
plt.xlabel('Detection probability (p)')
plt.ylabel('Punishment duration (T)')
plt.title(r'Heatmap of $\delta_{\mathrm{crit}}$ as a function of $p$ and $T$')
plt.tight_layout()
plt.savefig("delta_crit_heatmap_en.png", dpi=300)
plt.show()
