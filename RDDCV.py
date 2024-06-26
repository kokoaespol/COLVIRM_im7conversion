#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Copyright (C) COLVIRM project 2024
# This project is licensed under the terms of the MIT license.
#*PYTHON MODULE
# RDDCV.py
#*PURPOSE
# Read DIC data for computer vision analysis
#*ACRONYM
# Read_Dic_Data_Computer_Vision
#*DESCRIPTION
# Functions to read DIC data, extraction mode and
# incoming information from command line relevant
# for image refinement and Computer Vision
#*HISTORY
# NAME DATE   DESCRIPTION
# CAG  Jun24  Initial coding

# Function to Read Data from Command Line Interface
def RDCLI():
## Import modules
    # Import python system data module
    import sys
    # Import utilities for DIC data
    import UDDCV
## Rename module-mapped functions 
    # Python version
    pyvrs  = sys.version
    # CLI input from interpreter
    clinpt = sys.argv
    # Extract program name
    SNAME  = UDDCV.SNAME
    # Show python version
    SPYVR  = UDDCV.SPYVR
    # Confirm program running
    SPGRN  = UDDCV.SPGRN
    # String for insufficient data input
    SINDT  = UDDCV.SINDT
    # Extract minimum length of input data
    MINL   = RFORM.MINL
## Initialise error flag    
    error  = False
## Extract python and command line data
    # Extract program name
    prgnm  = SNAME(clinpt)
## Show python and command line data
    # Show python version
    SPYVR(pyvrs)
    # Confirm program in use
    SPGRN(prgnm)
## Check for admissible clinpt
    # Length of input data
    lclinp = len(clinpt)
    # Minimum input data
    mincli = MINL
## Insufficient minimum data
    if lclinp < mincli: error = SINDT()
    # Return
    return error,clinpt

# Function to Read Mode for image conversion
def RDMOD(clinpt):
    # Reading mode
    rdmod = clinpt[1]
    # Return
    return rdmod

# Class to store reading mode types
class RMDTP:
    # List of image reading modes, ends with default
    LIST   = ["--single-im7",
              "--default"   ]
    # Output string for each mode, ends with default
    SSTART = ["***Single-file mode***"          ,
              "***Single-file mode (default)***"]

# Class to store calling format
class RFORM:
    # Minimum number of command-line inputs
    MINL = 3

# Function to confirm invalid mode
def RINMD(rdmod):
## Import modules
    # Import utilities for DIC data
    import UDDCV
## Rename module-mapped functions
    # Print list of strings of modes
    SLRMOD = UDDCV.SLRMOD
    # String to confirm invalid mode
    SINMD  = UDDCV.SINMD
    # List of supported modes
    LIST   = RMDTP.LIST
## Confirm invalid and available modes
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
## Available modes
    # First mode: single file
    smode = lspmd[0]
    # Next mode: position [1] reserved
    pass
    # Last mode: default
    dmode = lspmd[dmodp]
    # Return
    return smode,dmode,dmodp

# Function to extract welcome message for mode
def RMDXM(rdmod,lspmd):
## Rename mapped functions and classes
    # Strings of welcome message for each mode
    SSTART = RMDTP.SSTART
## Initialise error flag
    error = False
## Mode detection
    # Extract mode strings & default mode position
    smode,dmode,dmodp = RMDXT(lspmd)
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
    return imode,error

