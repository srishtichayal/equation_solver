from gekko import GEKKO
from sympy import *
import re
import ast

class Solution():
    def __init__(self):
        self.equations = []
        self.variables = []
        self.coefficients = {} 
        self.num_equations = 0

    def process_equations(self, equations):
        # for i in range(len(equations)):
        #     equations[i] = re.sub(r'e\*\*', 'e', equations[i])
        equations = [x.replace('=', '==') for x in equations]
        equations = [x.replace('sin', '_m.sin') for x in equations]
        equations = [x.replace('cos', '_m.cos') for x in equations]
        equations = [x.replace('tan', '_m.tan') for x in equations]
        equations = [x.replace('sqrt', '_m.sqrt') for x in equations]
        equations = [x.replace('log', '_m.log') for x in equations]
        equations = [x.replace('ln', '_m.log') for x in equations]
        equations = [x.replace('exp', '2.718281828459') for x in equations]
        equations = [x.replace('pi', '_m.pi') for x in equations]
        equations = [x.replace('e', '2.718281828459') for x in equations]
        equations = [x.replace('E', '2.718281828459') for x in equations]
        return equations
    
    def safe_eval(self, expr): #can evaluate simple arithmetic expressions
        #Parse the expression
        node = ast.parse(expr, mode='eval')
        
        #Walk through all subnodes in the expression tree
        for subnode in ast.walk(node):
            if not isinstance(subnode, (
                ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Constant,
                ast.operator, ast.unaryop
            )):
                raise ValueError(f"Disallowed expression: '{expr}'")
        return eval(expr, {"__builtins__": {}})
    

    def parse_constants_file(self): 
        filepath = '_Coefficients.txt'
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    try:
                        self.coefficients[key] = self.safe_eval(value)
                    except Exception as e:
                        raise ValueError(f"Invalid expression for '{key}': '{value}' → {e}")


    def get_variables(self, equations):
        self.parse_constants_file()
        var_pattern = re.compile(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b')
        to_remove = set(['sin', 'cos', 'tan', 'sqrt', 'log', 'ln', 'exp', 'pi', 'e']) | set(self.coefficients.keys())
        
        variables = set()
        for eq in equations:
            for var in var_pattern.findall(eq):
                if var not in to_remove:
                    variables.add(var)
        self.variables = list(variables)
        

    def solution(self, equations, num_variables):
        equations = self.process_equations(equations)
        self.get_variables(equations)
        m = GEKKO(remote=False)

        g_vars = {var: m.Var(value=1, name=var) for var in self.variables}

        #Inject coefficient values directly into locals
        local_context = {**g_vars, **self.coefficients, "m": m}

        #Add equations
        for eq_str in equations:
            m.Equation(eval(eq_str, {}, local_context))

        #Solve system
        m.solve(disp=True)

        #Return solution
        return {var: g_vars[var].value[0] for var in self.variables}

    
    