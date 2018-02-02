# IPython log file

raise NotImplemented()
raise NotImplemented
try:
    raise NotImplemented()
except e:
    print(e)
    
try:
    raise NotImplemented()
except Exception as e:
    print(e)
    
try:
    raise NotImplementedError()
except Exception as e:
    print(e)
    
try:
    raise NotImplementedError('')
except Exception as e:
    print(e)
    
try:
    raise NotImplementedError('II')
except Exception as e:
    print(e)
    
    
get_ipython().run_line_magic('logstart', '')
