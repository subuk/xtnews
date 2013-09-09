xtnews
======

Simple Frontik backend

Dev install:

::

   git clone https://github.com/subuk/xtnews.git
   cd xtnews
   mkdir ~/envs
   virtualenv ~/envs/xtnews
   . ~/envs/xtnews/bin/activate

   pip install lxml==2.2.8
   pip install git+https://github.com/hhru/tornado
   pip install -r dev_requirements.txt
   python setup.py develop

   xtnews-initdb xtnews.ini
   honcho start
