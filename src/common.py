import json, os, glob
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA=os.path.join(ROOT,'data')
CASES_DIR=os.path.join(DATA,'cases')

def load_json(p):
  return json.load(open(p,encoding='utf-8'))

def load_vocabulary():
  return load_json(os.path.join(DATA,'vocabulary.json'))

def load_weights():
  w=load_json(os.path.join(DATA,'weights.json')); return w

def load_cases():
  return [load_json(p) for p in sorted(glob.glob(os.path.join(CASES_DIR,'*.json')))]
