# FindPi
This program was built in python. Python 3 is required to run. It finds the first 7 digit palindrome prime in an input 
string, currently configured to work with pi as formatted in the `pi.txt` file.

## Running
Navigate to the project's root directory, containing `find_pi.py`. 
There are two files that contain pi, `pi.txt` and `PI1MILDS.TXT`. Both contain 1 million decimal digits of pi, but 
`pi.txt` contains the preceding "3." while the other file omits it. The python file is currently 
configured to run and work with `pi.txt`, but if the other format for pi is desired, line:26 in `find_pi.py` 
can be commented out to work with the other .txt file. 

The program is run out of the project directory, from command line, by typing:

`python find_pi.py pi.txt`

The output is delivered back to terminal and reports the first 7 digit prime palindrome in the digits of pi, as well as 
the index of the first digit of the number found.
