# Diary 



## Week 1

### 31/01/2017
* Meeting with Helen re. starting project
* Set up github repo
* OPS: First draft of project description

### 03/02/2017
* OPS: Updates to description
* OPS: First draft of project tasks

### 05/02/2017
* OPS: First draft of delieverables
* OPS: Spelling and grammar corrections to all sections




## Week 2

### 06/02/2017
* OPS: Add PDF of OPS first draft
* Add initial labels and milestones to GitHub repository
* Create OPS completion issue

### 08/02/2017
* OPS: Add references to bibliography (1,2)
  * background subtraction: https://hal.inria.fr/inria-00545478/document
  * Pyramid: https://www.comsol.nl/blogs/explaining-the-peppers-ghost-illusion-with-ray-optics/

### 09/02/2017
* OPS : Add references to bibliography (3,4)
  * OpenCV video tutorial: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html#display-video
  * Single person FDD (Chapter 2,3): http://fddpma.sourceforge.net/help/fddpma_thesis.pdf
* OPS: Submit 'first submission' to blackboard
* Get LaTeX and BibTeX running on local machine
* Write first draft of ProjectMethodology document (details of process for development during the project)

### 10/02/2017
* Review and submit process document to GitHub
* Write and review Use Case diagram and documentation

### 12/02/2017
* Add issues to GitHub for design 
* Write initial activity diagram for basic system




## Week 3

### 13/02/2017
* Completed Actvity diagram for full system (Version 1.0)

### 14/02/2017
* Complete video processing UML class diagram

### 15/02/2017
* Add initial first draft of staging area design

### 16/02/2017
* Review and merge staging area design
* Build objects in visio for component diagram
* Create system component diagram
* Review and submit component diagram documentation
* Create first draft of UML class diagram for Charades Game (Requires review - PR open)

### 17/02/2017
* Review and merge Charades game class diagram
* Build features list
* Priority / Dependency / Complexity
* Set up jenkins
  * Install on windows
  * Work out issues with admin acc - username autoset to lower case, had to reset jenkins security to force login
  * Integrate jenkins with github project
  * Fix rate limit issue - OAuth for git (increase to 5k requests per hour from 60)
  * Use Bat notation over sh to allow JenkinsFile to work for Windows
  * Get Helloworld output from Jenkins
  
### 18/02/2017
* Implement feature 1 and create pull request for feature


### 19/02/2017
* Continued work on Jenkins to try and get python unit tests to run - currently without success



## Week 4


### 20/02/2017
* Resolve feature 1 pylint errors
* Resolve feature 1 coverage issues
* Put code from feature 1 into packages
* Ensure feature 1 tests pass
* Merge feature 1 to master
* Fix jenkins build reporting for: tests, coverage and pylint(almost) 
  * http://bhfsteve.blogspot.co.uk/2012/04/automated-python-unit-testing-code_27.html

### 21/02/2017
* Get jenkins to run from github rather than local - still running builds manually
* Hotfix for feature 1 design
* Minor update to feaute dependencies
* Meeting with Helen to agree feature list and time line
* Complete Pull request for feature 3 - to be reviewed

### 22/02/2017
* Forced to revert feature 3 due incorrect understanding of image representation in python OpenCV
* Design complete for feature 5k
* Tests for helper functions created and passing
* Tomorrow need to write `process_and_output_video` function 
  * stitch together helpers 
  
### 23/02/2017
* Complete feature 5 and create pull request

### 24/02/2017
* merge feature 5

### 25/02/2017
* Design feature 4

### 26/02/2017
* Implement feature 4
* Begin work on large scale refactor



## Week 5

### 27/02/2017
* Start iteration 2
* Test applocation using large pyramid and touch screen table
* Group meeting discussing progress and mid-project demo
  * Prepare talking points for next group meeting

### 28/02/2017
* Finish large scale refactoring and udpdate design
* Merge feature 4
* Remove vpa_run.py from coverage tests
  * See feature 4 PR for justification
* Start spike work on feature 2 (background subtraction) ahead of design phase
* Consider testing strategy
  * Most likely similar to rotate (np.array to make custom image)
  
### 01/03/2017
* Implemented feature 2 with image subtraction approach with relevant tests
    * While this is a good technique for finding motion, this suffers from the problem
      that when subtracting one image from another, this will also remove the colour channel from the
      foreground image as well as the background. for example if the background is completely green and 
      you subtract this from the original frame, then you lose any green from the object of interest

### 02/03/2017
* Considered revised background subtraction routine that use a green screen instead of an unknown background


### 04/03/2017
* Spent much of the morning ironing my new green screen background!
* Implement code that checks each pixel in the frame and is it is the same as a given background colour (within a threshold)
  then it changes that pixels colour to black
* This code almost works (takes a bit of fiddlering to get it right when the lighting is not great (many shadows/lighting
  highlights)) but is currently very ineffecient causes a huge FPS drop to around 5-10fps (est.) 
  * This speed is not acceptable for the end product so I must now consider possible ways to speed up the execution of 
    the background subtraction
    
### 05/03/2017
* Initial research into multithreading / cuda (throwing python threads out to the GPU)

## Week 6

### 06/03/2017
* Continued investigation into speeding up green screen
* Implement multithreading and multiprocessing
  * Showed no significant speed increase

### 07/03/2017
* Final draft of poster for assignment
* Meeting with Helen deciding to put background subtraction on hold for now

### 08/03/2017
* Freeze background subtraction investigation (renames on git branch)
* Set up andriod environment (https://developer.android.com/training/basics/firstapp/creating-project.html)

### 09/03/2017
* Update design and create UI design for charades game (feature 6)
* Implement status bar removal for app
  * https://developer.android.com/training/system-ui/status.html
  * http://stackoverflow.com/questions/28144657/android-error-attempt-to-invoke-virtual-method-void-android-app-actionbar-on

### 10/03/2017
* Implement all three interfaces for the app
* Begin to write UI tests
  * http://stackoverflow.com/questions/9405561/test-if-a-button-starts-a-new-activity-in-android-junit-pref-without-robotium

### 11/03/2017
* Complete tests and put up Pull request

## Week 7

### 13/03/2017
* Merge pull request for feature 6
* Write issue for feature 7
* Close old milestones to ensure git is up-to-date
* Remove milestone for Background subtraction issue (feature 2)

### 14-16/03/2017
* Presenting prototype at science week

### 17/03/2017
* Mid project demo
* feedback from mid project demo suggests it might be best to focus the project title a bit more - The current does not state the 
  end goal (Charades game) and is generic
* The app should be developed as a website instead. There is no real justification for doing an App by cotrast to a website hence 
  there will need to be a re-design to account for this and additional features should be reorganised to attempt to allow for the 
  change in the time schedule
  
## Week 8 

### 20/03/2017
* Set up Django and start following instruction in book: http://djangobook.com/

### 21/03/2017
* Begin spike solutions for the website

### 22/03/2017
* Complete design for website instead of App.
* Remove App UI design in favour of website design
* Write tests using selenium and LiveServerTestCase (Django) 
  * https://docs.djangoproject.com/en/1.8/topics/testing/tools/#liveservertestcase
  * https://pypi.python.org/pypi/selenium

### 23/03/2017
* Integrate tests with jenkins build
* Implement additional code to complete feature 6
* Merge feature 6

### 24/03/2017
* Design Feature 7
* Write tests for feature 7 - selenium
* Speed up selenium tests by only opening one instance per test class
  * Fix Errno10054 in selenium by using browser.refresh in teardown()
* Write tests for feature 7 - core python

### 25/03/2017
* Add implementation for viewer.py and get tests to pass
* Add implementation for actor.py and get tests to pass

### 26/03/2017
* Fix pylint issues for feature 7
* Update design for feature 7 with minor changes
* Merge feature 7
* Feature 8 UI design (phrase_selection.html)
* Feature 8 Class diagram (phrases module)
* Add tests for phrases module
* Add tests for select_phrase.html

## Week 9

### 27/03/2017

* Implement code to pass tests in feature 8
* Use XPath in selenium to test button values using get_attribute
  * http://selenium-python.readthedocs.io/locating-elements.html#locating-by-xpath

### 28/03/2017
* Add design for acting (single and multi word)
* Add tests for redirects
* Implement redirects for pages when actor not present

### 29/03/2017
* Add warnings on index for no actor
* PR for feature 8
* Resolve pylint issues
* Add tests for feature 9
* Add implementation to pass tests
* Initial static file set up
* Add start of css

### 30/03/2017
* Complete css
* Change tests to Static to allow for css import on localhost
* Add highlighting on current word button and word

### 31/04/2017
* Close and merge feature 9

### 01/04/2017
* Add session variable to store viewer number browser side
* Add guess basic test
* Improve Instructions.html and view
* Use url functions over hard coded addresses

## Week 10

### 04/04/2017
* Remove uneeded variable assignment in tests in favour of one-liners
* Add the reset page

### 06/04/2017
* Implment game.py and tests
* Add test redirect on login for too many actors
* update tests to work with game.py implementation and use reset where required
* Fix pylint issues for feature 10
* Merge feature 10

### 07/04/2017
* Write up issues for feature 11
* Add genre information to design 
* Implement tests for genre in guess.html
* Add code to pass tests. 
* Add code to remove current word info when phrase is one word.
* I should make it so the button for the viewer does not appear until the actor has selected a phrase

## Week 11

### 10/04/2017
* first draft for acknowledgement and abstract

### 11/04/2017
* first draft for background chapter(almost complete)

### 12/04/2017
* Only add continue button when actor has selected a word
* Update tests for this 
* settled on polling functionality to find out when the viewer button should be displayed
* Need to work out how to call python model function from with javascript in template
  * Polling function:
    * http://stackoverflow.com/questions/20820115/how-to-automatically-fetch-new-data-from-server
    * http://stackoverflow.com/questions/8106230/django-refresh-page-if-change-data-by-other-user    

### 13/04/2017
* Not possible to call view function in template due to HTTP Response style of django
* Decided best way to deal with this is to implement an API
* Spike work for API/ JQuery / Javascript on instructions page

### 14/04/2017
* Write tests for API
* Refactor phrase ready checking to Actor class
* fix bug with current_word not being set when phrase length is 1 word
* Implement API in instructions.html
