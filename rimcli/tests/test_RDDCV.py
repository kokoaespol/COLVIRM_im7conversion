import pytest


def test_RDDCV_RDCLI_should_pass_correct_number_arguments_():

    # Import the function to be tested
    from rimcli.modcli.rddcv import RDCLI

    # Mock the command line arguments
    import sys
    from unittest.mock import patch

    with patch.object(sys, "argv", ["script_name", "arg1", "arg2"]):
        # Call the function
        error, clinpt = RDCLI()

        # Check that the error is False
        assert not error

        # Check that clinpt has the expected number of arguments
        assert len(clinpt) == 3  # script_name + arg1 + arg2


def test_RDDCV_RDCLI_should_fail_with_insufficient_arguments():
    # Import the function to be tested
    from rimcli.modcli.rddcv import RDCLI

    # Mock the command line arguments
    import sys
    from unittest.mock import patch

    with patch.object(sys, "argv", ["script_name", "arg1"]):
        # Call the function
        error, clinpt = RDCLI()

        # Check that the error is True
        assert error

        # Check that clinpt has the expected number of arguments
        assert len(clinpt) == 2  # script_name + arg1
