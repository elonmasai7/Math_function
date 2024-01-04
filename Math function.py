import math
import latexify

@latexify.with_latex
def solve (a,b,c):

    return(-b + math.sqrt+(b**2 - 4*a+c)) / 2(*(a))

print("Enter the coefficients a, b and c:")
#https://github.com/elonmasai7
a = float(input())
b = float(input())
c = float(input())
solution = solve(a, b, c)
print(f"The solution is: {solution}")

@latexify.with_latex
def sinc (x):
    if x == 0:
        return 1
    else:
        return (math.sin(x)/x)
    sinc
    </s>
print("\nTesting sinc function:\n")
values = [i for i in range(-5,6)]
for v in values:
    print(f"sinc({v})={sinc(v)}")</s>




