#!/usr/bin/env python

"""
cddcv.py

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

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import ReadIM

from rimcli.modcli import rddcv, uddcv


def CDMOD(clinpt):
    """
    Converts a DIC image using the mode specified by the command-line input.

    Parameters:
        clinpt (list): Command-line input arguments

    Returns:
        bool: True if an error occurred, False otherwise
    """

    rdmod = rddcv.RDMOD(clinpt)
    lspmd = rddcv.RMDTP.IMAGE_READING_MODE_TYPES
    imode, error = rddcv.RMDXM(rdmod, lspmd)

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

    supported_modes = rddcv.RMDTP.IMAGE_READING_MODE_TYPES
    roi_mode = rddcv.RMDXT(supported_modes)[1]
    error = False

    if imode == 0:
        error = CNORS(clinpt, imode)
    elif imode == roi_mode:
        # ROI mode: ROI coordinates are transferred
        # but behaves like CNORS (i.e. no refinement)
        error = CRFSIM(clinpt)
    else:
        error = rddcv.RINMD(rdmod)
    return error


def CNORS(clinpt, imode):
    """
    Handles a single IM7 image with no refinement, using the CLI input.

    Parameters:
        clinpt (list): Command-line input arguments

    Returns:
        bool: True if file not found, False otherwise
    """

    iname, imname = uddcv.FNMCL(clinpt)
    error = uddcv.FNFND(iname)

    if not error:
        CIMLAY(iname, imname, imode)
    return error


def CRFSIM(clinpt):
    """
    Handles a single IM7 image with refinement, using the CLI input.
    Position of the ROI coordinates is assumed as
    X1 coordinate in clinpt[3] and X2 coordinate in clinpt[4].
    Y1 coordinate in clinpt[5] and Y2 coordinate in clinpt[6].

    Parameters:
        clinpt (list): Command-line input arguments

    Returns:
        bool: True if file not found, False otherwise
    """
    mncli_ROI = 7
    iname, imname = uddcv.FNMCL(clinpt)
    error = uddcv.FNFND(iname)
    if not error:
        error = len(clinpt) < mncli_ROI
        if not error:
            ROI_x1, ROI_x2, ROI_y1, ROI_y2 = uddcv.XTROI(clinpt)
            CIRLAY(iname, imname, ROI_x1, ROI_x2, ROI_y1, ROI_y2)
        else:
            print("Insufficient command-line inputs for ROI coordinates")
    return error


def CIMLAY(iname, imname, imode):
    """
    Operates on an image once its existence has been confirmed.

    Parameters:
        iname (str): Full input file name
        imname (str): Base image name (without extension)
    """

    uddcv.SIMLAY(iname)
    vrray = CIRRAY(iname)
    ncamr, _, _, imtype = CIRST(vrray)
    CIPNG(imname, imode, imtype, ncamr, vrray)

    del vrray


def CIRLAY(iname, imname, ROI_x1, ROI_x2, ROI_y1, ROI_y2):
    """
    Operates on an image once its existence has been confirmed.
    Assumes the image will require ROI generation or other refinements.

    Parameters:
        iname (str): Full input file name
        imname (str): Base image name (without extension)
        ROI_x1 (int): X1 coordinate for the region of interest
        ROI_x2 (int): X2 coordinate for the region of interest
        ROI_y1 (int): Y1 coordinate for the region of interest
        ROI_y2 (int): Y2 coordinate for the region of interest
    """

    uddcv.SIMLAY(iname)
    vrray = CIRRAY(iname)
    ncamr, _, _, imtype = CIRST(vrray)
    CIRPNG(imname, imtype, ncamr, vrray, ROI_x1, ROI_x2, ROI_y1, ROI_y2)

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
    uddcv.SIRST(ncamr, pxlr, pxlc, imtype)
    return ncamr, pxlr, pxlc, imtype


def CIPNG(imname, imode, imtype, ncamr, vrray):
    """
    Save each camera frame in the DIC image array as a PNG file.

    Parameters:
        imname (str): Base name for the output image files.
        imtype (dtype): Data type of the image array.
        ncamr (int): Number of camera images in the stack.
        vrray (np.ndarray): Image data array with shape (ncamr, H, W).
    """

    supported_modes = rddcv.RMDTP.IMAGE_READING_MODE_TYPES
    default_mode = rddcv.RMDXT(supported_modes)[2]

    # Function aliases for readability
    show_camera = uddcv.SCMRA
    build_filename = uddcv.SINAME
    log_saved = uddcv.SISAVE

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


def CIRPNG(imname, imtype, ncamr, vrray, ROI_x1, ROI_x2, ROI_y1, ROI_y2):
    """
    Save each camera frame in the DIC image array as a PNG file.
    Allow for ROI generation or other refinements in the future.

    Parameters:
        imname (str): Base name for the output image files.
        imtype (dtype): Data type of the image array.
        ncamr (int): Number of camera images in the stack.
        vrray (np.ndarray): Image data array with shape (ncamr, H, W).
        ROI_x1 (int): X1 coordinate for the region of interest.
        ROI_x2 (int): X2 coordinate for the region of interest.
        ROI_y1 (int): Y1 coordinate for the region of interest.
        ROI_y2 (int): Y2 coordinate for the region of interest.
    """

    # Function aliases for readability
    show_camera = uddcv.SCMRA
    build_filename = uddcv.SINAME
    log_saved = uddcv.SISAVE

    for icamr in range(ncamr):
        show_camera(icamr)
        fig = plt.figure()

        roi_image = vrray[icamr][ROI_x1:ROI_x2, ROI_y1:ROI_y2]
        plt.imshow(roi_image, cmap=cm.Greys_r)

        filename = build_filename(imname, imtype, icamr) + ".png"
        # Generate ROI or other refinements here if needed
        # For now, just save the image
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
