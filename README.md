# airsim-testing

## File Structure

```
airsim-testing/
├── tests/
│   └── test_takeoff.py
├── utils/
│   └── client_wrapper.py
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt
```

## Setup

```
brew install python@3.11
python3.11 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install numpy
pip install msgpack-rpc-python
pip install airsim pytest

export PYTHONPATH=$(pwd)
pytest tests/
```
