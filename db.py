import sqlite3
import json  # Import json to serialize the dict

DATABASE = 'rules.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    return db

def init_db():
    with get_db() as db:
        db.execute('CREATE TABLE IF NOT EXISTS rules (id INTEGER PRIMARY KEY, rule_string TEXT, ast_blob TEXT)')
        db.commit()

def insert_rule(rule_string, ast_blob):
    with get_db() as db:
        # Convert ast_blob from a dict to a JSON string
        ast_blob_json = json.dumps(ast_blob)
        db.execute('INSERT INTO rules (rule_string, ast_blob) VALUES (?, ?)', (rule_string, ast_blob_json))
        db.commit()
