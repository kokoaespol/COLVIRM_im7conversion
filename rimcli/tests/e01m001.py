#!/usr/bin/env python

# First automated test
# e01m001: <e>xample of testing category <01> for i<m>7 images. Test
# number <0001>


# Function to test rum-cli functionality
def test(file):
    """
    Test the rim-cli command line interface.
    This test runs the rim-cli command line interface
    on a single im7 image file. The input file is
    B00001.im7, which is a DIC image file.
    Parameters
    ----------
    file : str
        The path to the im7 image file to be tested.
    Returns
    -------
    None
    example
    -------
    test('/path/to/image.im7')
    """
    import pathlib
    import subprocess

    base_dir = pathlib.Path(file).parent
    imgdat = "B00001.im7"
    image_path = base_dir / imgdat
    print("Testing started in ", image_path)
    result = subprocess.run(["rim-cli", "--single-im7", str(image_path)], shell=False)
    if result.returncode != 0:
        print(f"Error executing command: {result.stderr}")
    print("Testing ended in ", image_path)


# Execute test with data link file
if __name__ == "__main__":
    from rimcli.tests.data import datlnk

    test(datlnk.__file__)
