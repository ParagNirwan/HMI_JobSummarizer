import Categorisation
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    images = ["govtPublicAdmin.jpg","Healthcare.jpg","Logistics.jpg","Consulting.jpg","Hospitality.jpg","Law Enforcement.jpg","Construction.jpg",
              "Automotive.jpg", "Manufacturing.jpg","Fashion.jpg","RealEstate.jpg", "Engineering.jpg",
              "IT.jpg","Telecommunications.jpg","Financial.jpg","Education.jpg","Food.jpg","retail.jpg","media.jpg","Agriculture.jpg","Sports.png"]

    images2 = {
        "Government Public Admin": "govtPublicAdmin.jpg",
        "Engineering": "Engineering.jpg",
        "Manufacturing": "Manufacturing.jpg",
        "Retail": "retail.jpg",
        "Real Estate": "RealEstate.jpg",
        "Law Enforcement": "Law Enforcement.jpg",
        "Information Technology": "IT.jpg",
        "Hospitality Tourism": "Hospitality.jpg",
        "Healthcare": "Healthcare.jpg",
        "Financial": "Financial.jpg",
        "Telecommunication": "Telecommunications.jpg",
        "Automotive": "Automotive.jpg",
        "Transportation Logistics": "Logistics.jpg",
        "Media": "media.jpg",
        "Education": "Education.jpg",
        "Fashion": "Fashion.jpg",
        "Food and Beverages": "Food.jpg",
        "Construction": "Construction.jpg",
        "Sports and Fitness": "Sports.png",
        "Consulting": "Consulting.jpg"
    }

    return render_template('index.html', sectors=Categorisation.sectorData, images=images2)


@app.route('/sector/<int:sector_id>')
def sector(sector_id):
    sector = Categorisation.sectorData[sector_id]
    jobs = sector['jobs']
    return render_template('sector.html', sector=sector, jobs=jobs)


if __name__ == '__main__':
    app.run()

