# Introduction to AI: Search Algorithms

Alessandro Ferrari - Programming component of the Intro to AI: Search Algorithms course


The program was developed and tested using a Python 3.8.5 64-bit virtual environment created in linux using the virtualenv program which can be installed by running "pip install virtualenv" or by installing the "python-virtualenv" package on most linux distros. The requirements.txt file doesn't actually list requirements, it's just the output of running "pip freeze > requirements.txt". There shouldn't be any extra dependencies.
The program was tested in Arch Linux using kernel 5.8.12-arch1-1 and Windows 10 using the latest build as of 14/08/2020.
The program is written using the camelCase standard.
The script takes 1 parameter, being the path to a file.

Example of script usage:
"python3 src/solve.py assignments/input3.txt"

Originally the program was split in 2 files, domino.py and solve.py, I didn't test all inputs after joining the 2 files, but it shouldn't cause any errors.

File structure
The file should follow the requirements given in the pdf:
	- First Line: Max size of frontier
	- Second Line: Max size of the set containing the explored states(to avoid going in an infinite loop)
	- Third Line: Either 1 or 0, 1 for verbose output, 0 for quiet output
	- Fourth Line: Number of dominoes
	- Fifth line: Dominoes

The program output doesn't strictly follow the sample outputs because of the difference in serializing the dominoes

There is also a git directory, which contains the git repository which I used for version control for this project. I used my local git servers as I wasn't sure if it was ok to release what we were writing to the public, so I just downloaded every branch.

Git structure:
- main branch: branch used until we started implementing iterative deepening
- iterativeDeepening branch: branch used after we started implementing iterative deepening
- final branch: final branch used to implement tweaks and optmizations at the end of the project
- Release V1-0-0: This is a tag of the commit which contains code which has depth first search implemented and working, but not dfs, tested on all inputs


