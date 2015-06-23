# SLEsolver

<b>SLEsolver</b> is a little <a href="http://www.riverbankcomputing.co.uk/software/pyqt/intro">PyQt4</a> app I implement for solving <a href="https://en.wikipedia.org/wiki/System_of_linear_equations">Systems of Linear Equations</a> (aka SLE).

For example:
  <ul>
  <li>2x<sub>1</sub>	+	x<sub>2</sub>	−	2x<sub>3</sub>	=	3</li>
  <li>x<sub>1</sub>	−	x<sub>2</sub>	−	x<sub>3</sub>	=	0</li>
  <li>x<sub>1</sub>	+	x<sub>2</sub>	+	3x<sub>3</sub>	=	12</li>
  </ul>

It works as follows:
  1. Type a system inside the Text Area.
  2. Press "Solve" button.
  3. Enjoy the result.

The app consists of three parts (modules):
  1. <b>Main file</b> (SLEsolver.pyw). It contains PyQt classes and gui-related algorhytms.
  2. <b>Parser</b> (parser.py). It's a class that provides parsing of input data and transferring it to evaluator, 
     It also represents opposite - gets data from evaluator and transfers it to the Text Area.
  4. <b>Matrix</b> (matrix.py). Class providing basic operations with matrices and vectors.
  3. <b>Evaluator</b> (core.py). Base class which produces all calculations. Only pure math.
     The class is arranged as a pluggable lib for other apps. You also can plug it to your own app.

To run the app make sure that you have installed <a href="http://www.riverbankcomputing.co.uk/software/pyqt/intro">PyQt4</a> and <a href="https://www.python.org/">python3</a> on your machine.

I write it just for fun and for the purpose of learning math.
Ejoy.
