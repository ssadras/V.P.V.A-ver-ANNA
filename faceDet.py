>>> import subprocess
>>> cmd = [ 'echo', 'arg1', 'arg2' ]
>>> output = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
>>> print output
