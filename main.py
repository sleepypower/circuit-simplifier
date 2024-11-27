import itertools
from sympy import symbols, sympify


def are_equivalent(expr1: str, expr2: str, variables: list) -> bool:
    """
    Determines if two Boolean expressions are equivalent.

    :param expr1: First Boolean expression as a string.
    :param expr2: Second Boolean expression as a string.
    :param variables: List of variable names used in the expressions.
    :return: True if the expressions are equivalent, False otherwise.
    """
    # Define symbols for variables
    vars_symbols = symbols(variables)

    # Parse expressions using sympy
    expr1_sympy = sympify(expr1)
    expr2_sympy = sympify(expr2)

    # Generate all possible combinations of truth values
    combinations = list(itertools.product(
        [False, True], repeat=len(variables)))

    # Evaluate expressions for each combination
    for combo in combinations:
        values = dict(zip(vars_symbols, combo))
        if expr1_sympy.subs(values) != expr2_sympy.subs(values):
            return False  # Found a mismatch; not equivalent

    return True  # All combinations match


# Example usage:
if __name__ == "__main__":
    expr1 = "A & B & ~(~A | B & C)"
    expr2 = "A & B & ~C"
    variables = ["A", "B", "C"]

    equivalent = are_equivalent(expr1, expr2, variables)
    if equivalent:
        print("The expressions are equivalent.")
    else:
        print("The expressions are not equivalent.")
