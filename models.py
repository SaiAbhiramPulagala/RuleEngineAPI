class Node:
    def __init__(self, type, value, left=None, right=None):
        self.type = type
        self.value = value
        self.left = left
        self.right = right

def parse_to_ast(rule_string):
    # This is a placeholder. You need to implement the actual parsing logic based on your rule syntax.
    parts = rule_string.split(' AND ')
    if len(parts) == 1:
        return Node('operand', parts[0])
    left = Node('operand', parts[0])
    right = Node('operand', parts[1])
    return Node('operator', 'AND', left, right)

def create_rule(rule_string):
    return parse_to_ast(rule_string)

def combine_rules(rules):
    asts = [create_rule(rule) for rule in rules]
    if len(asts) < 2:
        return asts[0] if asts else None
    combined = asts[0]
    for ast in asts[1:]:
        combined = Node("operator", "OR", combined, ast)
    return combined

def evaluate_rule(ast, data):
    if ast is None:
        return False
    if ast.type == "operand":
        key, op, value = ast.value.split()
        if op == '>':
            return float(data.get(key, 0)) > float(value)
        elif op == '<':
            return float(data.get(key, 0)) < float(value)
        elif op == '=':
            return str(data.get(key, "")) == value
    elif ast.type == "operator":
        left_result = evaluate_rule(ast.left, data) if ast.left else False
        right_result = evaluate_rule(ast.right, data) if ast.right else False
        return (left_result and right_result) if ast.value == "AND" else (left_result or right_result)
    return False

def json_to_ast(json_data):
    if json_data is None or 'type' not in json_data or 'value' not in json_data:
        return None
    left = json_to_ast(json_data.get('left')) if 'left' in json_data else None
    right = json_to_ast(json_data.get('right')) if 'right' in json_data else None
    return Node(json_data['type'], json_data['value'], left, right)

def ast_to_json(ast):
    if not ast:
        return None
    result = {'type': ast.type, 'value': ast.value}
    if ast.left:
        result['left'] = ast_to_json(ast.left)
    if ast.right:
        result['right'] = ast_to_json(ast.right)
    return result
