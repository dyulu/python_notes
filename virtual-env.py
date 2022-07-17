# https://docs.python.org/3/library/venv.html
#
# A virtual environment is a Python environment such that the Python interpreter, libraries and scripts installed into it
#     are isolated from those installed in other virtual environments, and (by default) any libraries installed in a “system”
#     Python, i.e., one which is installed as part of your operating system.
# A virtual environment is a directory tree which contains Python executable files and other files which indicate that it is
#     a virtual environment.
# Common installation tools such as setuptools and pip work as expected with virtual environments. In other words, when a virtual
#     environment is active, they install Python packages into the virtual environment without needing to be told to do so explicitly.

$ python3 -m venv -h
usage: venv [-h] [--system-site-packages] [--symlinks | --copies] [--clear]
            [--upgrade] [--without-pip] [--prompt PROMPT]
            ENV_DIR [ENV_DIR ...]

Creates virtual Python environments in one or more target directories.

positional arguments:
  ENV_DIR               A directory to create the environment in.

optional arguments:
  -h, --help            show this help message and exit
  --system-site-packages
                        Give the virtual environment access to the system
                        site-packages dir.
  --symlinks            Try to use symlinks rather than copies, when symlinks
                        are not the default for the platform.
  --copies              Try to use copies rather than symlinks, even when
                        symlinks are the default for the platform.
  --clear               Delete the contents of the environment directory if it
                        already exists, before environment creation.
  --upgrade             Upgrade the environment directory to use this version
                        of Python, assuming Python has been upgraded in-place.
  --without-pip         Skips installing or upgrading pip in the virtual
                        environment (pip is bootstrapped by default)
  --prompt PROMPT       Provides an alternative prompt prefix for this
                        environment.

Once an environment has been created, you may wish to activate it, e.g. by
sourcing an activate script in its bin directory.

# Debian/Ubuntu
# Create virtual environment for ProjectX
apt update
apt install python3-venv
mkdir ProjectX
python3 -m venv ProjectX

$ tree -L 2 ProjectX/
ProjectX/
├── bin
│   ├── activate
│   ├── activate.csh
│   ├── activate.fish
│   ├── easy_install
│   ├── easy_install-3.7
│   ├── pip
│   ├── pip3
│   ├── pip3.7
│   ├── python -> python3
│   └── python3 -> /usr/bin/python3
├── include
├── lib
│   └── python3.7
├── lib64 -> lib
├── pyvenv.cfg
└── share
    └── python-wheels

7 directories, 11 files

# Activate virtual environment and check the list of packages in it
$ source ProjectX/bin/activate
(ProjectX) :~$ pip3 list
Package       Version
------------- -------
pip           18.1   
pkg-resources 0.0.0  
setuptools    40.8.0 


# Install packages, e.g., requests, in virtual environment
# pip3 list: list all installed packages, regardless of how they were installed
# pip3 freeze: list only packages installed by pip
# python3 -c 'help("modules")': list all available modules
(ProjectX) :~$ python3 -m pip install requests
(ProjectX) :~$ pip3 list
Package            Version  
------------------ ---------
certifi            2022.6.15
charset-normalizer 2.0.12   
idna               3.3      
pip                18.1     
pkg-resources      0.0.0    
requests           2.28.0   
setuptools         40.8.0   
urllib3            1.26.9   
(ProjectX) :~$ pip3 show requests        # python3 -m pip install --upgrade requests; pip3 uninstall requests
Name: requests
Version: 2.28.0
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
Author-email: me@kennethreitz.org
License: Apache 2.0
Location: /root/ProjectX/lib/python3.7/site-packages
Requires: charset-normalizer, urllib3, idna, certifi
Required-by: 

# Produce the list of packages in the virtual environment for cloning the env by running pip3 install
#     python3 -m pip install -r ProjectX-requirements.txt
(ProjectX) :~$ pip3 freeze > ProjectX-requirements.txt
(ProjectX) :~$ cat ProjectX-requirements.txt 
certifi==2022.6.15
charset-normalizer==2.0.12
idna==3.3
pkg-resources==0.0.0
requests==2.28.0
urllib3==1.26.9

# Deactivate virtual environment
(ProjectX) :~$ deactivate

