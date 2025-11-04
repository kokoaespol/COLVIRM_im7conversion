#!/usr/bin/env python

"""
dic_cv_converter.py

Python module for converting DIC data for computer vision analysis.

Date: June 2024
Project: COLVIRM
License: MIT License

Description:
    This module provides functions to convert and refine DIC (Digital Image Correlation) data
    to prepare it for computer vision processing tasks.

History:
    - Jun 2024: Initial version implemented by CAG.
    - Nov 2024: Refactored function and variable names for improved readability.

Copyright:
    (C) CAG, KOKOA-ESPOL 2025
"""

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import ReadIM

from rimcli.modcli import rddcv, uddcv


def convert_to_mode(command_input_arguments):
    """
    Converts a DIC image using the mode specified by the command-line input.

    Parameters:
        command_input_arguments (list): Command-line input arguments

    Returns:
        bool: True if an error occurred, False otherwise
    """

    conversion_mode = rddcv.RDMOD(command_input_arguments)
    available_modes = rddcv.RMDTP.IMAGE_READING_MODE_TYPES
    mode_index, error = rddcv.RMDXM(conversion_mode, available_modes)

    if not error:
        error = convert_and_refine(mode_index, conversion_mode, command_input_arguments)

    return error


def convert_and_refine(mode_index, conversion_mode, command_input_arguments):
    """
    Converts and refines a DIC image according to the specified mode.

    Parameters:
        mode_index (int): Index of the conversion mode in the supported modes list
        conversion_mode: Mode for image conversion
        command_input_arguments (list): Command-line input arguments

    Returns:
        bool: True if an error occurred, False otherwise
    """

    supported_modes = rddcv.RMDTP.IMAGE_READING_MODE_TYPES
    roi_mode_index = rddcv.RMDXT(supported_modes)[1]
    error = False

    if mode_index == 0:
        error = convert_without_refinement(command_input_arguments, mode_index)
    elif mode_index == roi_mode_index:
        # ROI mode: ROI coordinates are transferred
        # but behaves like convert_without_refinement (i.e. no refinement)
        error = convert_with_refinement_roi(command_input_arguments)
    else:
        error = rddcv.RINMD(conversion_mode)

    return error


def convert_without_refinement(command_input_arguments, mode_index):
    """
    Handles a single IM7 image with no refinement, using the CLI input.

    Parameters:
        command_input_arguments (list): Command-line input arguments
        mode_index (int): Index of the conversion mode

    Returns:
        bool: True if file not found, False otherwise
    """

    full_image_filename, base_image_filename = uddcv.FNMCL(command_input_arguments)
    error = uddcv.FNFND(full_image_filename)

    if not error:
        process_image_conversion(full_image_filename, base_image_filename, mode_index)
    return error


def convert_with_refinement_roi(command_input_arguments):
    """
    Handles a single IM7 image with refinement, using the CLI input.
    Position of the ROI coordinates is assumed as
    X1 coordinate in command_input_arguments[3] and X2 coordinate in command_input_arguments[4].
    Y1 coordinate in command_input_arguments[5] and Y2 coordinate in command_input_arguments[6].

    Parameters:
        command_input_arguments (list): Command-line input arguments

    Returns:
        bool: True if file not found, False otherwise
    """
    MINIMUM_CLI_ARGUMENTS_FOR_ROI = 7
    full_image_filename, base_image_filename = uddcv.FNMCL(command_input_arguments)
    error = uddcv.FNFND(full_image_filename)

    if not error:
        error = len(command_input_arguments) < MINIMUM_CLI_ARGUMENTS_FOR_ROI
        if not error:
            roi_x1, roi_x2, roi_y1, roi_y2 = uddcv.XTROI(command_input_arguments)
            roi_image_conversion(
                full_image_filename, base_image_filename, roi_x1, roi_x2, roi_y1, roi_y2
            )
        else:
            print("Insufficient command-line inputs for ROI coordinates")
    return error


def process_image_conversion(full_image_filename, base_image_filename, mode_index):
    """
    Operates on an image once its existence has been confirmed.

    Parameters:
        full_image_filename (str): Full input file name
        base_image_filename (str): Base image name (without extension)
        mode_index (int): Index of the conversion mode
    """

    uddcv.SIMLAY(full_image_filename)
    image_array = read_image_to_array(full_image_filename)
    number_of_cameras, _, _, image_type = extract_array_settings(image_array)
    save_camera_frames_single_mode(base_image_filename, mode_index, image_type, number_of_cameras, image_array)

    del image_array


def roi_image_conversion(full_image_namefile, base_image_filename, ROI_x1, ROI_x2, ROI_y1, ROI_y2):
    """
    Operates on an image once its existence has been confirmed.
    Assumes the image will require ROI generation or other refinements.

    Parameters:
        full_image_namefile (str): Full input file name
        base_image_filename (str): Base image name (without extension)
        ROI_x1 (int): X1 coordinate for the region of interest
        ROI_x2 (int): X2 coordinate for the region of interest
        ROI_y1 (int): Y1 coordinate for the region of interest
        ROI_y2 (int): Y2 coordinate for the region of interest
    """

    uddcv.SIMLAY(full_image_namefile)
    image_data_array = read_image_to_array(full_image_namefile)
    number_of_cameras, _, _, image_data_type = extract_array_settings(image_data_array)
    save_camera_frames_roi_mode(base_image_filename, image_data_type, number_of_cameras, image_data_array, ROI_x1, ROI_x2, ROI_y1, ROI_y2)

    del image_data_array


# Function to extract image as array
def read_image_to_array(full_image_namefile):
    """
    Reads an IM7 image file into a NumPy array.

    Parameters:
        full_image_namefile (str): Input file name

    Returns:
        np.ndarray: Image data as array
    """

    vbuff, vatts = ReadIM.extra.get_Buffer_andAttributeList(full_image_namefile)
    image_data_array, _ = ReadIM.extra.buffer_as_array(vbuff)
    del vbuff, vatts
    return image_data_array


def extract_array_settings(image_data_array):
    """
    Extracts and show image array settings.

    Parameters:
        image_data_array (np.ndarray): Image array

    Returns:
        tuple: (number_of_cameras, pxlr, pxlc, image_data_type)
    """

    number_of_cameras, pxlr, pxlc = np.shape(image_data_array)
    image_data_type = image_data_array.dtype
    uddcv.SIRST(number_of_cameras, pxlr, pxlc, image_data_type)
    return number_of_cameras, pxlr, pxlc, image_data_type


def save_camera_frames_single_mode(base_image_file_name, imode, image_data_type, number_of_cameras, vrray):
    """
    Save each camera frame in the DIC image array as a PNG file.

    Parameters:
        base_image_file_name (str): Base name for the output image files.
        image_data_type (dtype): Data type of the image array.
        number_of_cameras (int): Number of camera images in the stack.
        vrray (np.ndarray): Image data array with shape (ncamr, H, W).
    """

    supported_modes = rddcv.RMDTP.IMAGE_READING_MODE_TYPES
    default_mode = rddcv.RMDXT(supported_modes)[2]

    # Function aliases for readability
    show_camera = uddcv.SCMRA
    build_filename = uddcv.SINAME
    log_saved = uddcv.SISAVE

    for icamr in range(number_of_cameras):
        show_camera(icamr)
        fig = plt.figure()

        plt.imshow(vrray[icamr], cmap=cm.Greys_r)

        filename = build_filename(base_image_file_name, image_data_type, icamr) + ".png"
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


def save_camera_frames_roi_mode(base_image_filename, image_daya_type, number_of_cameras, image_data_array, ROI_x1, ROI_x2, ROI_y1, ROI_y2):
    """
    Save each camera frame in the DIC image array as a PNG file.
    Allow for ROI generation or other refinements in the future.

    Parameters:
        base_image_file_name (str): Base name for the output image files.
        image_data_type (dtype): Data type of the image array.
        number_of_cameras (int): Number of camera images in the stack.
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

    for icamr in range(number_of_cameras):
        show_camera(icamr)
        fig = plt.figure()

        roi_image = image_data_array[icamr][ROI_x1:ROI_x2, ROI_y1:ROI_y2]
        plt.imshow(roi_image, cmap=cm.Greys_r)

        filename = build_filename(base_image_filename, image_daya_type, icamr) + ".png"
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
