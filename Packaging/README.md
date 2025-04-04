---
Title: 'RIMCLI: A Python tool for image format conversion of Digital Image Correlation using the command-line'

Tags:
  - Python
  - Digital image correlation
  - Image format conversion
  - Experimental mechanics
  - Solid and Fluids mechanics
  
Authors:
|Name                           |Identifier/email                                          |
|:---                           |:---                                                      |
|Carlos Xavier Azua-Gonzalez \+ |orcid: 0000-0002-4433-5182, Azua-GonzalezCX@cardiff.ac.uk |
|Alan Fleming                   |alanf@amc.edu.au                                          |

Maintainers:
  - KOKOA-ESPOL \*
    
Affiliations:
 - \+ School of Engineering, Cardiff University, United Kingdom
 - \* Escuela Superior Politecnica del Litoral (ESPOL), Guayaquil, Ecuador
   
Date: 23 March 2025

---
[//]: # (bibliography: paper.bib)
# Summary
Digital Image Correlation (DIC) and stereoscopic imaging are used for tracing deformation fields non-intrusively in a reconstructed 3D scene. This scene may involve problems pertaining to either solids and/or fluids. Examples of applications include the investigation of the mechanical response of fluids (flow in porous media, fluid & gas dynamics, ocean engineering), and the mechanical behaviour of materials and structures (e.g. fracture mechanics, detection and monitoring of cracks and shear bands in quasi-brittle materials). A problem of interest is typically replicated in instrumented tests under controlled lab conditions, induced by initial and boundary conditions, to collect rich and extensive sensor and image data. 
DIC techniques are exploited to extract associated vector/tensor fields (such as velocity and strain components). An accurate quantification of these physical quantities is of critical importance to reveal the underlying mechanics of the problem of interest. The quality of such DIC analyses is intimately related to the ever increasing high-resolution of images, typical of bespoke lab-based hardware and cameras.
For this purpose, a popular DIC camera and proprietary hardware/software manufacturer, the Digital image Acquisition and Visualisation (DaVis) LaVision corporation, developed the im7/vc7 image formats. Such image acquisiton equipment are now used worldwide in experimental mechanics labs, among other minor research-based setups which do acquire images in standard formats. Historically, this implied that users of the DaVis LaVision hardware were deprived from getting access to image datasets, forcing their post-processing to be limited to the proprietary software. Eventually, LaVision released openly low-level C++ software libraries to provide more transparent access to im7/vc7 image data. This enables an unprecedented opportunity to use emerging data science and Artificial Intelligence (AI) packages for data processing in DIC experimental campaigns that are underpinned by high resolution im7/vc7 images. 
In this realm, a powerful low-level python package, ReadIM, was originally developed by Alan Fleming (https://pypi.org/project/ReadIM/), which interfaces the low-level C++ code by Lavision to extract im7/vc7 images as Numpy arrays. In addition, a first trial of a higher-level ReadIM library ("IM", https://bitbucket.org/fleming79/im/src/master/) was coded, though this was unaccessible by the standard python package index (PyPI) repository.
# Statement of need
The novelty of this high-level repository lies in unlocking the non-expert use of im7 files in a format (e.g. png) suitable for streaming into Computer Vision (CV) and Artificial Intelligence (AI) pipelines. This is done through a single command line (CLI) operation, and therefore, suitable for integration into High Performance Computing (HPC) jobs that handle large numbers of non-interactive commands and tasks. In particular, high resolution im7 images are excellent candidates to fine-tune popular CV models using transfer learning. The user needs not to worry in understanding the complex settings of stereoscopic image acquisition and storage, nor the theoretical foundations of DIC. The user retrieves 2D images corresponding to each field of view (FOV). Useful information of the setting, such as number of syncronised acquisition channels and image resolution are also output. Each image is then suitable for streaming into AI pipelines. 
## Envisaged use of the RIMCLI by experimental (solid/fluid) mechanics researchers
CV models and associated (AI) pipelines are usually developed by computer experts/scientists, who may not be fully familiar with the physics principles behind DIC. 
It is envisioned that providing computer scientists with a fast-track tool to get the *raw input image* for AI labelling/training or inference would accelerate the pace at which new AI-driven techniques are developed to complement conventional DIC.
# Overview of RIMCLI
The libraries are built on top of the powerful ReadIM python package. The original ReadIM package by Alan Fleming, which interfaces C++ code for the low-level access of the im7 image format as Numpy arrays, has been recently repotentiated to secure cross platform access and provided with substantial incremental development to include further examples, automated testing and migrated to a new site to reactivate maintenance by the authors of this paper.
## Research making use of the libraries: COLVIRM_im7conversion
The COLVIRM project at Cardiff University (United Kingdom), Escuela Superior Politecnica del Litoral (ESPOL-Ecuador) and Universidad de la Rioja (UNIR-Spain) made use of the initial versions of the RIMCLI repository to convert im7 images into other common formats for AI analysis of crack propagation in historical mortars. The repository makes extensive use of the python package ReadIM, developed originally by Alan Fleming  and now being migrated to a new repository by the authors of this paper to repotentiate maintenance and visibility of the libraries. Historical usage of the original ReadIM package by other researchers is also reported in the personal webpage of Charles Jekel (https://jekel.me/2015/Open-and-View-IM7-Files-with-Python/)

## Key features
* **im7 image CLI-handling:**
  * **Single im7 image call:** Included in this original CLI-version
  * **Multiple im7 image call:** To be extended
* **Cross platform automated-testing:** Testing scripts should be created to test successful installation in Linux/Windows OS. 
* **Extended examples including HPC usage:** The original CLI-version has been already tested in an HPC environment
* **Database of subsets of im7 images:** Subset of images of recent research projects, which do not compromise the confidentiality of ongoing research will be made available

## Applications and limitations
The CLI-version of ReadIM has been extensively used for im7 image conversion, to accelerate integration of DIC images into AI pipelines, with especial interest in making it easy to use in an HPC environment by a single command line operation. Although the base version of the libraries, ReadIM, was of generic usage for im7 and vc7 image conversion, it is still a matter of future work to extend the CLI capabilities towards vc7 images.

## Real World example
To be completed

## Acknowledgement
The access to the Super Computing Wales project's facilities (Hawk supercomputing nodes) through the project SWC 2233 at Cardiff University is greatly acknowledged. The encouragement and initial communications by Dr Alan Fleming, the original maintainer and developer of the ReadIM libraries, are greatly acknowledged. The enthusiastic involvement of the Open Source Software Student Chapter at Escuela Superior Politecnica del Litoral (Comunidad de Codigo Abierto, KOKOA-ESPOL, Ecuador) is thankfully recognised. The following developers at KOKOA-ESPOL contributed with either coding and/or testing: <developer 1>, <developer 2>.
## History
| Name |   Year |  Description                                                                                    |
|:---  |:---    |:---                                                                                             |
|CAG   |Mar24   |Initial coding                                                                                   |
|CAG   |Jun24   |Initiated Github repository for version control                                                  |
|CAG   |Mar25   |Transferred ownership of the initial github repository of RIMCLI to KOKOA-ESPOL. Not in PYPI yet |
