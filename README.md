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
python code_runner.py
```
You can expect the answer now in _Answer.txt file.

### Example usage
This is the _Equations.txt file
```
5-z*abc+23*9*b-23*20*abc**2+23*20*b**2 = 0
100*abc-z*b+23*9*c-23*20*b**2+23*20*c**2 = 0
100*b-z*c+23*9*d-23*20*c**2+23*20*d**2 = 0
100*c-z*d+23*9*k-23*20*d**2+23*20*k**2 = 0
100*d-z*k+23*9*f-23*20*k**2+23*20*f**2 = 0
100*k-z*f+23*9*g-23*20*f**2+23*20*g**2 = 0
0.039+100*f+__z__*g-9*10*h+20*23*g**2-20*10*h**2 = 0
100*g-_z_*h-9*10*i-20*10*h**2-20*10*i**2 = 0
100*h-_z_*i-9*10*j-20*10*i**2-20*10*j**2 = 0
100*i-_z_*j-20*10*j**2 = 0
```
- In this implementation, we can specify coefficient values in a separate text file (_Coefficients.txt) 
- For example,
```
z=100+23*9
_z_=100+9*10
__z__=-100+9*23
```

You run the code with
```
python code_runner.py --equations=<name of file with equations> --answers=<file where answers are printed> --constants=<file where constant values are stored>
```
The answer now reflects in _Answers.txt file
```
Total time: 0.6498932838439941 seconds
i = -7.7073075802e-05
d = 0.0018439213405
g = -0.00041686078721
k = 0.00052650972415
c = 0.0045853284287
h = -0.00018293356589
b = 0.010341116978
f = -0.00010933152706
abc = 0.022650801207
j = -4.0566497419e-05

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

## Things to Keep in Mind
1. Use ** for powers (e.g., write x**2 instead of x^2)
2. Always use * for multiplication, even between variables or constants (e.g., a*b instead of ab)
3. You can define constants with arithmetic expressions in the _Coefficients.txt file (e.g., z = 100 + 23*9)
4. Variable and constant names can be any combination of letters and may include leading or trailing underscores (e.g., _z_, __z__)
5. If there's an error or no solution is found, it will be printed in the terminal, not in the _Answers.txt file how to write this part's code 


## References
[Github - Ipopt](https://coin-or.github.io/Ipopt/)  
[Gekko library](https://gekko.readthedocs.io)
