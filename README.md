# BMI_6018_Final_Project
## Calorie Tracker Program by Erik R. Thomas and Maxine R. Gavin
### Introduction
Obesity is a common health issue in the United States. The CDC found that more than one-third (36.5%) of U.S. adults are obese. A method of decreasing the number of over-weight and obese individuals is through lifestyle changes. This project aims to improve self awareness concerning daily caloric needs. 
### Program Use
This project involves a user interface that asks the individual the following questions: Gender, Age, Weight, Height, Physical Activity, Length of Physical Activity, and Calorie Consumption. Upon collection of this information the user recieves caloric balance. A positive caloric balance indicates a calorie surplus and a negative caloric balance indicates a calorie deficit. This is important information for individuals who would like to understand their daily needs and consume calories responsibly.
### Files 
The program involves five files:
#### Calorie Tracker (final project).ipynb is the user interface file. 
Calorie Tracker (final project).ipynb is the user interface file. This file allows the user to enter the neccesary data to retrive their caloric balance, and view their progress on a matplotlib graph. It does this by importing both calorie.py and caloriedb.py (which are discussed below) and incoporating them into its programmed menu system. This menu system asks the user a variety of questions and stores the answers which are used to determine caloric balance and evetually produce a visual progress graph for each session using matplotlib. 
#### calorie_tracker.py
This is a python file that is equivalent to Calorie Tracker (final project).ipynb, except that the graphing elements are commented out. 
#### calorie.py
Caloric balance is determined using the calorie.py file. In this file a class called Calorie that gets the information entered by the user and utilizes it to calculate caloric balance is created. The Calorie class incorparates the Harris-Benedict Equation equation that calculates the caloric balance. The equation used is shown below. 
* The imperial equation for Males is BMR = 66 + ( 6.2 × weight in pounds ) + ( 12.7 × height in inches ) – ( 6.76 × age in years ) 
* The imperial equation for Females is BMR = 655.1 + ( 4.35 × weight in pounds ) + ( 4.7 × height in inches ) - ( 4.7 × age in years )
* To incorparate calories burned in exercise in the caloric balance we used a table on what'scookingamerica.net (link listed below) that had values of calories burned per pound per minute.
* https://whatscookingamerica.net/Information/CalorieBurnChart.htm
#### caloriedb.py
caloriedb.py creates and manipulates a database that stores the users ending caloric balance for a session and what the session number was.
#### calorie.db
This file is a SQLite database that houses the users ending caloric balance for a session and what the session number was.
### User Instructions
To use this calorie tracker, simply initialize the Calorie Tracker (final project).ipynb program and enter the appropriate data when prompted (Gender, Age, Weight, Height, Physical Activity, Length of Physical Activity, and Calorie Consumption). This data will be used to calculate caloric balance at several steps. At the end of the session your final caloric balance will be displayed graphically alongside the previous sessions ending caloric balance. When testing this program 16 trial sessions were done, your first session will be number 17. Enjoy!
