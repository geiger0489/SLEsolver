# SLEsolver

SLEsolver is a little PyQt4 app I implement for solving Systems of Linear Equations (aka SLE).

For example:
  2x	+	y	−	2z	=	3
  x	−	y	−	z	=	0
  x	+	y	+	3z	=	12

It works as follows:
  1. Type a system inside the Text Area.
  2. Press "Solve" button.
  3. Enjoy the result.

The app consists of three parts (modules):
1. Main file (SLEsolver.pyw). It contains PyQt classes and gui-related algorhytms.
2. Parser (parser.py). It's a class that provides parsing of input data and transferring it to evaluator, 
   It also represent opposite - gets data from evaluator and transfer it to the Text Area.
3. Evaluator (core). Base class which produces all calculations. Only pure math.
   It is arranged to make it possible to use it as pluggable lib for other apps.
   You also can plug it to your own app.

I write it for fun and for the purpose of learning math.
Ejoy.
