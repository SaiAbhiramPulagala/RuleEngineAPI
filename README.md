# Rule Engine API

## Overview
This Rule Engine API allows users to create, combine, and evaluate rules. It is designed as a RESTful API using Flask, offering endpoints for managing rule creation, combination, and evaluation based on provided AST (Abstract Syntax Tree) structures and data.

## Features
- **Create Rule**: Convert plain-text rules into AST format.
- **Combine Rules**: Merge multiple rules into a single combined rule.
- **Evaluate Rule**: Evaluate the truth value of a rule against provided data.

## Dependencies
- Python 3.8+
- Flask
- SQLite

## Installation

### Prerequisites
Ensure you have Python and pip installed on your system. You can download Python from [here](https://www.python.org/downloads/).

### Setting Up
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/rule-engine-api.git
   cd rule-engine-api
2. Install the required Python packages:
  pip install flask sqlite3
3. Initialize the database:
  from db import init_db
  init_db()

Usage
**Create Rule**

Endpoint: POST /create_rule Payload:
```bash
   {
     "rule": "age > 30 AND salary > 50000"
   }
```
**Response:**
``` bash
{
  "type": "operator",
  "value": "AND",
  "left": {
    "type": "operand",
    "value": "age > 30"
  },
  "right": {
    "type": "operand",
    "value": "salary > 50000"
  }
}
```
****************************************************
**Combine Rules**
Endpoint: POST /combine_rules Payload:
```bash
{
  "rules": [
    "age > 30 AND salary > 50000",
    "age < 25 AND department = 'Marketing'"
  ]
}
```
Response:
```bash
{
  "type": "operator",
  "value": "OR",
  "left": { ... },
  "right": { ... }
}
```
****************************************************
**Evaluate Rule**

Endpoint: POST /evaluate_rule Payload:
```bash
{
  "ast": {
    "type": "operator",
    "value": "AND",
    "left": {
      "type": "operand",
      "value": "age > 30"
    },
    "right": {
      "type": "operand",
      "value": "salary > 50000"
    }
  },
  "data": {
    "age": 35,
    "salary": 60000
  }
}
```
**Response:**
```bash
{
  "result": true
}
```
