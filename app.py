import Categorisation
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    images = ["govtPublicAdmin.jpg","Healthcare.jpg","Logistics.jpg","Consulting.jpg","Hospitality.jpg","Law Enforcement.jpg",
              "Construction.jpg","Automotive.jpg","Manufacturing.jpg","RealEstate.jpg", "Engineering.jpg","IT.jpg","Telecommunications.jpg",
              "Financial.jpg","Education.jpg","food.jpg","retail.jpg","media.jpg"]
    return render_template('index.html', sectors=Categorisation.sectorData, images=images)


@app.route('/sector/<int:sector_id>')
def sector(sector_id):
    sector = Categorisation.sectorData[sector_id]
    jobs = sector['jobs']
    return render_template('sector.html', sector=sector, jobs=jobs)


if __name__ == '__main__':
    app.run()

