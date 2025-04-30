#!/usr/bin/env python

# Copyright (C) COLVIRM project 2024
# This project is licensed under the terms of the MIT license.

"""
RDDCV.py
Purpose: Read DIC data for computer vision analysis
Acronym: Read_Dic_Data_Computer_Vision
Description: Functions to read DIC data, extraction mode, and
incoming information from the command line relevant
for image refinement and Computer Vision.
"""

import sys
from rimcli.modcli import UDDCV


class RMDTP:
    """Class to store reading mode types."""
    LIST = ["--single-im7", "--default"]
    SSTART = ["***Single-file mode***", "***Single-file mode (default)***"]


class RFORM:
    """Class to store calling format."""
    MINL = 3



# Function to Read Data from Command Line Interface
def RDCLI():
    """
    Function to read data from the command line interface.
    """
    # Extract program name
    prgnm = UDDCV.SNAME(sys.argv)
    # Show Python version and confirm program running
    UDDCV.SPYVR(sys.version)
    UDDCV.SPGRN(prgnm)

    # Check for sufficient input data
    if len(sys.argv) < RFORM.MINL:
        error = UDDCV.SINDT()
        return error, sys.argv

    return False, sys.argv


def RDMOD(clinpt):
    """
    Function to read mode for image conversion.
    """
    return clinpt[1]

# Function to confirm invalid mode
def RINMD(rdmod):
    # Import modules
    # Import utilities for DIC data
    from rimcli.modcli import UDDCV

    # Rename module-mapped functions
    # Print list of strings of modes
    SLRMOD = UDDCV.SLRMOD
    # String to confirm invalid mode
    SINMD = UDDCV.SINMD
    # List of supported modes
    LIST = RMDTP.LIST
    # Confirm invalid and available modes
    # Extract list of supported modes
    lspmd = LIST
    # Confirm invalid mode
    error = SINMD(rdmod)
    # Print list of supported modes
    SLRMOD(lspmd)
    # Return
    return error


# Function to extract the string of each mode
def RMDXT(lspmd):
    # Length of supported mode list
    nmode = len(lspmd)
    # Last mode position: default
    dmodp = nmode - 1
    # Available modes
    # First mode: single file
    smode = lspmd[0]
    # Next mode: position [1] reserved
    pass
    # Last mode: default
    dmode = lspmd[dmodp]
    # Return
    return smode, dmode, dmodp


# Function to extract welcome message for mode
def RMDXM(rdmod, lspmd):
    # Rename mapped functions and classes
    # Strings of welcome message for each mode
    SSTART = RMDTP.SSTART
    # Initialise error flag
    error = False
    # Mode detection
    # Extract mode strings & default mode position
    smode, dmode, dmodp = RMDXT(lspmd)
    # Set mode number to an initial high value
    imode = 1000
    # Reading image as single mode
    if rdmod == smode:
        # Single mode position
        imode = 0
    # Reading image as default mode
    elif rdmod == dmode:
        # Default mode position
        imode = dmodp
    # Reading mode invalid
    else:
        # Switch on flag for invalid mode
        error = RINMD(rdmod)
    # Valid mode from input
    if not error:
        # String for starting the mode
        ssmod = SSTART[imode]
        # Welcome message to the current mode
        print(ssmod)
    # Return
    return imode, error
