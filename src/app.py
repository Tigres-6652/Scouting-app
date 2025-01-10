from flask import Flask, render_template, request, jsonify, Response


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pit_scouting')
def pit_scouting():
    return render_template('pit_scouting.html')

@app.route('/match_scouting')
def match_scouting():
    return render_template('match_scouting.html')

@app.route('/info_teams')
def info_teams():
    return render_template('info_teams.html')

@app.route('/strategy_scouting')
def strategy_scouting():
    return render_template('strategy_scouting.html')


if __name__ == '__main__':
    app.run(debug=True)
