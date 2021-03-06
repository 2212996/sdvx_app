from flask import Flask, render_template
# from api import text_count_bp
from flask import Blueprint, jsonify, request, session
from flask_restful import Api, Resource
import json
import test
import api

# postされたテキストをカウントするapi(POSTメソッド)
text_count_bp = Blueprint('text_count', __name__, url_prefix='/post')
class TextCount(Resource):
    def post(self):

        # postされたデータを読み込み
        input_data = request.json

        result_data = api.output(input_data['your_id'], input_data['opp_id'], input_data['minlevel'], input_data['maxlevel'], input_data['difficulty'], input_data['clearmark'], input_data['grade'], input_data['scoregap'])

        # print(result_data)

        return jsonify(result_data)

text_count = Api(text_count_bp)
text_count.add_resource(TextCount, '')

app = Flask(__name__,
                static_folder="../frontend/dist/static",
                template_folder="../frontend/dist")

app.register_blueprint(text_count_bp)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)