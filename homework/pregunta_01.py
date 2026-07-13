# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

import os

import matplotlib.pyplot as plt
import pandas as pd

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """


    os.makedirs("docs", exist_ok=True)

    data = pd.read_csv("files/input/shipping-data.csv")

    # Envíos por bodega
    data["Warehouse_block"].value_counts().sort_index().plot(
        kind="bar",
        color="steelblue",
    )
    plt.title("Shipping per warehouse")
    plt.xlabel("Warehouse block")
    plt.ylabel("Number of shipments")
    plt.tight_layout()
    plt.savefig("docs/shipping_per_warehouse.png")
    plt.close()

    # Medio de envío
    data["Mode_of_Shipment"].value_counts().plot(
        kind="bar",
        color="seagreen",
    )
    plt.title("Mode of shipment")
    plt.xlabel("Shipment mode")
    plt.ylabel("Number of shipments")
    plt.tight_layout()
    plt.savefig("docs/mode_of_shipment.png")
    plt.close()

    # Promedio de calificación por bodega
    data.groupby("Warehouse_block")["Customer_rating"].mean().sort_index().plot(
        kind="bar",
        color="darkorange",
    )
    plt.title("Average customer rating")
    plt.xlabel("Warehouse block")
    plt.ylabel("Average rating")
    plt.ylim(0, 5)
    plt.tight_layout()
    plt.savefig("docs/average_customer_rating.png")
    plt.close()

    # Distribución de peso
    data["Weight_in_gms"].plot(
        kind="hist",
        bins=30,
        color="mediumpurple",
        edgecolor="black",
    )
    plt.title("Weight distribution")
    plt.xlabel("Weight (g)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("docs/weight_distribution.png")
    plt.close()

    # Dashboard HTML
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Shipping Dashboard</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                margin: 0;
                padding: 30px;
                text-align: center;
            }

            h1 {
                color: #333;
            }

            .dashboard {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 20px;
                max-width: 1200px;
                margin: auto;
            }

            .card {
                background: white;
                padding: 15px;
                border-radius: 10px;
                box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
            }

            img {
                width: 100%;
                height: auto;
            }
        </style>
    </head>
    <body>
        <h1>Shipping Dashboard</h1>

        <div class="dashboard">
            <div class="card">
                <img src="shipping_per_warehouse.png" alt="Shipping per warehouse">
            </div>
            <div class="card">
                <img src="mode_of_shipment.png" alt="Mode of shipment">
            </div>
            <div class="card">
                <img src="average_customer_rating.png" alt="Average customer rating">
            </div>
            <div class="card">
                <img src="weight_distribution.png" alt="Weight distribution">
            </div>
        </div>
    </body>
    </html>
    """

    with open("docs/index.html", "w", encoding="utf-8") as file:
        file.write(html)