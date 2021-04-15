import toml
from pathlib import Path

def loadConfig(cfgPath):
    ''' loads toml file containing configurations for model training '''

    with open(cfgPath, 'r') as df:
        tomlString = df.read()
    cfg = toml.loads(tomlString)
    return cfg

def ensure_dir(file_path):
    Path(file_path).mkdir(parents=True, exist_ok=True)