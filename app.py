from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data for job sectors and jobs
job_sectors = [
    {
        'name': 'Information Technology',
        'jobs': ['Job 1', 'Job 2', 'Job 3']

    },
    {
        'name': 'Healthcare',
        'jobs': ['Job 4', 'Job 5', 'Job 6']
    },
{
        'name': 'Financial',
        'jobs': ['Job 5', 'Job 6', 'Job 7']
    },
{
        'name': 'Education',
        'jobs': ['Job 7', 'Job 8', 'Job 9']
    },
{
        'name': 'Financial',
        'jobs': ['Job 5', 'Job 6', 'Job 7']
    },
{
        'name': 'Education',
        'jobs': ['Job 7', 'Job 8', 'Job 9']
    },

{
        'name': 'Financial',
        'jobs': ['Job 5', 'Job 6', 'Job 7']
    },
{
        'name': 'Education',
        'jobs': ['Job 7', 'Job 8', 'Job 9']
    },

{
        'name': 'Financial',
        'jobs': ['Job 5', 'Job 6', 'Job 7']
    },
{
        'name': 'Education',
        'jobs': ['Job 7', 'Job 8', 'Job 9']
    },

{
        'name': 'Financial',
        'jobs': ['Job 5', 'Job 6', 'Job 7']
    },
{
        'name': 'Education',
        'jobs': ['Job 7', 'Job 8', 'Job 9']
    },

{
        'name': 'Financial',
        'jobs': ['Job 5', 'Job 6', 'Job 7']
    },
{
        'name': 'Education',
        'jobs': ['Job 7', 'Job 8', 'Job 9']
    }

    # Add more sectors and their corresponding jobs here
]


@app.route('/')
def index():
    return render_template('index.html', sectors=job_sectors)


@app.route('/sector/<int:sector_id>')
def sector(sector_id):
    sector = job_sectors[sector_id]
    jobs = sector['jobs']
    return render_template('sector.html', sector=sector, jobs=jobs)


if __name__ == '__main__':
    app.run()

