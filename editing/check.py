import json,re,sys,glob,collections
todo={x['idx']:x for x in json.load(open('todo.json'))}
rev={}
for f in glob.glob('rev/*.json'): rev.update({int(k):v for k,v in json.load(open(f)).items()})
NUM=re.compile(r'-?\d[\d,]*\.?\d*')
CIT=re.compile(r'\b([A-Z][a-zA-ZÀ-ɏ\'-]+)\s*(?:et al\.?|and\s+[A-Z][a-zA-Z\'-]+)?\s*\((\d{4}[a-z]?)\)')
bad=0
for i,new in sorted(rev.items()):
    old=todo[i]['text']
    on=collections.Counter(NUM.findall(old)); nn=collections.Counter(NUM.findall(new))
    if on!=nn:
        print(f'!! {i} NUMBERS  missing={sorted((on-nn).elements())} added={sorted((nn-on).elements())}'); bad+=1
    oc=collections.Counter(CIT.findall(old)); nc=collections.Counter(CIT.findall(new))
    if oc!=nc:
        print(f'!! {i} CITATIONS missing={sorted((oc-nc).elements())} added={sorted((nc-oc).elements())}'); bad+=1
print(f'checked {len(rev)}/{len(todo)} paragraphs; {bad} issues')
