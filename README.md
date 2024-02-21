This project consists in four files containing a simple model to create test cases using Selenium, a Python library that allows the user to interact with elements in the given webpage.
A brief description of each file is given below:

-- Log_def.py - Defines a log format along with the path where the log files are going to be saved.
-- locator.py - Stores in separated classes all the locator codes the script is going to use.
-- page.py - Defines the interactions and tests that will be executed within the webpage.
-- main.py - Opens the webpage and executes the tests in order.

The general idea of this project was to create an automation capable of inputing data in an specific field in the website, check the status changes constantly and, 
when the status changed to complete, download the generated file. 
At every step of the test, the the log function would print in an .txt file if the test was successfull or not, so it would be possible to analize if the application was working correctly.

Finally, it's important to mention that this model works for most of the tests that follow the same structure, which makes it easier to adapat it to other applications.
So it is possible to save a lot of work simply by editing the information in the Python files and applying them to other similar contexts.
