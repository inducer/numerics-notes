#! /bin/bash

set -euo pipefail

cd
python3 -m venv myenv --system-site-packages
source myenv/bin/activate
pip install jupyterlab jupyterlab_vim 
python -m jupyterlab --ip 0.0.0.0 --no-browser --allow-root



