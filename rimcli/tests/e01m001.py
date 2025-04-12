#!/usr/bin/env python

# First automated test
# e01m001: <e>xample of testing category <01> for i<m>7 images. Test
# number <0001>


def test(file):
    import pathlib
    import subprocess

    base_dir = pathlib.Path(file).parent
    imgdat = "B00001.im7"
    image_path = base_dir / imgdat
    print("Testing started in ", image_path)
    result = subprocess.run(["rim-cli", "--single-im7", str(image_path)], shell=True)

    if result.returncode != 0:
        print(f"Error executing command: {result.stderr}")

    print("Testing ended in ", image_path)


if __name__ == "__main__":
    from rimcli.tests.data import datlnk

    test(datlnk.__file__)
