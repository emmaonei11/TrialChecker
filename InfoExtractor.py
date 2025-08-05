from flask import Flask, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup
from collections import defaultdict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    drug_name = data['drug']

    # Sample site to scrape (Note: You must verify legal use)
    search_url = f"https://www.cancerresearchuk.org/about-cancer/find-a-clinical-trial/search?search={drug_name}"

    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch trials"}), 500

    soup = BeautifulSoup(response.text, 'html.parser')

    # Placeholder structure: Adapt to real page structure
    trials = soup.select('.search-result__item')  # Update this selector as needed

    number_of_trials = len(trials)
    other_drugs = set()
    patients_per_drug = defaultdict(int)

    for trial in trials:
        # Placeholder: Replace with actual selectors
        description = trial.get_text()
        
        # Simulated parsing logic
        lines = description.split('\n')
        for line in lines:
            if 'Drugs used:' in line:
                drugs = line.replace('Drugs used:', '').split(',')
                drugs = [d.strip() for d in drugs]
                for d in drugs:
                    if d.lower() != drug_name.lower():
                        other_drugs.add(d)
                    patients_per_drug[d] += 1
            elif 'Patients:' in line:
                count = int(line.replace('Patients:', '').strip())
                patients_per_drug[drug_name] += count

    return jsonify({
        "number_of_trials": number_of_trials,
        "other_drugs": list(other_drugs),
        "patients_per_drug": patients_per_drug
    })

if __name__ == '__main__':
    app.run(debug=True)
