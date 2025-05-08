#!/usr/bin/env python

"""
CDDCV.py

Python module for converting DIC data for computer vision analysis.

Date: June 2024
Project: COLVIRM
License: MIT License

Acronym:
Convert_Dic_Data_Computer_Vision

Description:
    This module provides functions to convert and refine DIC (Digital Image Correlation) data
    to prepare it for computer vision processing tasks.

History:
    - Jun 2024: Initial version implemented by CAG.

Copyright:
    (C) CAG, KOKOA-ESPOL 2025
"""

import ReadIM
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

from rimcli.modcli import RDDCV, UDDCV


def CDMOD(clinpt):
    """
       Converts a DIC image using the mode specified by the command-line input.

       Parameters:
           clinpt (list): Command-line input arguments

       Returns:
           bool: True if an error occurred, False otherwise
       """

    rdmod = RDDCV.RDMOD(clinpt)
    lspmd = RDDCV.RMDTP.LIST
    imode, error = RDDCV.RMDXM(rdmod, lspmd)

    if not error:
        error = CRDCV(imode, rdmod, clinpt)

    return error


# Function to convert and refine images per detected mode
def CRDCV(imode, rdmod, clinpt):
    """
     Converts and refines a DIC image according to the specified mode.

     Parameters:
         imode (int): Detected input mode
         clinpt (list): Command-line input arguments

     Returns:
         bool: True if an error occurred, False otherwise
     """

    supported_modes = RDDCV.RMDTP.LIST
    default_mode = RDDCV.RMDXT(supported_modes)[2]
    error = False

    if imode == 0:
        error = CNORS(clinpt)
    elif imode == default_mode:
        # Default mode not implemented yet
        pass
    else:
        error = RDDCV.RINMD(rdmod)
    return error


def CNORS(clinpt):
    """
     Handles a single IM7 image with no refinement, using the CLI input.

     Parameters:
         clinpt (list): Command-line input arguments

     Returns:
         bool: True if file not found, False otherwise
     """

    iname, imname = UDDCV.FNMCL(clinpt)
    error = UDDCV.FNFND(iname)

    if not error:
        CIMLAY(iname, imname)
    return error


def CIMLAY(iname, imname):
    """
     Operates on an image once its existence has been confirmed.

     Parameters:
         iname (str): Full input file name
         imname (str): Base image name (without extension)
     """

    UDDCV.SIMLAY(iname)
    vrray = CIRRAY(iname)
    ncamr, _, _, imtype = CIRST(vrray)
    CIPNG(imname, imtype, ncamr, vrray)

    del vrray


# Function to extract image as array
def CIRRAY(iname):
    """
        Reads an IM7 image file into a NumPy array.

        Parameters:
            iname (str): Input file name

        Returns:
            np.ndarray: Image data as array
    """

    vbuff, vatts = ReadIM.extra.get_Buffer_andAttributeList(iname)
    vrray, _ = ReadIM.extra.buffer_as_array(vbuff)
    del vbuff, vatts
    return vrray


def CIRST(vrray):
    """
      Extracts and show image array settings.

      Parameters:
          vrray (np.ndarray): Image array

      Returns:
          tuple: (ncamr, pxlr, pxlc, imtype)
      """

    ncamr, pxlr, pxlc = np.shape(vrray)
    imtype = vrray.dtype
    UDDCV.SIRST(ncamr, pxlr, pxlc, imtype)
    return ncamr, pxlr, pxlc, imtype


def CIPNG(imname, imtype, ncamr, vrray):
    """
      Save each camera frame in the DIC image array as a PNG file.

      Parameters:
          imname (str): Base name for the output image files.
          imtype (dtype): Data type of the image array.
          ncamr (int): Number of camera images in the stack.
          vrray (np.ndarray): Image data array with shape (ncamr, H, W).
    """

    # Function aliases for readability
    show_camera = UDDCV.SCMRA
    build_filename = UDDCV.SINAME
    log_saved = UDDCV.SISAVE

    for icamr in range(ncamr):
        show_camera(icamr)
        fig = plt.figure()
        plt.imshow(vrray[icamr], cmap=cm.Greys_r)

        filename = build_filename(imname, imtype, icamr) + ".png"
        plt.savefig(
            filename,
            dpi="figure",
            format="png",
            facecolor="auto",
            edgecolor="auto",
        )
        log_saved(filename)
        plt.close(fig)

    plt.close("all")
