#!/usr/bin/env python

# Copyright (C) COLVIRM project 2024
# This project is licensed under the terms of the MIT license.

"""
uddcv.py
Purpose: Utilities for DIC data and computer vision analysis
Acronym: Utilities_Dic_Data_Computer_Vision
Description: Common utilities used for DIC data reading, refinement
and format conversion for preparation to carry out
Computer Vision analyses.
"""


# Function to show exit string
def SEXIT(error, clinpt):
    """
    Function to print exit message depending on program execution.

    input:  error  - boolean indicating if error occurred
            clinpt - command line input

    output: None
    """
    prgnm = SNAME(clinpt)
    if error:
        print(prgnm, "run aborted!")
    else:
        print(prgnm, "run successfully completed!")
    return None


# Function to extract python script name
def SNAME(clinpt):
    """
    Function to extract the program name.

    input:  clinpt - command line input

    output: prgnm - program name
    """
    prgnm = clinpt[0]
    return prgnm


# Function to show Python version
def SPYVR(pyvrs):
    """
    Function to display Python version in use.

    input:  pyvrs - Python version string

    output: None
    """
    print("Python version in use:", pyvrs)
    return None


# Function to confirm program is running
def SPGRN(prgnm):
    """
    Function to display that the program is running.

    input:  prgnm - program name

    output: None
    """
    print("Running", prgnm, "as python script...")
    return None


# Function to clarify insufficient input data
def SINDT():
    """
    Function to show error for insufficient input data.

    input:  None

    output: error - boolean flag indicating error
    """
    print("Insufficient command-line inputs")
    error = True
    return error


# Function to output list of supported modes
def SLRMOD(lspmd):
    """
    Function to display list of supported modes.

    input:  lspmd - list of modes

    output: None
    """
    print("List of supported modes:")
    imode = 0
    for modes in lspmd:
        imode = imode + 1
        print(imode, ".", modes)
    return None


# Function to confirm invalid reading mode
def SINMD(rdmod):
    """
    Function to show error message for invalid mode.

    input:  rdmod - reading mode string

    output: error - boolean flag indicating error
    """
    print("Command-line input for mode:", rdmod, ", is invalid")
    error = True
    return error


# Function to get im7 file name from cli
def FNMCL(clinpt):
    """
    Function to extract .im7 file name from command line input.

    input:  clinpt - command line input

    output: iname  - full image file name with extension
            imname - base image file name without extension
    """
    LIM7 = FMIM7.LIM7
    FRIM7 = FMIM7.FRIM7
    imname = clinpt[2]
    lname = len(imname)
    lim7 = LIM7
    fmpos = lname - lim7
    formt = imname[fmpos:lname]
    if not formt == FRIM7:
        iname = imname + FRIM7
    else:
        iname = imname
        imname = imname[:fmpos]
    return iname, imname


# Class: information of .im7 format
class FMIM7:
    """
    Class to store .im7 file format information.
    """

    FRIM7 = ".im7"
    LIM7 = len(FRIM7)


# Function to detect inexisting file
def FNFND(iname):
    """
    Function to check if a file exists.

    input:  iname - full image file name

    output: error - boolean indicating if file was not found
    """
    import os

    PATH = os.path
    FEXST = PATH.isfile
    error = False
    ffnd = FEXST(iname)
    if not ffnd:
        print("DIC file", iname, "not found")
        error = True
    return error


# Function to show string of image-level
def SIMLAY(iname):
    """
    Function to print messages for image-level operation.

    input:  iname - full image file name

    output: None
    """
    print("Operating at im7-file level")
    print("Name of im7 file:", iname)
    return None


# Function to show image array settings
def SIRST(ncamr, pxlr, pxlc, imtype):
    """
    Function to show image array properties.

    input:  ncamr  - number of cameras
            pxlr   - pixel rows
            pxlc   - pixel columns
            imtype - image channel type

    output: None
    """
    sncamr = SDEMS("Number of cameras in DIC:")
    print(sncamr, ncamr)
    spxl = SDEMS("Camera pixel resolution:")
    print(spxl, pxlr, "x", pxlc)
    sityp = SDEMS("Image channel type:")
    print(sityp, imtype)
    return None


# Function to merge double empty space before a string
def SDEMS(string):
    """
    Function to add empty space before a string.

    input:  string - original string

    output: string - modified string
    """
    empty = "  "
    string = empty + string
    return string


# Function to merge arrow before a string
def SAROW(string):
    """
    Function to add arrow before a string.

    input:  string - original string

    output: string - modified string
    """
    arrow = "-> "
    string = arrow + string
    return string


# Function to confirm camera no. in use
def SCMRA(icamr):
    """
    Function to display selected camera number.

    input:  icamr - camera number

    output: None
    """
    message = SAROW("Importing from camera no.:")
    message = SDEMS(message)
    print(message, icamr)
    return None


# Function to create image name from type and camera number
def SINAME(imname, imtype, icamr):
    """
    Function to generate full image name with type and camera number.

    input:  imname - base image name
            imtype - image channel type
            icamr  - camera number

    output: siname - full structured image name
    """
    sitype = str(imtype)
    sicamr = str(icamr)
    siname = SUSCR(imname)
    siname = siname + sitype
    siname = SUSCR(siname)
    siname = siname + sicamr
    return siname


# Function to confirm image saved
def SISAVE(siname):
    """
    Function to confirm image was saved.

    input: siname - name of the saved image

    output: None - prints confirmation message
    """
    message = "New image saved as"
    message = SAROW(message)  # Add arrow to message
    message = SDEMS(message)  # Add spacing to message
    print(message, siname)
    return None


# Function to add underscore to string
def SUSCR(string):
    """
    Function to add an underscore to a string.

    input: string - original string

    output: string - string with appended underscore
    """
    uscr = "_"
    string = string + uscr
    return string


def XTROI(clinpt):
    """
    Function to extract ROI (Region of Interest) coordinates from command line input.

    input:  clinpt - command line input

    output: ROI_x1 - x1-coordinate of the ROI
            ROI_x2 - x2-coordinate of the ROI
            ROI_y1 - y1-coordinate of the ROI
            ROI_y2 - y2-coordinate of the ROI
    """
    ROI_x1 = int(clinpt[3])
    ROI_x2 = int(clinpt[4])
    ROI_y1 = int(clinpt[5])
    ROI_y2 = int(clinpt[6])
    return ROI_x1, ROI_x2, ROI_y1, ROI_y2