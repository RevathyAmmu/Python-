import pylab as plt
import numpy as np

# Constants
c = 3.0e8  # Speed of light in vacuum (m/s)
n = 1.33   # Refractive index of water (Super-Kamiokande)
particles = {
    'Electron': 0.511,  # MeV/c^2
    'Muon': 105.7,      # MeV/c^2
    'Tau': 1777,        # MeV/c^2
    'Proton': 938.3,    # MeV/c^2
}

# Function to calculate beta from momentum and mass
def beta_from_momentum(p, mass):
    energy = np.sqrt(p**2 + mass**2)
    return p / energy  # beta = p / E

# Function to calculate Cherenkov angle from beta
def cherenkov_angle_from_beta(beta):
    return np.arccos(1 / (n * beta)) * 180 / np.pi  # In degrees

# Momentum range (in MeV/c)
momentum_range = np.linspace(0.1, 10000, 500)  # MeV/c

# Plot Cherenkov angle for each particle
plt.figure(figsize=(10, 6))
for particle, mass in particles.items():
    momenta = momentum_range
    betas = beta_from_momentum(momenta, mass)
    angles = cherenkov_angle_from_beta(betas)
    
    
    angles = np.ma.masked_where(betas < 1/n, angles)
    
    plt.plot(momenta, angles, label=f'{particle} (m={mass} MeV/c²)')

# Plot settings
plt.title('Cherenkov Angle vs Momentum for Various Particles in Super-Kamiokande')
plt.xlabel('Momentum (MeV/c)')
plt.ylabel('Cherenkov Angle (degrees)')
plt.legend(loc='best')

plt.xscale('log')  # Logarithmic scale for better visualization
plt.ylim(0, 60)    # Cherenkov angle limit in degrees
plt.show()

