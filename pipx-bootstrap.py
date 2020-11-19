import glob
import runpy
import subprocess
import sys
import tempfile

if sys.version_info < (3, 6):
    sys.exit('python 3.6+ is required')

with tempfile.TemporaryDirectory() as tmp:
    subprocess.check_call([
        sys.executable, '-m', 'pip',
        'download', '--only-binary', ':all:', '--dest', tmp, 'pipx',
    ])
    sys.path = glob.glob(f'{tmp}/*.whl') + sys.path
    sys.argv = ['pipx', 'install', 'pipx'] + sys.argv[1:]
    runpy.run_module('pipx', run_name='__main__')
