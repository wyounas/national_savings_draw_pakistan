# PCLI (A command line script to see if you've won a prize bond) 

You can use this command line script to search your prize bond draws on [National Savings'](http://savings.gov.pk/draw-search/) website. It's particularly useful if you have many prize bonds and quickly want to see if you've won anything. 

![screen shot](https://drive.google.com/open?id=1AZeq2ryGThqeFS6wPuI_1DRSD-C2shWC)

# Why did I build this?

I will add details soon.




# Installation

## Python

I built this on Python 3.4.5. So first we need to install Python.

On Mac, I used Homebrew to install Python e.g. one can use this command:

To install on Windows, you can download the installer from  [here](https://www.python.org/downloads/windows/). Once downloaded this installer can be run to complete Python's installation.

For Ubuntu you might find this  [resource](https://askubuntu.com/questions/802279/how-to-install-python-3-4-5-from-apt)  useful.

## Virtual environment

Now it's time to create a virtual environment (assuming you cloned the code under ~/code/pkli).

First line in the above snippet creates a virtual environment named venv under ~/code/pkli. The second command activates the virtual environment.

In case you need more help with creating a virtual environment this  [resource](https://docs.python.org/3/library/venv.html)  can prove to be useful.

## Install the required libraries

To install the required libraries please run this:

`> pip install -r requirements.txt`

# Usage

Save your prize bond numbers in the NUMBERS list. And run this script like this:

    > python prize_bonds.py

As of May 2020, this is working. Unfortuantely, it will break in case National Savings make changes to their website. 

# Authors

Waqas Younas. 

Email: I can be reached at waqas.younas@gmail.com. 
Twitter: http://twitter.com/wyounas


# License


[MIT](https://choosealicense.com/licenses/mit/)