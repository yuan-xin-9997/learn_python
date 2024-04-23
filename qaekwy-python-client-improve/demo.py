from qaekwy.engine import DirectEngine
from qaekwy.model.constraint.relational import RelationalExpression
from qaekwy.model.specific import SpecificMaximum
from qaekwy.model.variable.integer import IntegerVariable
from qaekwy.model.modeller import Modeller
from qaekwy.model.searcher import SearcherType


# Define the optimization problem using Qaekwy Python Client
class SimpleOptimizationProblem(Modeller):
    def __init__(self):
        super().__init__()

        # Create a integer variables
        x = IntegerVariable(var_name="x", domain_low=0, domain_high=10)
        y = IntegerVariable(var_name="y", domain_low=0, domain_high=10)
        z = IntegerVariable(var_name="z", domain_low=0, domain_high=10)

        # Constraints
        constraint_1 = RelationalExpression(y > 2 * x)
        constraint_2 = RelationalExpression(x >= 4)
        constraint_3 = RelationalExpression(z == y - x)

        # Objective: Maximize z
        self.add_objective(
            SpecificMaximum(variable=z)
        )

        # Add variable and constraint to the problem
        self.add_variable(x)
        self.add_variable(y)
        self.add_variable(z)
        self.add_constraint(constraint_1)
        self.add_constraint(constraint_2)
        self.add_constraint(constraint_3)

        # Set the search strategy
        self.set_searcher(SearcherType.BAB)

# Create a Qaekwy engine for interaction with the freely-available Cloud instance
qaekwy_engine = DirectEngine()

# Create the optimization problem instance
optimization_problem = SimpleOptimizationProblem()

# Request the Qaekwy engine to solve the problem
response = qaekwy_engine.model(model=optimization_problem)

# Retrieve the list of solutions from the response
list_of_solutions = response.get_solutions()

# Print the solution(s) obtained
for solution in list_of_solutions:
    print(f"Optimal solution: x = {solution.x}")
    print(f"Optimal solution: y = {solution.y}")
    print(f"Optimal solution: z = {solution.z}")

print()