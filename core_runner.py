def solve_equations(solver_name, equations_list, constants_str=None):
    if solver_name == "gekko":
        import gekko_solver as selected_solver
    elif solver_name == "scipy":
        import scipy_solver as selected_solver
    else:
        raise ValueError("Unknown solver specified.")

    s = selected_solver.Solution()

    if constants_str:
        from tempfile import NamedTemporaryFile
        with NamedTemporaryFile(delete=False, mode='w', suffix=".txt") as f:
            f.write(constants_str)
            s.constantspath = f.name

    all_results = []
    for eq_block in equations_list:
        answers = s.solution(eq_block)
        s.constantspath = None
        s.coefficients.update(answers)
        all_results.append(answers)

    return all_results
