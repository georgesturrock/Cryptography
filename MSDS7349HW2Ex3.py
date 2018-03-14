#  import AES from pycrypto version 2.6
#  installed from sudo apt-get python-crypto
#
#  credit to:
#  https://www.thehackr.com/encrypt-and-decrypt-images-using-python/
#  https://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto
#  https://stackoverflow.com/questions/44314026/how-to-create-image-from-binary-string
#  https://stevenwooding.com/python-example-encryption-using-aes-in-counter-mode/

import os
import random
import struct
from Crypto.Cipher import AES
from Crypto.Util import Counter
from PIL import Image

#  set key and initialization vector
ekey = '0123456789abcdef'
IV = '0123456789012345'
newsize='256,256'

#  Open image to encrypt and extract byte data
jpgimage = Image.open('/home/gsturrock/Pictures/chrome.jpg')
jpgimage.show()
jpgimage_src = jpgimage.tobytes()
print('Original Length:', len(jpgimage_src), jpgimage.size)

#  CBC encryption
encryptor = AES.new(ekey, AES.MODE_CBC, IV)
cbc_crypt = encryptor.encrypt(jpgimage_src)
jpgimage_enc = Image.frombytes('RGB', jpgimage.size, cbc_crypt)
jpgimage_enc.show()
jpgimage_enc.save('CBCchrome.jpg')

#  ECB encryption
encryptor = AES.new(ekey, AES.MODE_ECB)
ebc_crypt = encryptor.encrypt(jpgimage_src)
jpgimage_enc = Image.frombytes('RGB', jpgimage.size, ebc_crypt)
jpgimage_enc.show()
jpgimage_enc.save('EBCchrome.jpg')

#  Counter Mode encryption
#  create random 16 bit character
rctr = os.urandom(16)
#  create encoded 128bit counter to feed into AES.new
ctr = Counter.new(128, initial_value=long(rctr.encode('hex'), 16))
encryptor = AES.new(ekey, AES.MODE_CTR, counter=ctr)
ctr_crypt = encryptor.encrypt(jpgimage_src)
jpgimage_enc = Image.frombytes('RGB', jpgimage.size, ctr_crypt)
jpgimage_enc.show()
jpgimage_enc.save('CTRchrome.jpg')
