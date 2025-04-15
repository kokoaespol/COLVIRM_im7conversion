#!/usr/bin/env python

# First automated test
# e01m001: <e>xample of testing category <01> for i<m>7 images. Test
# number <0001>


# Function to test rum-cli functionality
def test(file):
    # Import subprocess execution module
    import subprocess

    # Import pathway manipulation module
    import pathlib

    # Construct full path to image
    base_dir = pathlib.Path(file).parent
    imgdat = "B00001.im7"
    image_path = base_dir / imgdat

    # Execute rim-cli with single-image mode
    print("Testing started in ", image_path)
    result = subprocess.run(["rim-cli", "--single-im7", str(image_path)], shell=True)

    # Verify command execution success
    if result.returncode != 0:
        print(f"Error executing command: {result.stderr}")

    print("Testing ended in ", image_path)


if __name__ == "__main__":
    # Import data linking module
    from rimcli.tests.data import datlnk

    # Execute test with data link file
    test(datlnk.__file__)
