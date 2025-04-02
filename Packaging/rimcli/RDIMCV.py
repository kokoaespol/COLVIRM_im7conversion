#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Copyright (C) COLVIRM project 2024
# This project is licensed under the terms of the MIT license.
#*PYTHON PROGRAM
# RDIMCV.py
#*PURPOSE
# Read a DIC image for computer vision analysis
#*ACRONYM
# Read_Dic_IMage_Computer_Vision
#*DESCRIPTION
# Read a set of Digital-Image-Correlation (DIC) images.
# Input is proprietary format im7, which gets converted
# to another formats more suitable for Computer Vision
#*HISTORY
# NAME DATE   DESCRIPTION
# CAG  May24  Initial coding

# Main function
def rcmain():
## Import modules
    # Import Read Dic Data for Computer Vision
    from rimcli import RDDCV
    # Import Convert Dic Data for Computer Vision
    from rimcli import CDDCV
    # Import utilities for DIC data
    from rimcli import UDDCV
## Rename module-mapped functions 
    # Function to read commmand line data
    RDCLI = RDDCV.RDCLI
    # Function to convert Dic image to given mode
    CDMOD = CDDCV.CDMOD
    # Function to show exit string
    SEXIT = UDDCV.SEXIT
## Extract input data
    # Extract interpreter and command line input
    error,clinpt = RDCLI()
## Convert DIC images
    # Convert to CLI-based mode
    if not error: error = CDMOD(clinpt)
## Terminate run
    # String on exit
    SEXIT(error,clinpt)

# Main method
if __name__ == '__main__':
    # Execute main function
    rcmain()

