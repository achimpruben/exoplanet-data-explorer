from flask import Flask, render_template, abort
from exoplanet_api import get_exoplanets, get_exoplanet_details
from plot_helper import plot_planet_comparison, plot_star_comparison

app = Flask(__name__)

@app.route("/")
def index():
    planets = get_exoplanets()
    return render_template("index.html", planets=planets)

@app.route("/planet/<name>")
def planet_detail(name):
    planet = get_exoplanet_details(name)
    if not planet:
        abort(404)
    
    plot_planet_comparison(planet, name)
    plot_star_comparison(planet, name)
    
    return render_template("details.html", planet=planet, name=name)

if __name__ == "__main__":
    app.run(debug=True)
