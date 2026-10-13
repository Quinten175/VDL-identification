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

### 2. Git Commit Requirements

- Follow the naming and formatting rules before committing code.
-
