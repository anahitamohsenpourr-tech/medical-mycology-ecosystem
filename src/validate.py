from common import load_cases, load_vocabulary

v=load_vocabulary()
for c in load_cases():
  assert c['case_id']
print('OK')
