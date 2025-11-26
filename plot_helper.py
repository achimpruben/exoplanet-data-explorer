import matplotlib.pyplot as plt

def plot_planet_comparison(planet, name):
    labels = ['Radius (Earth)', 'Mass (Earth)', 'Orbital Period (days)', 'Equilibrium Temp (K)']
    earth = [1, 1, 365.25, 255]
    exo = [
        planet.get('pl_rade', 0),
        planet.get('pl_bmasse', 0),
        planet.get('pl_orbper', 0),
        planet.get('pl_eqt', 0)
    ]
    
    x = range(len(labels))
    
    plt.figure(figsize=(10, 6))
    plt.bar(x, earth, width=0.4, label='Earth', align='center')
    plt.bar([i + 0.4 for i in x], exo, width=0.4, label=name, align='center')
    
    plt.xticks([i + 0.2 for i in x], labels, rotation=15)
    plt.ylabel('Value')
    plt.title(f'Comparison: Earth vs {name}')
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'static/plots/{name}_planet_comparison.png')
    plt.close()

def plot_star_comparison(planet, name):
    labels = ['Radius (Sun)', 'Mass (Sun)', 'Temperature (K)', 'Luminosity (Sun)']
    sun = [1, 1, 5778, 1]
    star = [
        planet.get('st_rad', 0),
        planet.get('st_mass', 0),
        planet.get('st_teff', 0),
        planet.get('st_lum', 0)
    ]
    
    x = range(len(labels))
    
    plt.figure(figsize=(10, 6))
    plt.bar(x, sun, width=0.4, label='Sun', align='center')
    plt.bar([i + 0.4 for i in x], star, width=0.4, label=planet.get('pl_hostname', 'Host Star'), align='center')
    
    plt.xticks([i + 0.2 for i in x], labels, rotation=15)
    plt.ylabel('Value')
    plt.title(f'Comparison: Sun vs {planet.get("pl_hostname", "Host Star")}')
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'static/plots/{name}_star_comparison.png')
    plt.close()

