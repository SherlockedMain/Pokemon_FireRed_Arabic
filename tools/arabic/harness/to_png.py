import sys,glob,os
from PIL import Image
for f in glob.glob(sys.argv[1]+'/*.raw'):
    im=Image.frombytes('RGB',(240,160),open(f,'rb').read()); im.resize((480,320),Image.NEAREST).save(f[:-4]+'.png'); os.remove(f)
