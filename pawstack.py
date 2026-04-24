import sys,shlex,operator as op
s=[]
for w in shlex.split(open(sys.argv[1]).read()):
 if w.replace('.','',1).isdigit():s+=[float(w)]
 elif w in(d:={'+':op.add,'-':op.sub,'*':op.mul,'/':op.truediv,'%':lambda a,b:int(a)%int(b),'==':op.eq,'>':op.gt,'<':op.lt}):b,a=s.pop(),s.pop();s+=[d[w](a,b)]
 elif w in(c:={'int':int,'str':str,'float':float,'lower':lambda x:str(x).lower()}):s+=[c[w](s.pop())]
 elif w=='in':u=input();s+=[int(u)if u.isdigit()else float(u)if u.replace('.','',1).isdigit()else u]
 elif w=='yip':print(s.pop())
 elif w=='eat':s.pop()
 elif w=='paw-at':print(s[-1])
 elif w=='dup':s+=[s[-1]]
 elif w=='pop-all':print('Popping all values:');exec('while s:print(s.pop())')
 elif w=='rev':s+=[str(s.pop())[::-1]]
 elif w=='repeat':s+=[s.pop()*int(s.pop())]
 else:s+=[w]