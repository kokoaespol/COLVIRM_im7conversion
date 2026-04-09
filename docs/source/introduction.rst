Introduction
============

Summary
-------
Digital Image Correlation (DIC), and stereoscopic imaging, are conventionally used as non-invasive techniques that trace deformation fields. The stereoscopic technique aims at reconstructing the 3D scene from 2D views, whereas DIC traces patterns to update the displacement vector at sampling locations. Another popular experimental technique is the Particle Image Velocimetry (PIV), which aims to trace velocity fields in fluids that possess tracer particles. The techniques are commonly used to study mechanics problems with applications in solids and/or fluids, and some researchers have tried to combine both techniques to study problems at the interface of a solid-fluid system. Examples of applications in fluid mechanics range from flow in porous media, fluid & gas dynamics (:cite:`Michaelis2006`, :cite:`Elsinga2006`), ocean engineering; and in solid mechanics, applications may involve fracture mechanics problems, such as the detection and monitoring of cracks and shear bands in quasi-brittle materials. A problem of interest is typically investigated via instrumented lab tests, i.e. under well controlled boundary conditions through a desired time window. Therefore, such experimental campaigns enable rich and extensive data collection via sensors and imaging. This offers the opportunity to integrate such data and conventional image processing techniques with powerful Artificial Intelligence (AI) algorithms, such as machine learning (ML). There are similarities in the acquisition cameras, as used in both PIV and DIC. Currently, this work and the code implementations focus on DIC applications only.

In DIC techniques, the displacement and strain fields are approximated from tracing correlated subsets of pixel patches for a number of sequential images. In fracture problems, an accurate quantification of the displacement field is of critical importance to obtain realistic spatial derivatives, which would reveal the strains within the Fracture Process Zone (FPZ). Detecting and quantifying the spread of the FPZ is crucial to understand the underlying mechanics of fracture and failure of materials and structures. Therefore, the quality of the DIC analyses are strongly dependent on obtaining images of sufficiently high-resolution for the problem of interest. 

A popular high-resolution DIC camera manufacturer (LaVision) has developed the Digital image Acquisition and Visualisation (DaVis) software to control their proprietary hardware. Such cameras record images in the im7 image format, which is not a common format used in popular AI image processing pipelines. 
Therefore, easing the integration of im7 images into AI pipelines seems of vital importance to harness progress in the DIC community. LaVision has produced low-level interfaces to access data from im7 images, via a C++ code, and a wrapper of the code using python. Nonetheless, a barrier is encountered when trying to increase the popularity of the python and C++ codes among Computer Vision (CV) experts. CV scientists do not always possess an expert level of understanding of the mechanics involved in DIC analyses, which is often required to dive more easily through the low-level code documentations. DIC works with physically meaningful vectors and tensors, used in Newton's laws as adopted by Continuum Mechanics, while AI-image pipelines are able to perform the detection and segmentation tasks in an abstract manner by-passing the need to know about the laws governing the detection of the FPZ. An alternative python code that aimed to ease this obstacle is the ReadIM package by Alan Fleming (https://pypi.org/project/ReadIM/), which uses the LaVision's low-level C++ code to extract and write im7 images as Numpy arrays. In addition, a first trial of a higher-level ReadIM library ("IM", https://bitbucket.org/fleming79/im/src/master/) was programmed as a research code, altough not accessible via the standard python package index (PyPI) repository.

It is believed that a good first high-level code that integrates im7 images effectively into AI pipelines should address the need of the selection of Regions of Interest (ROIs). This is especially valid for complex scenarios, where removing data beyond an initial ROI benefits computing speed, in detection and segmentation stages without compromising accuracy. It is envisaged that problems involving deformation localisation, that account for relatively small displacements, would benefit from setting a rough initial (static) ROI for a large sequence of images. For example, a crack is expected to propagate through the weakest zone in a lab specimen, or through the most critically-loaded structural sections, and hundreds or thousands of sequential crack images would be needed for training an AI pipeline.

In this regard, the current work aims to release an open-source python package, named ``rimcli`` (**R**\ ead DIC **IM**\ ages using the **C**\ ommand **L**\ ine **I**\ nterface), high-level code that eases the integration of large sets of im7 images into AI pipelines. The code is extensible, and has been designed with a flexible architecture to incorporate additional pre-processing steps that may be required for custom AI pipelines in the future. 

Statement of need
------------------

The novelty of this high-level repository lies in unlocking the non-expert use of im7 files in a format (e.g. png) suitable for streaming into CV and AI pipelines. This is done primarily through a single command line (CLI) operation, and therefore, suitable for integration into High Performance Computing (HPC) jobs that handle large numbers of non-interactive commands and tasks. In particular, high resolution im7 images are strong candidates to fine-tune popular CV models using transfer learning. The user needs not to worry in understanding the complex settings of stereoscopic image acquisition and storage, nor the theoretical foundations of DIC. The user retrieves 2D images corresponding to each field of view (FOV) available in the im7 format, gets these as a numpy array by using the ReadIM package, and exports the images in a common format for AI analysis. Useful information of the setting, such as number of syncronised cameras and image resolution are also sent as an output. Generation of ROIs is also possible, resulting in each image becoming suitable for streaming into AI pipelines, even in complex scenarios where additional image data would normally be interfering with the real zone of interest. 

## Envisaged use of the RIMCLI by experimental (solid/fluid) mechanics researchers
CV models and associated (AI) pipelines are usually developed by computer experts/scientists, who may not be fully familiar with the physics principles behind DIC. 
It is envisioned that providing computer scientists with a fast-track tool to get the *raw input image* for AI labelling/training or inference would accelerate the pace at which new AI-driven techniques are developed to complement conventional DIC.
# Overview of RIMCLI
The libraries are built on top of the powerful ReadIM python package. The original ReadIM package by Alan Fleming, which interfaces C++ code for the low-level access of the im7 image format as Numpy arrays, has been recently repotentiated to secure cross platform access and provided with substantial incremental development to include further examples, automated testing and migrated to a new site to reactivate maintenance by the authors of this paper.
## Research making use of the libraries: COLVIRM_im7conversion
The COLVIRM project at Cardiff University (United Kingdom), Escuela Superior Politecnica del Litoral (ESPOL-Ecuador) and Universidad de la Rioja (UNIR-Spain) made use of the initial versions of the RIMCLI repository to convert im7 images into other common formats for AI analysis of crack propagation in historical mortars. The repository makes extensive use of the python package ReadIM, developed originally by Alan Fleming  and now being migrated to a new repository by the authors of this paper to repotentiate maintenance and visibility of the libraries. Historical usage of the original ReadIM package by other researchers is also reported in the personal webpage of Charles Jekel (https://jekel.me/2015/Open-and-View-IM7-Files-with-Python/)

Key features
------------

* **im7 image CLI-handling:**
  * **Single im7 image call:** Included in this original CLI-version
  * **Multiple im7 image call:** To be extended
* **Cross platform automated-testing:** Testing scripts should be created to test successful installation in Linux/Windows OS. 
* **Extended examples including HPC usage:** The original CLI-version has been already tested in an HPC environment
* **Database of subsets of im7 images:** Subset of images of recent research projects, which do not compromise the confidentiality of ongoing research will be made available

Applications and limitations
-----------------------------
The CLI-version of ReadIM has been extensively used for im7 image conversion, to accelerate integration of DIC images into AI pipelines, with especial interest in making it easy to use in an HPC environment by a single command line operation. Although the base version of the libraries, ReadIM, was of generic usage for im7 and vc7 image conversion, it is still a matter of future work to extend the CLI capabilities towards vc7 images.

Real World example
------------------

To be completed

Acknowledgement
----------------

The access to the Super Computing Wales project's facilities (Hawk supercomputing nodes) through the project SWC 2233 at Cardiff University is greatly acknowledged. The encouragement and initial communications by Dr Alan Fleming, the original maintainer and developer of the ReadIM libraries, are greatly acknowledged. The enthusiastic involvement of the Open Source Software Student Chapter at Escuela Superior Politecnica del Litoral (Comunidad de Codigo Abierto, KOKOA-ESPOL, Ecuador) is thankfully recognised. The following developers at KOKOA-ESPOL contributed with either coding and/or testing: <developer 1>, <developer 2>.

History
--------

| Name |   Year |  Description                                                                                    |
|:---  |:---    |:---                                                                                             |
|CAG   |Mar24   |Initial coding of (local) rimcli package                                                         |
|CAG   |Jun24   |Initiated Github repository for version control                                                  |
|CAG   |Mar25   |Transferred ownership of the initial github repository of rimcli to KOKOA-ESPOL. Not in PyPi yet |


Note: 
-----

Should you like to contribute to the ``rimcli`` project, go to the :ref:`Basic package structure` to have a first glimpse of understanding of the code structure. A good understanding of the :ref:`Coding standard` is also desirable. 
Once acquainted with the code structure and coding standards, do refer to further guidelines for developers in the documentation. 

For more information feel free to contact a member of KOKOA-ESPOL.

References:
-----------

.. bibliography:: references/litdic.bib
