import json,re,sys,glob,collections
NUM=re.compile(r'-?\d[\d,]*\.?\d*')
CIT=re.compile(r'\b([A-Z][a-zA-ZÀ-ɏ\'-]+)\s*(?:et al\.?|and\s+[A-Z][a-zA-Z\'-]+)?\s*\((\d{4}[a-z]?)\)')
AI=re.compile(r'\b(moreover|furthermore|delve|underscor\w*|crucial|pivotal|robust|comprehensive|notably|holistic|multifaceted|nuanced|intricate|showcas\w*|leverag\w*|landscape|realm|testament|seamless|myriad|plethora|tapestry|cornerstone|paradigm|foster\w*|harness\w*|navigat\w*|elevate the|unlock\w*|it is worth noting|in essence|in conclusion|overall,)\b',re.I)
import json as _j
EXC=_j.load(open('exp/exceptions.json'))
tot=0;bad=0
for k in ('E1','E2','E3'):
    todo={x['idx']:x for x in json.load(open(f'exp/todo_{k}.json'))}
    rev={}
    for f in glob.glob(f'exp/rev/{k}_*.json'): rev.update({int(a):b for a,b in json.load(open(f)).items()})
    for i,new in sorted(rev.items()):
        old=todo[i]['text']; tot+=1
        on,nn=collections.Counter(NUM.findall(old)),collections.Counter(NUM.findall(new))
        if on!=nn and f'{k}:{i}' not in EXC: print(f'!! {k}:{i} NUMBERS missing={sorted((on-nn).elements())} added={sorted((nn-on).elements())}');bad+=1
        oc,nc=collections.Counter(CIT.findall(old)),collections.Counter(CIT.findall(new))
        if oc!=nc: print(f'!! {k}:{i} CITATIONS missing={sorted((oc-nc).elements())} added={sorted((nc-oc).elements())}');bad+=1
        if '—' in new or '–' in new.replace('–','',new.count('–') if re.search(r'\d–\d',new) else 0):
            if '—' in new: print(f'!! {k}:{i} EM DASH');bad+=1
        hits=set(m.group(0).lower() for m in AI.finditer(new)) - set(m.group(0).lower() for m in AI.finditer(old))
        if hits: print(f'!! {k}:{i} AI-TELL {sorted(hits)}');bad+=1
    print(f'{k}: {len(rev)}/{len(todo)} revised')
print(f'total {tot} checked; {bad} issues')
