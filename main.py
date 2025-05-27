import itertools
from sympy import simplify_logic, symbols, sympify, to_dnf, to_cnf
from typing import List, Optional


class BooleanSimplifier:
    def __init__(self):
        """Initialize the Boolean Simplifier."""
        pass

    def simplify(self, expression: str, form: Optional[str] = None) -> str:
        """
        Simplify a Boolean expression.

        Args:
            expression: The Boolean expression as a string.
            form: Optional parameter to specify output form ('dnf' or 'cnf').
                 If None, returns the simplest form.

        Returns:
            A simplified Boolean expression as a string.
        """
        try:
            # Convert string expression to sympy expression
            expr = sympify(expression)

            # Simplify the expression
            simplified = simplify_logic(expr)

            # Convert to specified form if requested
            if form == 'dnf':
                simplified = to_dnf(simplified)
            elif form == 'cnf':
                simplified = to_cnf(simplified)

            return str(simplified)
        except Exception as e:
            raise ValueError(f"Invalid Boolean expression: {str(e)}")

    def extract_variables(self, expression: str) -> List[str]:
        """
        Extract all variables from a Boolean expression.

        Args:
            expression: The Boolean expression as a string.

        Returns:
            A list of variable names found in the expression.
        """
        try:
            expr = sympify(expression)
            return sorted([str(symbol) for symbol in expr.free_symbols])
        except Exception as e:
            raise ValueError(f"Invalid Boolean expression: {str(e)}")


def are_equivalent(expr1: str, expr2: str, variables: list) -> bool:
    """
    Determines if two Boolean expressions are equivalent.

    Args:
        expr1: First Boolean expression as a string.
        expr2: Second Boolean expression as a string.
        variables: List of variable names used in the expressions.

    Returns:
        True if the expressions are equivalent, False otherwise.
    """

    vars_symbols = symbols(variables)

    expr1_sympy = sympify(expr1)
    expr2_sympy = sympify(expr2)

    combinations = list(itertools.product(
        [False, True], repeat=len(variables)))

    # Evaluate expressions for each combination
    for combo in combinations:
        values = dict(zip(vars_symbols, combo))
        if expr1_sympy.subs(values) != expr2_sympy.subs(values):
            return False  # Found a mismatch; not equivalent

    return True  # All combinations match


def main():
    """Main function to demonstrate the Boolean Simplifier usage."""
    simplifier = BooleanSimplifier()

    # Test cases
    test_cases = [
        "A & B & ~(~A | B & C)",
        "A & ~A",
        "A | ~A",
        "A & (B | C) & (B | ~C)",
        "~(~(A & B))",
        "(A | B) & (A | C)",
        "A & B & ~(~A | B & C)",
        "(A & B) | (A & ~B) | (~A & B)",
    ]

    print("Boolean Expression Simplification Examples:")
    print("-" * 50)

    for expr in test_cases:
        try:
            print(f"\nOriginal:  {expr}")
            simplified = simplifier.simplify(expr)
            print(f"Simplified: {simplified}")

            vars_used = simplifier.extract_variables(expr)
            print(f"Variables:  {vars_used}")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
