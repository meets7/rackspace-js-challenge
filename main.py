from flask import Flask, render_template, jsonify, json, send_from_directory
import os


app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/dirPagination-template')
def static_route():
    return send_from_directory('templates', 'dirPagination.tpl.html')


@app.route("/getTableData", methods=["GET"])
def register():
    site_root = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(site_root, "static/data", "data.json")
    data = json.load(open(json_url))
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
