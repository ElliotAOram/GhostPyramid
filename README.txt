===========================================================
=================INSTALLING AND RUNNING====================
===========================================================
Hologram application
====================
The university linux machines in the delphinium already have Pyhton,
NumPy, SciPy, and OpenCV setup and configured. It is advised that you
use those machines run the hologram application if possible. If not
possible, then please follow the steps below.

* Install Python v2.7.6
* Install python-gtk2 (sudo apt-get install python-gtk2)
* Install NumPy  v1.8.2
* Install SciPy  v0.13.3
* Install OpenCV v2.4.8

To run the code:
* Open a terminal window.
* Navigate to the python/vpa directory in the provided source code.
* If you are not using the default web cam on the machine
    * Open the run_vpa.py in an editor of your choosing.
    * Replace the input parameter of VPA.begin_capture() (default 0)
      to the correct ID for the camera. If the machine has two cameras,
      this will most likely be 1.
* Use 'python run_vpa.py' to run the application
* This should produce a black window with 4 duplicate camera feeds that
  all face inward.
* Close the program by pressing 'q' on the keyboard.


Charades Game
=============
To install the Charades Game
* Install Django v1.8.3

To run the code:
* Open a terminal window
* Navigate to the charades directory.
* Use the command 'Python manage.py runserver' to start the server.
* Open a web browser and navigate to http://localhost:8000
* You should now see the website landing page.
* For details of using the website, please consult the user guide below.


============================================================
=======================USER GUIDE===========================
============================================================

* Log into the website using the session id "BSW18" and clicking the 'Actor' button.
* Open a second browser (or tab) and navigate to the localhost:8000 URL.
* Log into the website using the session id "BSW18" and clicking the 'Viewer' button.

Actor
=====
* Read the instructions and continue to the phrase selection page.
* Select a phrase from the five possible options
* If the phrase has multiple words select a word using the buttons below
  each word.
* Wait for the Viewer to guess the word.
* Once the phrase has been successfully guessed the Actor will be redirected 
  automatically to the select phrase page or prompted to select a new word.

Viewer
======
* Wait for the Actor to select a word / phrase (see above instructions).
* Click the continue button that appears once the phrase is ready to be guessed.
* Guess the phrase by typing the word into the text field and pressing submit.
* If correct the viewer will be taken to the waiting for actor page which will show
  current score and if you another user guessed correctly.
* When the Actor has selected a new phrase, the viewer will be automatically redriected
  to the guess page.
  
The above process will happen 3 times before the game completes. After the game completes,
the data will be reset.

To reset the webpage (clear all the data manually) visit the localhost:8000/reset/ URL 
and give the password 'secret'.

