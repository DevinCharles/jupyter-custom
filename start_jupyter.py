from subprocess import run, Popen
from time import sleep
import os

browser_path = 'C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\chrome_proxy.exe'

nb_folder = os.path.expanduser('~')+'\\Documents\\Notebooks'
if not os.path.exists(nb_folder):
    os.makedirs(nb_folder)
# startup.sh should be saved in Notebooks folder (nb_folder) and contain:
# zotero --headless & start.sh jupyter lab --LabApp.token='notebook'
cmd = r"docker run --rm --name=jupyter --env JUPYTER_RUNTIME_DIR=/tmp -v "+nb_folder+":/home/jovyan -p 8888:8888 jupyter/custom /home/jovyan/startup.sh"
print(cmd)
try:
    print('Killing Container')
    run('docker rm --force jupyter')
except:
    print('Could not kill container')
    
try:
    Popen(cmd)
    sleep(2.5)
    Popen([browser_path,'--app=http://127.0.0.1:8888/?token=notebook'])
except:
    print('Failed to start container')
    exit
