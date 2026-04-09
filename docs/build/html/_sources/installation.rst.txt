Installation
============

Dedicated environment
---------------------
At first initiate a python environment. If you have not created a dedicated environment yet, then create one as follows.
The environment should be based on a python version suitable for the ``rimcli`` package (``python>=3.8`` is recommended).
An environment could be created and initiated using ``conda``, see e.g. installation of `anaconda/miniconda <https://www.anaconda.com/docs/getting-started/miniconda/install#quickstart-install-instructions>`_ (miniconda is a minimal package manager equipped with ``conda``). Run ``python --version`` to confirm the python version, and ``pip list`` to check the current packages installed in your newly created environment.

  .. code-block:: bash
  
      # Activate conda. Replace ~/anaconda3 with (mini/ana)conda path
      source ~/anaconda3/bin/activate
      # Create a conda environment, named "rimenv" with python=3.8:
      conda create --name rimdev python=3.8 -y
      # Activate python environment
      conda activate rimdev
      # Get rimenv's python version
      python --version
      # Get list of default packages installed in rimenv
      pip list

Development tools
-----------------
Modern environment package managers such as ``conda`` would often equip your new environment with ``pip``, enabling you to install further python packages from standard repositories such as `testpypi <https://test.pypi.org/>`_ and `pypi <https://pypi.org/>`_. Further information on package installation can be obtained with ``pip --help``.

In addition, your environment may be initiated with development tools such as ``setuptools`` and ``wheel`` by default. These would be useful if you were to further develop the ``rimcli`` package. If needed ``pip install setuptools wheel``. It is also useful to ``pip  install twine``, since this package allows you to upload your development to the standard python package repositories, given that you possess enough authorisation credentials, e.g. through a (test)pypi token.

Install from (test)pypi
-----------------------
In a terminal, initialise your :ref:`dedicated environment <Dedicated environment>`. Then run the ``pip install`` method below.

 .. code-block:: bash
  
    # Install from (testpypi), replace <version> as required
    pip install -i https://pypi.python.org/simple --extra-index-url https://test.pypi.org/simple/ rimcli==<version>

The list of rimcli versions are available in `(test)pypi <https://test.pypi.org/project/rimcli/0.0.18/#history>`_

Install from source code
------------------------
Download a stable version of the `source code from (test)pypi <https://test.pypi.org/project/rimcli/#files>`_. Extract the contents of the compressed ``rimcli-<version>.tar.gz``.
Initiate your :ref:`dedicated environment <Dedicated environment>` within the main package folder. Compile the distribution files from the ``setup.py`` file, and ``pip install`` the newly compiled binary from ``./dist/*.whl``. You can check that the ``rimcli`` package was installed by inspecting your packages using ``pip list``.

 .. code-block:: bash
 
    # Compile rimcli package source code and distribution
    python ./setup.py sdist bdist_wheel
    # Install compiled binary distribution of rimcli
    pip install ./dist/*.whl
    
**For developers only:**
Only if you have made changes in your python source code, and have generated a few versions (versioned through the ``setup.py``), it is possible you may have more than one ``*.whl`` in ``./dist/``. In that case, indicate the specific binary version to be installed. Check your new package version is installable for every distribution that you may want to upload to (test)pypi. Do this test before uploading.

Uploading to the (test)pypi repo is done by the command ``twine upload --repository testpypi ./dist/*``.
Make sure that only the latest version of your modified package (as binary ``*.whl`` and compressed source code ``*.tar.gz``) is present in your ``./dist/`` folder before uploading to (test)pypi.
Remember to upload to the correct repository, i.e. either ``testpypi`` or ``pypi``. It is always recommended to try uploading to ``testpypi`` before any attempts to upload to the official `pypi repo <https://pypi.org/>`_ (no versions in pypi are available yet).

Rendering the html documentation
--------------------------------
A local html documentation is attached when the :ref:`source code is downloaded <Install from source code>`, e.g. from the (testpypi) repository.
Extract the contents of the compressed source code folder, and change the location of your file explorer to the main package folder. The html documentation is found in ``./docs/build/html``.
Open any of the ``*.html`` files to start navigating the documentation.

If the html documentation is for any reason corrupted, you would need to regenerate it using ``sphinx``. First follow the :ref:`source code installation instructions <Install from source code>` so that all **package dependencies** are installed in your dedicated environment.
Then, open a terminal within the main package folder and run ``sphinx-build`` to regenerate the html repo.

 .. code-block:: bash
 
     # Clean html documentation repo using sphinx
     rm -rf ./docs/build
     # Regenerate html documentation repo using sphinx
     sphinx-build -M html ./docs/source/ ./docs/build/
     
**For developers only:**
Only if you have made changes in your python source code, **before rendering your package html documentation**, open a terminal within the main package folder and run ``sphinx-apidocs`` to regenerate the source ``*.rst`` files for all subpackages and modules.

 .. code-block:: bash
 
    # Clean previous package documentation for all subpackages/modules
    rm ./docs/source/rimcli.*
    # Regenerate package documentation for all subpackages/modules
    sphinx-apidoc -o ./docs/source/ ./rimcli

If errors occur use ``rm ./docs/source/rimcli.*.rst`` to delete the existing source ``*.rst`` files before running the lines above.
