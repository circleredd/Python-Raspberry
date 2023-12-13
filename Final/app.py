from flask import Flask, request
from flask import render_template
import link, sql
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        date = request.values.get('search')
        if date == '':
            pass
        else:
            date = date.split(sep='-')
            time = sql.Time.get_time(date)
            formatted_time = [date[0].strftime("%Y-%m-%d %H:%M:%S") for date in time] 
            return render_template('index.html', time = formatted_time)
    
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
