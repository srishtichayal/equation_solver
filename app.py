from flask import Flask, render_template, request, jsonify
from core_runner import solve_equations

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    solver = data.get('solver')
    equations_raw = data.get('equations')
    constants_raw = data.get('constants', '')

    try:
        eq_blocks = [block.strip().split('\n') for block in equations_raw.strip().split('---')]
        results = solve_equations(solver, eq_blocks, constants_raw)

        output_str = ""
        for i, block in enumerate(results):
            output_str += f"--- Solving System of Equations {i+1} ---\n"
            for k, v in block.items():
                output_str += f"{k} = {v}\n"
            output_str += "\n"

        return jsonify({"success": True, "solution": output_str})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
