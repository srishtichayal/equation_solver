# equation_solver
# Ipopt (Interior Point OPTimizer)
## Overview
It is an open source software package for large-scale non-linear optimization. It can be used to solve general nonlinear programming problems of the form:
<br>
$min_{x \in R^n} f(x)$
<br>
Such that
$g^L \leq g(x) \leq g^U$
and
$x^L \leq x \leq x^U$
<br>
Where $x\in R^n$ are the optimization variables possibly with lower and upper bounds, $x^L \in (R \; U \; \{-\infty \})^n$ and $x^U \in (R \; U \; \{+\infty \})^n$ 
With $x^L \leq x^U$, $ f:R^𝑛→R$ is the objective function, and 𝑔:ℝ𝑛→ℝ𝑚 are the general nonlinear constraints. 
The functions $𝑓(𝑥)$ and $𝑔(𝑥)$ can be linear or nonlinear and convex or non-convex (but should be twice continuously differentiable). 
The constraint functions, $𝑔(𝑥)$, have lower and upper bounds, $g^L \in (R \; U \; \{-\infty \})^m$ and $g^U \in (R \; U \; \{+\infty \})^m$  with $g^L \leq g^U$.

It is designed to exploit 1st and 2nd Hessian transformations, if provided otherwise it approximates using quasi-Newton methods, specifically a [BFGS update](https://en.wikipedia.org/wiki/Broyden–Fletcher–Goldfarb–Shanno_algorithm)

## Availability

The Ipopt package is available from COIN-OR under the EPL (Eclipse Public License) open-source license and includes the source code for Ipopt. This means, it is available free of charge, also for commercial purposes. 

## How to use
Requirements are:
- Gekko
- Sympy
### Setup
Install requirements 
```
pip install -r requirements.txt
```
Write your equations in _Equations.txt file and execute the code_runner.py file.

To execute code runner file
```
python code_runner.py --equations=<name of file with equations> --answers=<file where answers are printed> --constants=<file where constant values are stored>
```
You can expect the answer now in _Answer.txt file.

### Example usage
This is the _Equations.txt file
```
5-(100+23*9)*abc+23*9*b-23*20*abc**2+23*20*b**2 = 0
100*abc-(100+23*9)*b+23*9*c-23*20*b**2+23*20*c**2 = 0
100*b-(100+23*9)*c+23*9*d-23*20*c**2+23*20*d**2 = 0
100*c-(100+23*9)*d+23*9*k-23*20*d**2+23*20*k**2 = 0
100*d-(100+23*9)*k+23*9*f-23*20*k**2+23*20*f**2 = 0
100*k-(100+23*9)*f+23*9*g-23*20*f**2+23*20*g**2 = 0
0.039+100*f+(-100+9*23)*g-9*10*h+20*23*g**2-20*10*h**2 = 0
100*g-(100+9*10)*h-9*10*i-20*10*h**2-20*10*i**2 = 0
100*h-(100+9*10)*i-9*10*j-20*10*i**2-20*10*j**2 = 0
100*i-(100+9*10)*j-20*10*j**2 = 0
```
- In this implementation, we can replace values with a constant variable and specify that variable in a different file
- For example, we can replace 100+23*9 with _z_:
```
5-(_z_)*abc+23*9*b-23*20*abc**2+23*20*b**2 = 0
100*abc-(_z_)*b+23*9*c-23*20*b**2+23*20*c**2 = 0
100*b-(_z_)*c+23*9*d-23*20*c**2+23*20*d**2 = 0
100*c-(_z_)*d+23*9*k-23*20*d**2+23*20*k**2 = 0
100*d-(_z_)*k+23*9*f-23*20*k**2+23*20*f**2 = 0
100*k-(_z_)*f+23*9*g-23*20*f**2+23*20*g**2 = 0
0.039+100*f+(-100+9*23)*g-9*10*h+20*23*g**2-20*10*h**2 = 0
100*g-(100+9*10)*h-9*10*i-20*10*h**2-20*10*i**2 = 0
100*h-(100+9*10)*i-9*10*j-20*10*i**2-20*10*j**2 = 0
100*i-(100+9*10)*j-20*10*j**2 = 0
```
Then in 'constants.txt'
```
_z_ = 100+23*9
```
You run the code with
```
python code_runner.py --equations=<name of file with equations> --answers=<file where answers are printed> --constants=<file where constant values are stored>
```
The answer now reflects in _Answers.txt file
```
Total time: 10.360125303268433 seconds
f = -0.00010933152706
h = -0.00018293356589
i = -7.7073075802e-05
k = 0.00052650972415
d = 0.0018439213405
g = -0.00041686078721
j = -4.0566497419e-05
b = 0.010341116978
c = 0.0045853284287
abc = 0.022650801207
```
### Extras
To get the code to show the optimization method use, just change the following in gekko_solver.py (line number 56)
<br>
From
```
_m.solve(disp=False)
```
To
```
_m.solve(disp=True)
```

## Limitations
1. You have to replace constants with the constant value.
2. You have to replace the power operator with the ** operator.
3. In case of no solution, the error would be printed in the terminal and not reflected in the _Answer.txt file.
<hr>
I tried covering all the corner cases while inputting the equations, but there might be some cases that I might have missed. Please feel free to raise an issue if you find any.

## References
[Github - Ipopt](https://coin-or.github.io/Ipopt/)  
[Gekko library](https://gekko.readthedocs.io)
