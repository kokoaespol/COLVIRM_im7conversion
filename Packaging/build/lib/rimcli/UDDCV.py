#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Copyright (C) COLVIRM project 2024
# This project is licensed under the terms of the MIT license.
#*PYTHON MODULE
# UDDCV.py
#*PURPOSE
# Utilities for DIC data and computer vision analysis
#*ACRONYM
# Utilities_Dic_Data_Computer_Vision
#*DESCRIPTION
# Common utilities used for DIC data reading, refinement
# and format conversion for preparation to carry out
# Computer Vision analyses
#*HISTORY
# NAME DATE   DESCRIPTION
# CAG  Jun24  Initial coding

# Function to show exit string
def SEXIT(error,clinpt):
    # Extract program name
    prgnm = SNAME(clinpt)
## Program run not completed
    if error == True:
        # Exit string on aborted run
        print(prgnm,"run aborted!")
## Program run completed
    else:
        # Exit string on successful run
        print(prgnm,"run successfully completed!")
    # Return
    return None

# Function to extract python script name
def SNAME(clinpt):
    # Python program name
    prgnm = clinpt[0]
    # Return
    return prgnm

# Function to show Python version
def SPYVR(pyvrs):
    # Show python version
    print("Python version in use:",pyvrs)
    # Return
    return None

# Function to confirm program is running
def SPGRN(prgnm):
    # Show message of program running
    print("Running",prgnm,"as python script...")
    # Return
    return None

# Function to clarify insufficient input data
def SINDT():
    # Insufficient input data
    print("Insufficient command-line inputs")
    # Switch on error flag
    error = True
    # Return
    return error

# Function to output list of supported modes
def SLRMOD(lspmd):
    # List of modes
    print("List of supported modes:")
    # Initialise mode pointer
    imode = 0
    # Loop over available reading modes
    for modes in lspmd:
        # Advance mode pointer
        imode = imode + 1 
        # Print available mode
        print(imode,".",modes)
    # Return    
    return None

# Function to confirm invalid reading mode
def SINMD(rdmod):
    # Current mode is invalid
    print("Command-line input for mode:",rdmod,", is invalid")
    # Switch on error flag
    error = True
    # Return
    return error

# Function to get im7 file name from cli
def FNMCL(clinpt):
## Rename module-mapped classes
    # Extract length of .im7
    LIM7   = FMIM7.LIM7
    # Extract .im7
    FRIM7  = FMIM7.FRIM7
## Extract file name
    # Record File name
    imname = clinpt[2]
    # Length of file name
    lname  = len(imname)
## Autodetection of file format    
    # Length of .im7 as string
    lim7   = LIM7
    # Start position of .im7 string
    fmpos  = lname - lim7
    # Extract (expected) format
    formt  = imname[fmpos:lname]
    # Format not declared explicitly
    if not formt == FRIM7:
        # File name with format
        iname  = imname + FRIM7
    # Format declared explicitly
    else:
        # File name with format
        iname  = imname
        # Subtract format
        imname = imname[:fmpos]
    # Return
    return iname,imname

# Class: information of .im7 format
class FMIM7:
    # The im7 as string
    FRIM7 = ".im7"
    # Length of the format string
    LIM7  = len(FRIM7)

# Function to detect inexisting file
def FNFND(iname):
## Import modules
    # Python-OS module
    import os
## Rename module-mapped functions
    # Extract path
    PATH  = os.path
    # Detect existing file
    FEXST = PATH.isfile
## Initialise error flag
    error = False
## Detect if file exists    
    # Flag to confirm file exists
    ffnd = FEXST(iname)
    # File not found
    if not ffnd:
        # DIC file not found
        print("DIC file",iname,"not found")
        # Switch on error flag
        error = True
    # Return
    return error

# Function to show string of image-level
def SIMLAY(iname):
    # Confirm im7 image-level operation
    print("Operating at im7-file level")
    # Show file name
    print("Name of im7 file:",iname)
    # Return
    return None

# Function to show image array settings
def SIRST(ncamr,pxlr,pxlc,imtype):
## Settings: Number of cameras
    # String of number of cameras
    sncamr = "Number of cameras in DIC:"
    # Append space before string
    sncamr = SDEMS(sncamr)
    # Show number of cameras
    print(sncamr,ncamr)
## Settings: Number of pixels
    # String of number of pixels
    spxl   = "Camera pixel resolution:"
    # Append space before string
    spxl   = SDEMS(spxl)
    # Show number of pixels
    print(spxl,pxlr,"x",pxlc)
## Settings: Image channel type
    # String of image type
    sityp  =  "Image channel type:"
    # Append space before string
    sityp  = SDEMS(sityp)
    # Image type
    print(sityp,imtype)
    # Return
    return None

# Function to merge double empty space before a string
def SDEMS(string):
    # Empty string
    empty = "  "
    # Modify string with empty space before string
    string = empty + string
    # Return
    return string

# Function to merge arrow before a string
def SAROW(string):
    # Arrow string
    arrow = "-> "
    # Modify string with arrow before string
    string = arrow + string
    # Return
    return string

# Function to confirm camera no. in use
def SCMRA(icamr):
    # Confirm camera number in use
    message = "Importing from camera no.:"
    # Include arrow in message
    message = SAROW(message)
    # Include empty space before message
    message = SDEMS(message)
    # Show message
    print(message,icamr)
    # Return
    return None

# Function to create image name from type and camera number
def SINAME(imname,imtype,icamr):
    # Image type as string
    sitype = str(imtype)
    # Camera number as string
    sicamr = str(icamr)
## Add type and camera number to image name
    # Add underscore to image name
    siname = SUSCR(imname)
    # Add image type
    siname = siname + sitype
    # Add underscore
    siname = SUSCR(siname)
    # Add camera number
    siname = siname + sicamr
    # Return
    return siname

# Function to confirm image saved
def SISAVE(siname):
    # Message to confirm image saved
    message = "New image saved as"
    # Include arrow in message
    message = SAROW(message)
    # Include empty space before message
    message = SDEMS(message)
    # Confirm image was saved
    print(message,siname)
    # Return
    return None

# Function to add underscore to string
def SUSCR(string):
    # Under score as string
    uscr = "_"
    # Add under score to string
    string = string + uscr
    # Return
    return string

