#!/usr/bin/env python

"""
rdimcv.py - Read a DIC image for computer vision analysis

Description:
    Read a set of Digital-Image-Correlation (DIC) images.
    Input is proprietary format im7, which gets converted
    to formats more suitable for Computer Vision.

Acronym:
    Read_Dic_IMage_Computer_Vision

Copyright:
    (C) CAG, KOKOA-ESPOL 2025

History:
    Name    Date    Description
    CAG     May24   Initial coding

License:
    This project is licensed under the terms of the MIT license.
"""


# Main function of rimcli
def rcmain():
    """
    Main function to read a DIC image for computer vision analysis
    Read a set of Digital-Image-Correlation (DIC) images.
    Input is proprietary format im7, which gets converted
    to another formats more suitable for Computer Vision
    """
    # Import modules
    # Import Read DIC Data function for Computer Vision
    from rimcli.modcli.RDDCV import RDCLI as read_command_line

    # Import Convert DIC Data function for Computer Vision
    from rimcli.modcli.CDDCV import CDMOD as convert_to_mode

    # Import show exit string function for DIC data
    from rimcli.modcli.UDDCV import SEXIT as show_exit_message

    # Extract input data
    # Extract interpreter and command line input
    has_error, command_line_input = read_command_line()
    # Convert DIC images
    # Convert to CLI-based mode
    if not has_error:
        has_error = convert_to_mode(command_line_input)
    # Terminate run
    # String on exit
    show_exit_message(has_error, command_line_input)


# Main method for rdimcv
if __name__ == "__main__":
    # Execute main function
    rcmain()
