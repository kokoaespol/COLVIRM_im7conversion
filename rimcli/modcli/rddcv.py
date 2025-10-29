#!/usr/bin/env python

# Copyright (C) COLVIRM project 2024
# This project is licensed under the terms of the MIT license.

"""
rddcv.py
Purpose: Read DIC data for computer vision analysis
Acronym: Read_Dic_Data_Computer_Vision
Description: Functions to read DIC data, extraction mode, and
incoming information from the command line relevant
for image refinement and Computer Vision.
"""

import sys

from rimcli.modcli import uddcv


class RMDTP:
    """Class to store reading mode types."""

    IMAGE_READING_MODE_TYPES = ["--single-im7", "--roi-im7"]


def RDCLI():
    """
    Function to read data from the command line interface.

    input: None

    output: error - boolean indicating if there is an error
            sys.argv - command line arguments
    """
    minimum_cli = 3

    # Extract program name
    prgnm = uddcv.SNAME(sys.argv)
    # Show Python version and confirm program running
    uddcv.SPYVR(sys.version)
    uddcv.SPGRN(prgnm)

    # Check for sufficient input data
    if len(sys.argv) < minimum_cli:
        error = uddcv.SINDT()
        return error, sys.argv

    return False, sys.argv


def RDMOD(clinpt):
    """
    Function to read mode for image conversion.

    input: clinpt - command line input

    output: clinpt[1] - mode for image conversion
    """
    return clinpt[1]


def RINMD(rdmod):
    """
    Function to confirm invalid mode.

    input: rdmod - mode for image conversion

    output: error - boolean indicating if mode is invalid
    """
    error = uddcv.SINMD(rdmod)
    uddcv.SLRMOD(RMDTP.IMAGE_READING_MODE_TYPES)
    return error


def RMDXT(lspmd):
    """
    Function to extract the string of each mode.

    input: lspmd - list of modes

    output: lspmd[0] - single mode
            lspmd[dmodp] - default mode
            dmodp - index of the last mode
    """
    dmodp = len(lspmd) - 1
    return lspmd[0], lspmd[dmodp], dmodp


def RMDXM(rdmod, lspmd):
    """
    Function to extract welcome message for mode.

    input: rdmod - mode for image conversion
           lspmd - list of modes

    output: imode - index of the mode
            error - boolean indicating if mode is invalid
    """
    OUTPUT_STRING_MODES = [
        "***Single-file mode***",
        "***Single-file mode (default)***",
        "***ROI refinement mode***",
    ]
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
        print(OUTPUT_STRING_MODES[imode])
    return imode, error
