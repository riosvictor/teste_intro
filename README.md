python3 -m venv ./env    
source ./env/bin/activate
pip install unittest2
python -m unittest -v test.py

python -m unittest -v api_test.py