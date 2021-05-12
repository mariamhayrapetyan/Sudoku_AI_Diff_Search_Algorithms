import itertools

rows = "123456789"
cols = "ABCDEFGHI"


class Sudoku:

    def __init__(self, grid):

        self.variables = list()
        self.variables = self.generate_variables()

        self.domains = dict()
        self.domains = self.generate_domains(grid)

        global_constraints = self.generate_global_constraints()

        self.binary_constraints = list()
        self.binary_constraints = self.generate_binary_constraints(global_constraints)

        self.neighbors = dict()
        self.neighbors = self.generate_neighbor_variables()

        self.eliminated = dict()
        self.eliminated = {v: list() if grid[i] == '0' else [int(grid[i])] for i, v in enumerate(self.variables)}


    def generate_variables(self):

        variables = []

        for col in cols:

            for row in rows:
                new_variable = col + row
                variables.append(new_variable)

        return variables


    def generate_domains(self, grid):

        grid_list = list(grid)

        domains = dict()

        for i, variable in enumerate(self.variables):
            if grid_list[i] == "0":
                domains[variable] = list(range(1, 10))
            else:
                domains[variable] = [int(grid_list[i])]

        return domains


    def generate_global_constraints(self):

        row_constraints = []
        column_constraints = []
        subgrid_constraints = []

        #rows constraints
        for row in rows:
            row_constraints.append([col + row for col in cols])

        #columns constraints
        for col in cols:
            column_constraints.append([col + row for row in rows])

        #subgrid constraints
        rows_subgrid = (cols[i:i + 3] for i in range(0, len(rows), 3))
        rows_subgrid = list(rows_subgrid)

        cols_subgrid = (rows[i:i + 3] for i in range(0, len(cols), 3))
        cols_subgrid = list(cols_subgrid)

        for row in rows_subgrid:
            for col in cols_subgrid:

                current_subgrid_constraints = []

                for i in row:
                    for j in col:
                        current_subgrid_constraints.append(i + j)

                subgrid_constraints.append(current_subgrid_constraints)

        return row_constraints + column_constraints + subgrid_constraints


    def generate_binary_constraints(self, global_constraints):
        generated_binary_constraints = list()

        for constraint_set in global_constraints:

            binary_constraints = list()

            for i in itertools.permutations(constraint_set, 2):
                binary_constraints.append(i)

            for constraint in binary_constraints:
                constraint_list = list(constraint)
                if (constraint_list not in generated_binary_constraints):
                    generated_binary_constraints.append([constraint[0], constraint[1]])

        return generated_binary_constraints


    def generate_neighbor_variables(self):
        neighbor_variables = dict()

        for var in self.variables:
            neighbor_variables[var] = list()

            for constraint in self.binary_constraints:
                if var == constraint[0]:
                    neighbor_variables[var].append(constraint[1])

        return neighbor_variables



    def isFinished(self):
        for variables, domains in self.domains.items():
            if len(domains) > 1:
                return False

        return True


    def __str__(self):
        output = ""
        count = 1
        round = 0

        for variable in self.variables:

            value = str(self.domains[variable])
            if type(self.domains[variable]) == list:
                if len(self.domains[variable]) > 1:
                    value = "0"
                else:
                    value = str(self.domains[variable][0])

            output += " " + value + " "

            if count % 3 == 0:
                output += "|"
                if count >= 9:
                    count = 0
                    round += 1
                    output = output[:-1]
                    output += "\n"
                    tazaban = round * 9
                    if tazaban % 27 == 0 and tazaban != 81:
                        output += "=============================\n"
            count += 1
        return output


def not_equal(xi, xj):
    result = xi != xj
    return result


def number_of_conflicts(csp, var, value):
    count = 0

    for neighbor in csp.neighbors[var]:

        if len(csp.domains[neighbor]) > 1 and value in csp.domains[neighbor]:
            count += 1

    return count


def is_consistent(csp, assignment, var, value):
    is_consistent = True

    for current_var, current_value in assignment.items():

        if current_value == value and current_var in csp.neighbors[var]:
            is_consistent = False

    return is_consistent


def assign(var, value, assignment):
    assignment[var] = value


def assign_with_forward_check(csp, var, value, assignment):
    assignment[var] = value

    if csp.domains:
        forward_check(csp, var, value, assignment)


def unassign(var, assignment):
    if var in assignment:
        del assignment[var]


def unassign_with_forward_check(csp, var, assignment):
    if var in assignment:

        for (variable, value) in csp.eliminated[var]:
            csp.domains[variable].append(value)

        csp.eliminated[var] = []

        del assignment[var]


def forward_check(csp, var, value, assignment):
    for neighbor in csp.neighbors[var]:

        if neighbor not in assignment:

            if value in csp.domains[neighbor]:
                csp.domains[neighbor].remove(value)

                csp.eliminated[var].append((neighbor, value))


# def print_grid1(grid):
#     output = ""
#     count = 1
#     round = 0
#
#     for cell in grid:
#
#         value = cell
#         output += " " + value + " "
#
#         if count % 3 == 0:
#             output += "|"
#             if count >= 9:
#                 count = 0
#                 round += 1
#                 output = output[:-1]
#                 output += "\n"
#                 tazaban = round * 9
#                 if tazaban % 27 == 0 and tazaban != 81:
#                     output += "=============================\n"
#         count += 1
#     return output
