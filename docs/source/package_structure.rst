Package structure and Coding standard
=====================================

Basic package structure
-----------------------

The structure of the package is as follows:

.. code-block:: bash

    rimcli/
    ├── __init__.py
    ├── read_dic_image_CV.py
    │   ├── def RCMAIN():
    │   └── ...
    ├── tests/
    │   ├── __init__.py
    │   ├── data/
    │   │   ├── __init__.py
    │   │   ├── datlnk.py
    │   │   └── *.im7 
    │   ├── devenv/
    │   │   ├── __init__.py
    │   │   └── *.yml 
    │   ├── e01m*.py
    │   └── test_RDDCV.py
    │   
    └── modcli/
        ├── __init__.py
        ├── rddcv.py
        │   ├── def RDCLI():
        │   └── ...
        ├── cdic_cv_converterddcv.py
        │   ├── def convert_to_mode(clinpt):
        │   └── ...
        └── uddcv.py
            ├── def SEXIT(error,clinpt):
            └── ...

Coding standard
---------------

The Python Enhancement Proposal (PEP) by Guido Van Rossum et al. should be used as a slack guideline. In addition, purpose specific guidelines have been proposed with the sole intention to preserve internal consistency across the rimcli code. These guidelines are as follows:

* **License:** start each new module with a line that refers to the MIT license by which the ``rimcli`` code was originally developed for, but update the date if it is not yet in its final state (as per history chapter as described later in the guidelines).

  .. code-block:: python
      
      # Copyright (C) CAG, KOKOA-ESPOL 2025
      # This project is licensed under the terms of the MIT license.
  
* **Variable/function/class/module/(sub-)package names:** Generally, the use of up to six alphanumeric characters in ``lowercase`` style is preferred for names. The use of ``lower_case_with_underscores`` style is admitted when this enhances readability. The name could often be an acronym, which should self-describe the use of the variable or function if read together with the preceding comment. However, package and sub-package module names should be short, and should try to adhere to six characters as much as possible (e.g. ``modcli.py`` is advised, whereas ``modcli_subpackage.py`` is discouraged).

  * The reasoning behind short module and variable names (whenever possible) is that, by experience of developing long codes with various contributors, the longer the names the easier to introduce bugs (especially in modules with repetitive and similar tasks).

* **Purpose and acronym:** include a brief description of the purpose of each module, typically within a single line, followed by an acronym as a comment as shown below:

  .. code-block:: python
      
      # Python program
      # rdimcv.py
      # Purpose
      # Read a DIC image for computer vision analysis
      # Acronym
      # Read_Dic_IMage_Computer_Vision
      
  * This is to be added aside from standard descriptions included as documentation strings for functions and classes, which are then automatically updated by ``sphinx``.
  
* **Description:** A succinct description of the operation of the module that expands on the purpose of the module as shown in the example below:
  
  .. code-block:: python
  
     # Description
     # Read a set of Digital-Image-Correlation (DIC) images.
     # Input is proprietary format im7, which gets converted
     # to another formats more suitable for Computer Vision
   
* **History:** Update the history of the core and main modules for every substantial contribution, e.g.

  .. code-block:: python
  
      # History
      # Name Date   Description
      # CAG  May24  Initial coding
      
* **Comments:** aim for a succinct comment per each line of code as much as possible. See two examples of code below. The first code example is inadmissible because there is one line for a number of operations; whereas the second code example, with a descriptive comment per each line of code, complies with the coding standard. Adding comments for the obvious is rather unnecessary, and discouraged. However, experience tells that there are always alternatives ways to include a meaningful comment per each code line in a creative and informative way, rather than filling in spaces with the obvious. 

  .. code-block:: python

      # This is code for importing python packages
      import <package_1>
      import <package_1>
    
  .. code-block:: python

      # Importing python <package_1> for operation 1
      import <package_1>
      # Importing python <package_2> for operation 2
      import <package_2>
   
   
  * Comments should be placed above the code they refer to and respect indentation
  * Avoid lengthy comments that exceed 3 lines of code. Clarifications can be included either in the description of a module or in history chapter, or as part of the documentation strings, if required.
  * In-line comments are admissible, as long as they do not create confusion with the logic of the code. Notes for further development may be included in the documentation strings.
