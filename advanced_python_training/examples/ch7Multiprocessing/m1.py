import subprocess

f = subprocess.run('vim')  # :q at the end to quit
print('code', f.returncode)
