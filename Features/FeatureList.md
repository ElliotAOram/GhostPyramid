# Feature List
### Version 1.4
### 23/04/2017

| Number        | Description                                                     | Complexity (1-5)  | Priority (1-5) | Dependencies | Prototype |
| ------------- |:---------------------------------------------------------------:| -----------------:|---------------:|-------------:|----------:|
| 1             | Capture the video from the external camera                      | 1                 | 5              | None         | True      |
| 2             | Subtract the background from the video feed                     | 4                 | 4              | 4            | True      |
| 3             | Rotate and scale video feeds where required                     | 2                 | 4              | 2,4          | True      |
| 4             | Output the video feed to a window for display                   | 1                 | 4              | 1            | True      |
| 5             | Display the home page of the website                            | 1                 | 1              | None         | False     |
| 6             | Select the type of User you are (Viewer / Actor)                | 2                 | 3              | 5            | False     |
| 7             | Select a phrase as Actor                                        | 2                 | 3              | 6            | False     |
| 8             | Select a word from the phrase as Actor                          | 2                 | 2              | 7            | False     |
| 9             | Be able to log into a session/room using room code              | 4                 | 3              | 8            | False     |
| 10            | Display word and genre information on Viewer interface          | 3                 | 3              | 8            | False     |
| 11            | Allow Viewer to guess the current word                          | 2                 | 2              | 10           | False     |
| 12            | Allow Viewer to guess the phrase                                | 2                 | 3              | 10           | False     |
| 13            | Inform Users when the word has been guessed correctly           | 2                 | 3              | 11           | False     |
| 14            | When word is guessed correctly prompt Actor for new word        | 3                 | 3              | 12           | False     |
| 15            | Inform Users when phrase has been guessed correctly             | 2                 | 3              | 12           | False     |
| 16            | Build list of possible phrases                                  | 1                 | 2              | None         | False     |
| 17            | Establish end game conditions                                   | 3                 | 1              | 15           | False     |


* Feature 3: This feature was not correct as explained in https://github.com/ElliotAOram/GhostPyramid/pull/34

* Feature 10: Added session feature and changed to website over app

* Fix dependency numbering