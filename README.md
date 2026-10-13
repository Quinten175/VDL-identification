# VDL-identification

# Python Code Style Guidelines

All Python code in this repository must follow
the [NVIDIA Isaac Sim Python coding guidelines](https://docs.isaacsim.omniverse.nvidia.com/latest/py/docs/overview/guidelines.html)
and PEP 8 conventions. These rules help maintain consistent, readable, and maintainable code across all contributors.

## 1. Naming Conventions

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

Use meaningful names that describe the purpose of a variable, function, class, or module. Avoid ambiguous names and
unnecessary abbreviations.

## 2. Git Commit Requirements

- Follow the naming and formatting rules before committing code.
-

# Isaac Sim Extensions in VS Code and PyCharm

## Overview

Isaac Sim extensions, such as `omni.replicator.core`, are installed inside the Isaac Sim package. IDEs may not automatically index these extensions, causing unresolved import warnings and missing autocomplete.

This project uses a setup script to discover installed Isaac Sim extension directories and configure Python's import paths automatically.

## Setup

The extension path configuration is handled by:

```text
tools/configure_isaacsim_paths.py
```

The script discovers available extension directories in the active `.venv` and creates a `.pth` file in `site-packages` to add the discovered paths.

The setup is specific to the active virtual environment and should be run after installing or updating Isaac Sim.

## VS Code

1. Open the project in VS Code.
2. Select the project's `.venv/bin/python` using **Python: Select Interpreter**.
3. Ensure `.vscode/settings.json` contains:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
    "python.analysis.indexing": true,
    "python.analysis.autoImportCompletions": true
}
```

4. Reload VS Code or restart the Pylance language server if imports remain unresolved.

## PyCharm

1. Open **Settings → Project → Python Interpreter**.
2. Select the project's `.venv/bin/python`.
3. Keep `.venv` excluded from ordinary project source roots.
4. If extensions remain unresolved, configure the relevant extension directories as interpreter paths or source roots for code analysis.

## Important

- Do not install a separate package named `omni`.
- `omni.replicator.core` is an Isaac Sim extension.
- IDE indexing settings improve autocomplete and import resolution but do not initialize Isaac Sim's Kit runtime.
- For runtime execution, initialize `SimulationApp` before importing Replicator or other Kit extensions.
- Native or dynamically generated APIs may not be fully understood by the IDE.