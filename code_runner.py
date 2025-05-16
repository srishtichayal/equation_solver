import gekko_solver
import time
equations = []
equations_file = '_Equations1.txt'
with open(equations_file, 'r') as f:
    for line in f:
        equations.append(line.strip())

s = gekko_solver.Solution()

# write answers to file 
answers_file = '_Answers.txt'
start_time = time.time()
answers = s.solution(equations, len(equations))
end_time = time.time()

with open(answers_file, 'w') as f:
    total_time = end_time - start_time
    f.write(f'Total time: {total_time} seconds\n')
    for key, value in answers.items():
        var_name = key
        var_value = value
        # write to the file
        f.write(f'{var_name} = {var_value}\n')