import sys, os, subprocess, tempfile, string, random, atexit


_created_files = []

def temp_help(helpstr):
    stdout = sys.stdout
    fpath = os.path.join(tempfile.gettempdir(),
                         ''.join([random.choice(string.ascii_letters + string.digits) for trash in range(16)]))
    f = open(fpath, 'w')
    sys.stdout = f
    help(helpstr)
    sys.stdout = stdout
    f.close()
    subprocess.Popen('n++ "%s"'%fpath, shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
    _created_files.append(fpath)

@atexit.register
def _cleanup():
    for f in _created_files:
        if os.path.isfile(f):
            os.remove(f)
