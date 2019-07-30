from flask import Flask, send_from_directory, request
import lyrics

app = Flask(__name__, static_url_path="")
url = ""

@app.route('/')
def serv():
    return send_from_directory("", './web/index.html')

@app.route('/bar_graph.js')
def server_static():
    return send_from_directory("", './web/bar_graph.js')

@app.route('/pie_chart.js')
def ser():
    return send_from_directory("", "./web/pie_chart.js")

@app.route('/lyrics')
def runBarGraph():
    return lyrics.get_lyric_data('us') # Change the country code argument to whatever the desired country is.
    


if __name__ == "__main__":
    app.run(port="8080", host="0.0.0.0", debug=True)
