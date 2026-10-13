# VDL-identification
## Python Code Style Guidelines

All Python code in this repository must follow the [NVIDIA Isaac Sim Python coding guidelines](https://docs.isaacsim.omniverse.nvidia.com/latest/py/docs/overview/guidelines.html) and PEP 8 conventions. These rules help maintain consistent, readable, and maintainable code across all contributors.

### 1. Naming Conventions

- **Variables and functions:** Use `snake_case`.
  - Correct: `calculate_total`, `robot_position`
  - Incorrect: `calculateTotal`, `RobotPosition`

- **Classes:** Use `PascalCase`.
  - Correct: `RobotController`, `SimulationManager`
  - Incorrect: `robot_controller`, `simulation_manager`

- **Constants:** Use `UPPER_SNAKE_CASE`.
  - Correct: `MAX_SPEED`, `DEFAULT_TIMEOUT`
  - Incorrect: `max_speed`, `MaxSpeed`

- **Modules and Python files:** Use short, descriptive `snake_case` names.
  - Correct: `robot_controller.py`, `simulation_utils.py`
  - Incorrect: `RobotController.py`, `simulationUtils.py`

- **Function parameters:** Use descriptive `snake_case` names.
  - Correct: `def calculate_total(item_price, item_quantity):`
  - Incorrect: `def calculate_total(itemPrice, itemQuantity):`

Use meaningful names that describe the purpose of a variable, function, class, or module. Avoid ambiguous names and unnecessary abbreviations.

### 2. Formatting Rules

- Use **Black** for automatic Python code formatting.
- Use **isort** to organize imports, configured with the Black profile.
- Use four spaces for indentation.
- Limit lines to 120 characters.
- Use parentheses for multiline expressions instead of backslash continuations.
- Separate top-level functions and classes with two blank lines.
- Keep imports organized and remove unused imports.
- Use consistent whitespace around operators and after commas.

### 3. Type Annotations and Documentation

- Add type annotations to function parameters and return values.
- Use Google-style docstrings for public modules, classes, and functions where applicable.
- Document the purpose of functions, their arguments, return values, and relevant exceptions.
- Keep functions focused on a single responsibility.

Example:

```python
def calculate_total(item_price: float, item_quantity: int) -> float:
    """Calculate the total price for a specified quantity of items.

    Args:
        item_price: The price of a single item.
        item_quantity: The number of items.

    Returns:
        The total price before tax.
    """
    return item_price * item_quantity
```

### 4. Automated Code Checks

This repository uses **Ruff** to detect naming violations and common Python code issues.

Install the development tools:

```bash
python -m pip install black isort ruff pre-commit
```

Run the checks before submitting changes:

```bash
python -m black .
python -m isort .
python -m ruff check .
```

To check formatting without modifying files:

```bash
python -m black --check .
python -m isort --check-only .
python -m ruff check .
```

### 5. Git Commit Requirements

- Follow the naming and formatting rules before committing code.
-
