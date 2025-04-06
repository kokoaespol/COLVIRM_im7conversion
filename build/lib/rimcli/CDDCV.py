#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Copyright (C) COLVIRM project 2024
# This project is licensed under the terms of the MIT license.
#*PYTHON MODULE
# CDDCV.py
#*PURPOSE
# Convert DIC data for computer vision analysis
#*ACRONYM
# Convert_Dic_Data_Computer_Vision
#*DESCRIPTION
# Functions to convert and refine DIC data for
# Computer Vision
#*HISTORY
# NAME DATE   DESCRIPTION
# CAG  Jun24  Initial coding

# Function to convert Dic image to given mode
def CDMOD(clinpt):
## Import modules
    # Import Read Dic Data for Computer Vision
    from rimcli import RDDCV
## Rename read mode functions and classes
    # Extract command-line reading mode
    RDMOD = RDDCV.RDMOD
    # Class of supported modes
    RMDTP = RDDCV.RMDTP
    # Extract starting message of modes
    RMDXM = RDDCV.RMDXM
    # List of supported modes
    LIST  = RMDTP.LIST
## Initialise error flag
    error = False
## DIC image reading modes    
    # Read mode
    rdmod = RDMOD(clinpt)
    # Extract list of supported modes
    lspmd = LIST
    # Detect mode number
    imode,error = RMDXM(rdmod,lspmd)
## Operate on image using detected mode
    if not error: error = CRDCV(imode,clinpt)
    # Return
    return error

# Function to convert and refine images per detected mode
def CRDCV(imode,clinpt):
## Import modules
    # Import Read Dic Data for Computer Vision
    from rimcli import RDDCV
    # Import Utilities for Computer Vision
    from rimcli import UDDCV
## Rename module-mapped functions and classes
    # Class of supported modes
    RMDTP = RDDCV.RMDTP
    # Declare invalid mode
    RINMD = RDDCV.RINMD
    # Extract individual string of modes
    RMDXT = RDDCV.RMDXT
    # List of supported modes
    LIST  = RMDTP.LIST
## Initialise error flag
    error = False
## Load supported modes
    # Extract list of supported modes
    lspmd = LIST
    # Length of supported mode list
    smode,dmode,dmodp = RMDXT(lspmd)
    # Single-file: mode 0
    if imode == 0:
        # Convert single im7, no refinement, name from cli
        error = CNORS(clinpt)
    # Default image reading mode
    elif imode == dmodp:
        # Not implemented yet, use as "--single-im7"
        pass
    # Invalid mode passed through
    else:
        # Switch on flag for invalid mode
        error = RINMD(rdmod)
    # Return    
    return error

# Function to operate on single im7 image, no refinement
def CNORS(clinpt):
## Import modules
    # Import Utilities for Computer Vision
    from rimcli import UDDCV
## Rename module-mapped functions and classes
    # Extract file name from cli
    FNMCL = UDDCV.FNMCL
    # Detect if file not found
    FNFND = UDDCV.FNFND
## Extract file name, if existing
    # File name (with & without format)
    iname,imname = FNMCL(clinpt)
    # Switch on error if file not found
    error = FNFND(iname)
    # Operate at image lay
    if not error: CIMLAY(iname,imname)
    # Return
    return error

# Function to operate once file confirmed to exist
def CIMLAY(iname,imname):
## Import modules
    # Import Utilities for Computer Vision
    from rimcli import UDDCV
## Rename module-mapped functions
    # Confirm image level entered
    SIMLAY = UDDCV.SIMLAY
## Enter image level
    # Confirm im7 image level entered
    SIMLAY(iname)
    # Import im7 image as (python) array
    vrray = CIRRAY(iname)
    # Extract image array settings
    ncamr,pxlr,pxlc,imtype = CIRST(vrray)
    # Extracted image array into png image
    CIPNG(imname,imtype,ncamr,vrray)
    # Delete image array
    del(vrray)
    # Return
    return None

# Function to extract image as array
def CIRRAY(iname):
## Import modules
    # Read im7 image to array
    import ReadIM
## Rename module-mapped functions
    # Read image with extra output
    READX = ReadIM.extra
    # Read image buffer and attributes
    RBFAT = READX.get_Buffer_andAttributeList
    # Read image buffer as array
    RBFAR = READX.buffer_as_array
## Extract image attributes and buffer as array
    # Extract image attributes and buffer
    vbuff, vatts = RBFAT(iname)
    # Convert image buffer into python array
    vrray, vbuff = RBFAR(vbuff)
    # Remove unused image attributes and buffer
    del(vbuff,vatts)
    # Return
    return vrray

# Function to show image array settings
def CIRST(vrray):
## Import modules
    # Import Utilities for Computer Vision
    from rimcli import UDDCV
    # Scientific package of python
    import numpy as np
## Rename module-mapped functions
    # Extract image array settings
    SIRST = UDDCV.SIRST
    # Extract shape of python array
    SHAPE = np.shape
## Extract image characteristics
    # Image camera and pixel numbers
    ncamr , pxlr , pxlc = SHAPE(vrray)
    # Image-channel(s) data type
    imtype = vrray.dtype
    # Report image characteristics
    SIRST(ncamr,pxlr,pxlc,imtype)
    # Return
    return ncamr,pxlr,pxlc,imtype

# Function to save image array as png
def CIPNG(imname,imtype,ncamr,vrray):
## Import modules
    # Utilities for DIC image and computer vision
    from rimcli import UDDCV 
    # Plotting module
    import matplotlib.pyplot as plt
    # Colour map
    import matplotlib.cm as cm
## Rename module-mapped functions and classes
    # String to confirm camera in use
    SCMRA  = UDDCV.SCMRA
    # Image name with type and camera number
    SINAME = UDDCV.SINAME
    # String to confirm image saved
    SISAVE = UDDCV.SISAVE
    # Open new figure
    FIGURE = plt.figure
    # Close figure
    CLOSE  = plt.close
    # Show image in current figure
    IMSHOW = plt.imshow
    # Save current figure
    SAVEFG = plt.savefig
    # Colour map: Greys red
    GREYSR = cm.Greys_r
## Save image in another format
    # List of camera IDs
    lcamr = range(0,ncamr)
    # Loop over cameras
    for icamr in lcamr:
        # Show camera no. in use
        SCMRA(icamr)
        # Create new figure
        fig = FIGURE()
        # Current camera image as array
        ivrray = vrray[icamr]
        # Show image array in current figure
        IMSHOW(ivrray,cmap = GREYSR)
        # Image name
        siname = SINAME(imname,imtype,icamr)
        # Save figure as png
        SAVEFG(siname+'.png',
               # Dots per inch
               dpi='figure',
               # Image format
               format='png',
               # Face colour
               facecolor='auto',
               # Edge colour
               edgecolor='auto')
        # Show saved figure name
        SISAVE(siname)
        # Close figure
        CLOSE()
    # Section to refine image
    # tbc.....
    # End of Section to refine image
    # Close all figures
    CLOSE('all')
    # Return
    return None

