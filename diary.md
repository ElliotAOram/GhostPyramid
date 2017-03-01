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