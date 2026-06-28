import json, os
from common import ROOT, load_cases

idx={'count':0,'cases':[]}
for c in load_cases():
  idx['cases'].append({'case_id':c['case_id']});
idx['count']=len(idx['cases'])
json.dump(idx, open(os.path.join(ROOT,'data','index.json'),'w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('index built')
