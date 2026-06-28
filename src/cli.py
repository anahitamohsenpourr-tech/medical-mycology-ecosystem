from common import load_vocabulary
from matcher import match

print('Medical Mycology CLI (decision support only)')
print('---')
v=load_vocabulary()
query={
  'host_factors':['immunocompetent'],
  'immune_status':'immunocompetent',
  'presentation':{'site':['lung'],'key_signs':['lung_mass','chronic_cough'],'onset':'chronic'}
}
top,_=match(query,3)
for t in top:
  print(t['case']['case_id'], t['score'])
