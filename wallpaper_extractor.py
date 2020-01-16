import os
import shutil
os.chdir('C:\\')
username = os.environ['USERNAME']
src = "C:\\Users\\"+ username +"\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\"

dst = "C:\\Users\\"+ username +"\\Desktop\\Wallpapers\\"

for file in os.listdir(dst):
    file_path = os.path.join(dst,file)
    base_file_name,ext = os.path.splitext(file)
    if ext == ".jpg":
        
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(e)
for srcfilename in os.listdir(src):
    shutil.copy(src + srcfilename, dst)

for i in os.listdir(dst):
    changed_name = dst + i + ".jpg"
    os.rename(dst + i,changed_name)
    print(changed_name)

        
        
