import Categorisation
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', sectors=Categorisation.sectorData)


@app.route('/sector/<int:sector_id>')
def sector(sector_id):
    sector = Categorisation.sectorData[sector_id]
    jobs = sector['jobs']
    return render_template('sector.html', sector=Categorisation.sectorData, jobs=jobs)


if __name__ == '__main__':
    app.run()

