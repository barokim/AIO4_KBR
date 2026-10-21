from pathlib import Path
import importlib.util,contextlib,io,json
from fastapi.testclient import TestClient
base=next(Path('Day6').glob('*'))
def load(rel):
 spec=importlib.util.spec_from_file_location(rel.replace('/','_').replace('.','_'),base/rel)
 mod=importlib.util.module_from_spec(spec)
 with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mod)
 return mod
v=load('ch.04_validator/demo.py')
r={}
s=v.Signup(username='  A  ',password='password12',password_confirm='password12')
r['username_after_constraint']={'value':s.username,'length':len(s.username)}
f=load('ch.03_Field/exercise.py')
r['price_zero_accepted']=f.Product(title='AB',price=0,SKUcode='SKU-0001').price==0
r['sku_prefix_accepted']=f.Product(title='AB',price=1,SKUcode='XXSKU-0001').SKUcode
r['stock_default']=f.Product(title='AB',price=1,SKUcode='SKU-0001').stock
m=load('ch07_FastAPI/app.py');m.reset_demo_data()
c=TestClient(m.app)
cases=[('list','GET','/tasks',None),('create','POST','/tasks',{'title':'  new  '}),('strict_bool','POST','/tasks',{'title':'x','done':'true'}),('blank','POST','/tasks',{'title':'   '}),('extra','POST','/tasks',{'title':'x','foo':1}),('partial','PATCH','/tasks/1',{'done':True}),('null','PATCH','/tasks/1',{'title':None}),('empty','PATCH','/tasks/1',{}),('put_default','PUT','/tasks/1',{'title':'replaced'}),('missing','GET','/tasks/999',None),('path_type','GET','/tasks/abc',None),('delete','DELETE','/tasks/2',None),('deleted','GET','/tasks/2',None)]
r['api']=[]
for name,method,url,data in cases:
 response=c.request(method,url,**({'json':data} if data is not None else {}))
 r['api'].append({'case':name,'status':response.status_code,'body':response.json() if response.content else None})
x=load('ch07_FastAPI/exercise_app.py')
r['unfinished_post']=TestClient(x.app).post('/tasks',json={'title':'x'}).status_code
Path('tmp/day6_paper/checks.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(r,ensure_ascii=True,indent=2))
