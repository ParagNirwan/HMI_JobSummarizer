import Categorisation
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    images = ["IT.jpg", "Engineering.jpg","retail.jpg","RealEstate.jpg","Law Enforcement.jpg","Hospitality.jpg",
              "Healthcare.jpg",
              "Financial.jpg",
              "Telecommunications.jpg",
              "Automotive.jpg",
              "Logistics.jpg",
              "Education.jpg",
              "Manufacturing.jpg",
              "media.jpg",
              "govtPublicAdmin.jpg",
              "Food.jpg",
              "Construction.jpg",
              "Consulting.jpg"
              ]
    return render_template('index.html', sectors=Categorisation.sectorData, images=images)


@app.route('/sector/<int:sector_id>')
def sector(sector_id):
    sector = Categorisation.sectorData[sector_id]
    jobs = sector['jobs']
    return render_template('sector.html', sector=sector, jobs=jobs)


if __name__ == '__main__':
    app.run()

