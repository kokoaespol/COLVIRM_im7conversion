---
title: 'RIMCLI: A Python tool for conversion of Digital Image Correlation images using the terminal'
tags:
  - Python
  - Digital image correlation
  - Image conversion
  - Experimental mechanics
  - Solids and Fluids
authors:
  - name: Carlos Xavier Azua-Gonzalez
    orcid: 0000-0002-4433-5182
    affiliation: 1
affiliations:
 - name: School of Engineering, Cardiff University
   index: 1
date: 23 March 2025
---
[//]: # (bibliography: paper.bib)
# Summary
Digital Image Correlation (DIC) and stereoscopic imaging are used for tracing deformation fields non-intrusively in a reconstructed 3D scene, which may involve either solids and/or fluids. Such techniques are exploited to extract associated vector/tensor fields (velocity, strain components) of importance to reveal the mechanics governing a bespoke phenomenon replicated under controlled lab conditions, e.g. to investigate the stream lines in fluids (flow through a scaled earth-filled dam, aerodynamics, combustion, and oceanography), or to detect growing defects in solids due to exposure to extreme stimuli of impact/temperature/moisture/ageing (cracks in weakened construction materials, the failure of a building foundation due to exceeding the capacity of the soil beneath, to geologic earthquake-induced fault rupture replicated at lab scale).
For this purpose, a popular DIC camera and proprietary hardware/software manufacturer, Digital image Acquisition and Visualisation (DaVis) LaVision, developed the im7 image format. Such image acquisiton equipment is now used worldwide in experimental mechanics labs. Historically, this implied that DaVis LaVision image datasets were initially analysed through proprietary software by the researchers, a.k.a. in a blackbox mode. Eventually, LaVision released openly low-level software libraries written in C++ to provide more transparent access to image data and enable new applications of such data underpinned by image processing software developed by the researchers. 
A powerful low-level python package, ReadIM, was originally developed by Alan Fleming (https://pypi.org/project/ReadIM/), which interfaces the low-level C++ code to extract im7 images as Numpy arrays. In addition, a first trial of a higher-level ReadIM library ("IM", https://bitbucket.org/fleming79/im/src/master/) was coded, which still required some level of understanding of the storage of DIC images and was unable to be installed directly from the PyPI repository.
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
| Name |   Year |  Description                                         |
|:---  |:---    |:---                                                  |
|CAG   |Mar25   |Transferred ownership to KOKOA-ESPOL. Not in PYPI yet |
