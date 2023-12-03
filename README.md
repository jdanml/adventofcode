
# adventofcode
This project contains my solutions for the challenges presented in the [Advent of Code event](https://adventofcode.com/2023/about) 
Solutions are written in the following languages:
  * Python

## Run Locally  

1. Clone the project  

~~~bash  
  git clone https://github.com/jdanml/adventofcode
~~~

2. Go to the project directory  

~~~bash  
  cd adventofcode
~~~

3. Install [Poetry](https://python-poetry.org/docs/)
   
4. Install dependencies with Poetry

~~~bash  
poetry install
~~~

5. Run the solution for a given day as follows 

~~~bash  
poetry run aocrun day <year> <day>
# Example
poetry run aocrun day 2023 1
~~~

Alternatively, you can also do:

~~~bash  
poetry shell
aocrun day <year> <day>
~~~

## License  

[MIT](https://choosealicense.com/licenses/mit/)
