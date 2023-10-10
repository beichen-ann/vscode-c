import matplotlib.pyplot as plt

# Define circuit components
PTC = 'PTC Thermistor'
Triode = 'Control Triode'
Load = 'Load'

# Create circuit diagram
fig, ax = plt.subplots(figsize=(6, 4))

# Draw components
ax.plot([0, 1], [0, 0], 'k-', linewidth=2)  # Load line
ax.plot([1], [0], 'ko', markersize=10)  # Load dot
ax.text(1, 0.05, Load, ha='center')

ax.plot([1, 1], [0, 1], 'k--', linewidth=2)  # Connection line
ax.text(1.05, 0.5, PTC, ha='left')

ax.plot([1, 2], [1, 1], 'k-', linewidth=2)  # PTC line
ax.plot([2], [1], 'ko', markersize=10)  # PTC dot

ax.plot([2, 2], [1, 2], 'k--', linewidth=2)  # Connection line
ax.text(2.05, 1.5, Triode, ha='left')

ax.plot([2, 3], [2, 2], 'k-', linewidth=2)  # Triode line
ax.plot([3], [2], 'ko', markersize=10)  # Triode dot

# Customize plot appearance
ax.axis('off')
plt.tight_layout()

# Save or show the circuit diagram
plt.savefig('circuit_diagram.png')
plt.show()
