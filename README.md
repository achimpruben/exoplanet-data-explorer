# Exoplanet Data Explorer
**[Work in progress]**

## 🚀 Description
A simple **Python Flask web app** designed to fetch and display real astronomical data for confirmed exoplanets.

### Key Features
* Fetches live exoplanet data using Python's `requests` library by querying the **NASA Exoplanet Archive**.
* Generates charts comparing exoplanet properties against Earth and host stars against the Sun.

## ⚙️ Setup

1.  **Create the Virtual Environment**
    ```bash
    python -m venv venv
    ```
2.  **Activate the Virtual Environment**
    ```bash
    venv\Scripts\activate
    ```
3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run Application**
    ```bash
    python app.py
    ```
    Navigate to the address shown in the terminal (e.g. `http://127.0.0.1:5000/`).
