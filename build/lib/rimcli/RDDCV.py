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


def RINMD(rdmod):
    """
    Function to confirm invalid mode.
    """
    UDDCV.SINMD(rdmod)
    UDDCV.SLRMOD(RMDTP.LIST)
    return True


def RMDXT(lspmd):
    """
    Function to extract the string of each mode.
    """
    dmodp = len(lspmd) - 1
    return lspmd[0], lspmd[dmodp], dmodp


def RMDXM(rdmod, lspmd):
    """
    Function to extract welcome message for mode.
    """
    smode, dmode, dmodp = RMDXT(lspmd)
    imode = 1000
    error = False

    if rdmod == smode:
        imode = 0
    elif rdmod == dmode:
        imode = dmodp
    else:
        error = RINMD(rdmod)

    if not error:
        print(RMDTP.SSTART[imode])

    return imode, error
