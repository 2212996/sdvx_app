from flask import Blueprint, jsonify, request, session
from flask_restful import Api, Resource
import json
import test

# postされたテキストをカウントするapi(POSTメソッド)
text_count_bp = Blueprint('text_count', __name__, url_prefix='/api/post')
class TextCount(Resource):
    def post(self):

        # postされたデータを読み込み
        input_data = request.json

        result_data = test.run_selection(input_data['user1'], input_data['user2'], input_data['difficulty'], input_data['gap'])

        print(result_data)

        return jsonify(result_data)

text_count = Api(text_count_bp)
text_count.add_resource(TextCount, '')