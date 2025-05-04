#!/usr/bin/env python

# Copyright (C) COLVIRM project 2024
# This project is licensed under the terms of the MIT license.
# *PYTHON MODULE
# RDDCV.py
# *PURPOSE
# Read DIC data for computer vision analysis
# *ACRONYM
# Read_Dic_Data_Computer_Vision
# *DESCRIPTION
# Handles command-line input to select and validate 
# DIC image processing modes. Provides mode detection,
# user messaging, and input verification for image 
# refinement workflows in computer vision.
# *HISTORY
# NAME DATE   DESCRIPTION
# CAG  Jun24  Initial coding

import sys
from rimcli.modcli import UDDCV

# Class to store reading mode types
class RMDTP:
    # List of valid command-line mode flags
    LIST = ["--single-im7", "--default"]
    # Corresponding mode start messages
    SSTART = ["***Single-file mode***", "***Single-file mode (default)***"]


# Class to store calling format
class RFORM:
    # Minimum number of CLI inputs required
    MINL = 3


# Function to read data from command-line interface
def RDCLI():
    # Extract program name
    prgnm = UDDCV.SNAME(sys.argv)
    # Show Python version
    UDDCV.SPYVR(sys.version)
    # Confirm program is running
    UDDCV.SPGRN(prgnm)
    # Check if input length is less than minimum required
    if len(sys.argv) < RFORM.MINL:
        # Show insufficient data message and set error flag
        error = UDDCV.SINDT()
        # Return error flag and CLI input
        return error, sys.argv
    # Return no error and CLI input
    return False, sys.argv


# Function to read mode from CLI input
def RDMOD(clinpt):
    # Return second CLI argument as reading mode
    return clinpt[1]


# Function to confirm invalid mode
def RINMD(rdmod):
    # Show invalid mode message
    UDDCV.SINMD(rdmod)
    # Show list of supported modes
    UDDCV.SLRMOD(RMDTP.LIST)
    # Return error flag
    return True


# Function to extract mode strings from list
def RMDXT(lspmd):
    # Calculate index of default mode
    dmodp = len(lspmd) - 1
    # Return single mode, default mode, and default index
    return lspmd[0], lspmd[dmodp], dmodp


# Function to extract welcome message for mode
def RMDXM(rdmod, lspmd):
    # Extract single, default modes and index
    smode, dmode, dmodp = RMDXT(lspmd)
    # Initialize mode index with large number
    imode = 1000
    # Initialize error flag
    error = False
    # Mode matches single mode
    if rdmod == smode:
        imode = 0
    # Mode matches default mode
    elif rdmod == dmode:
        imode = dmodp
    # Mode is invalid
    else:
        error = RINMD(rdmod)
    # Show welcome message if mode is valid
    if not error:
        print(RMDTP.SSTART[imode])
    # Return mode index and error flag
    return imode, error
