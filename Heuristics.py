from CSP import *


def MRV(assignment, csp):
    unassigned = []

    for var in csp.variables:

        if var not in assignment:
            unassigned.append(var)

    feature = lambda var: len(csp.domains[var])

    return min(unassigned, key=feature)


def select_unassigned_variables(assignment, csp):
    unassigned = []

    for var in csp.variables:

        if var not in assignment:
            unassigned.append(var)

    return unassigned.pop(0)


def LCS(csp, var):

    if len(csp.domains[var]) == 1:
        return csp.domains[var]

    feature = lambda value: number_of_conflicts(csp, var, value)
    return sorted(csp.domains[var], key=feature)

def order_domain_values(csp, var):
    return csp.domains[var]

