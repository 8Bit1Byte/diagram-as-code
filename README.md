# diagram-as-code

### Create Virtual Environment
1. Open Powershell (or any shell you want)
2. python -m venv venv
3. To activate this newally create enivronment run this in shell
    -   ./venv/Scripts/activate.ps1
4. Now clone this repo
    -  git clone https://github.com/8Bit1Byte/diagram-as-code.git
5. Go to directory diagram-as-code
    - cd diagram-as-code/
6. Run the blackbox.py and it will generate output_data.py form input_data.json
    - python blackbox.py (generate output_data.py)
7. Run the output_data.py
    - python input_data.json (generate architecture image)