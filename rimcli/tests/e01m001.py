#!/usr/bin/env python

# First automated test
# e01m001: <e>xample of testing category <01> for i<m>7 images. Test number <0001>

def test(file):
    import os
    import subprocess
    path = os.path.dirname(file)
    imgdat = '/B00001.im7'
    path = path + imgdat
    print('Testing started in ',path)
    subprocess.run(['rim-cli --single-im7 ' + path],shell=True, executable="/bin/bash")
    print('Testing ended in ',path)
    
if __name__=='__main__':
    from rimcli.tests.data import datlnk
    test(datlnk.__file__)
