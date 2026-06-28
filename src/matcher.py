from common import load_cases, load_weights, load_vocabulary

def _jacc(q,c):
  q=set(q or []); c=set(c or []);
  if not q and not c: return 0,0,[]
  o=q&c; return len(o), len(q|c), sorted(o)

def score_case(query, case, weights):
  raw=0.0; max_raw=0.0; contrib=[]
  def add(name,w,q,c):
    nonlocal raw,max_raw
    max_raw+=w
    o,u,items=_jacc(q,c)
    if u: raw+=w*(o/u)
    if items: contrib.append((name,items))
  pq=query.get('presentation',{}); pc=case.get('presentation',{})
  add('host_factors',weights['host_factors'],query.get('host_factors'),case.get('host_factors'))
  add('immune_status',weights['immune_status'],[query.get('immune_status')],[case.get('immune_status')])
  add('site',weights['site'],pq.get('site'),pc.get('site'))
  add('key_signs',weights['key_signs'],pq.get('key_signs'),pc.get('key_signs'))
  add('onset',weights['onset'],[pq.get('onset')],[pc.get('onset')])
  s=round((raw/max_raw)*100,1) if max_raw else 0
  return s, contrib

def match(query, top_n=3):
  weights=load_weights(); out=[]
  for c in load_cases():
    s,contrib=score_case(query,c,weights)
    out.append({'case':c,'score':s,'contributions':contrib})
  out.sort(key=lambda x:x['score'], reverse=True)
  return out[:top_n], []
