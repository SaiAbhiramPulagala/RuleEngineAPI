from flask import Flask, request, jsonify
import models
import db

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Rule Engine API! Use the API endpoints to interact with the system."

@app.route('/create_rule', methods=['POST'])
def create_rule():
    try:
        rule_string = request.json['rule']
        ast = models.create_rule(rule_string)
        db.insert_rule(rule_string, models.ast_to_json(ast))
        return jsonify(models.ast_to_json(ast))
    except KeyError:
        return jsonify({'error': 'Invalid input format'}), 400

@app.route('/combine_rules', methods=['POST'])
def combine_rules():
    try:
        rules = request.json['rules']
        combined_ast = models.combine_rules(rules)
        return jsonify(models.ast_to_json(combined_ast))
    except KeyError:
        return jsonify({'error': 'Invalid input format'}), 400

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    try:
        ast_json = request.json['ast']
        data = request.json['data']
        ast = models.json_to_ast(ast_json)
        if ast is None:
            return jsonify({"error": "Invalid AST format"}), 400
        result = models.evaluate_rule(ast, data)
        return jsonify({"result": result})
    except KeyError:
        return jsonify({'error': 'Missing data in request'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
