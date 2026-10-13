
#!/usr/bin/env bash

set -e

PYTHON_VERSION="3.12"
VENV_DIR=".venv"

if ! command -v "python${PYTHON_VERSION}" >/dev/null 2>&1; then
    echo "Python ${PYTHON_VERSION} is required."
    exit 1
fi

"python${PYTHON_VERSION}" -m venv "$VENV_DIR"

PYTHON="$VENV_DIR/bin/python"

"$PYTHON" -m pip install --upgrade pip

if [[ "${1:-}" == "--cuda" ]]; then
    "$PYTHON" -m pip install torch==2.11.0 \
        --index-url https://download.pytorch.org/whl/cu128
fi

"$PYTHON" -m pip install -r requirements.txt

echo "Installation completed."
echo "Activate the environment with: source ${VENV_DIR}/bin/activate"

python3 tools/configure_isaacsim_paths.py
