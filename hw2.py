import constraint

DOMAIN = range(0,10)
ONES_CONSTRAINT = lambda x, y ,z : (x + y) % 10 == z
GENERAL_CONSTRAINT = lambda x0, x1, y0, y1, z : (x0 + y0) // 2 + (x1 + y1) % 10 == z

def create_add_problem(addend, summ):
    if type(addend) is not list or type(addend[0]) is not str:
        raise TypeError('addend must be a list of strings')
    problem = constraint.Problem()
    variables = _get_variable_list(addend, summ)
    problem = _add_vars_to_problem(problem, variables)

    problem.addConstraint(constraint.AllDifferentConstraint())
    problem = _generate_constraints(problem, addend, summ)
    
    return problem

def main():
    prob = create_add_problem(['DAYS', 'TOO'], 'SHORT')
    prob_sol = prob.getSolutions()
    print(prob_sol)


def _generate_constraints(problem, addend, summ):
    add_1 = addend[0].zfill(len(summ))
    print(add_1)
    add_2 = addend[1].zfill(len(summ))
    print(add_2)
    print(summ)
    # -col is the index from the right
    for col in range(1,len(summ)+1):
        if -col == -1: # we are in the ones place
            x = add_1[-col]
            y = add_2[-col]
            z = summ[-col]
            problem.addConstraint(ONES_CONSTRAINT, (x, y , z))
        else:
            x1 = add_1[-col]
            y1 = add_2[-col]
            z = summ[-col]
            x0 = add_1[-col+1]
            y0 = add_2[-col+1]
            problem.addConstraint(GENERAL_CONSTRAINT, (x0, x1, y0, y1 , z))
    return problem
        

def _get_variable_list(addend, summ):
    variables = set()
    variables.update([c for c in summ])
    for v in addend:
        variables.update([c for c in v])

    return list(variables)

def _add_vars_to_problem(problem, variables):
    problem.addVariable('0', [0])
    for v in variables:
        problem.addVariable(v, DOMAIN)
    return problem

if __name__ == '__main__':
    main()

