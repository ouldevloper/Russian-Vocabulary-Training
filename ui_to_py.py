import glob
import os


[os.popen(f"pyuic5 -x {file} > {file.removesuffix('.ui')}.py") for file in glob.glob("*.ui")]