# CMPS 2200 Assignment 02
## Answers

**Name:**_Srikanya Balaji Garuda__


Place all written answers from `assignment-02.md` here for easier grading.

1. **Asymptotic notation**

    a) $T(n)=2T(n/3)+1$
.  
Level 0: 1
Level 1: 2
Level 2: $2^2$
Level i: $2^i$

Work increases, recurrence is leaf-denominated

Cost of leaf: 1, Number of leaves: $2^(\log_3 n)$ = $n^\log_3 2$

W(n) = O($n^\log_3 2$)
.  
.   
.  
    b) $T(n)=5T(n/4)+n$

Level 0: n
Level 1: 5*(n/4)
Level 2: $5^2*(\frac{n}{4^2})$
Level i: $n*(\frac{5^i}{4^i})$

Work increases, recurrence is leaf-denominated

Cost of leaf: 1, Number of leaves: $5^(\log_4 n)$ = $n^\log_4 5$

W(n) = O($n^\log_4 5$)
.  
.  
.  
.  
    c) $T(n)=7T(n/7)+n$
.  
Level 0: n
Level 1: 7*(n/7)
Level 2: $7^2*(\frac{n}{7^2})$
Level i: $n*(\frac{7^i}{7^i})$: n

Work stays constant, work is balanced, work at each level = n

number of levels: $\log_7 n$

multiple number of levels by work per level

W(n) = O($n\log n$)
.  
.  
.  
.  
    d) $T(n)=9T(n/3)+n^2$

Level 0: $n^2$
Level 1: $9*(n/3)^2: n^2$
Level 2: $9^2*(\frac{n}{3^2})^2: n^2$
Level i: $n^2*(\frac{9^i}{(3^i)^2})$

Work stays constant, work is balanced, work at each level = $n^2$

number of levels: $\log_3 n$

multiple number of levels by work per level

W(n) = O($n^2\log n$)
.  
.  
.  
    e) $T(n)=8T(n/2)+n^3$
.  
Level 0: $n^3$
Level 1: $8*(n/2)^3: n^3$
Level 2: $8^2*(\frac{n}{2^3})^2: n^3$
Level i: $n^3*(\frac{8^i}{(2^i)^3})$

Work stays constant, work is balanced, work at each level = $n^3$

number of levels: $\log_2 n$

multiple number of levels by work per level

W(n) = O($n^3\log n$) 
.  
.  
    f) $T(n)=49T(n/25)+n^{3/2}\log n$
Level 0: $n^{3/2}\log n$
Level 1: $49*(n/25)^{3/2}\log (n/25)$
Level i: $49^i*(n/(25^i))^{3/2}\log (n/(25^i))$ = $n^(3/2)*(49/125)^i*\log (n/(25^i))$

Since the local exponent is 3/2 (from n^(3/2)), is greater than the branching factor $\log_25 49 \approx 1.21$, which defines the recursive branches, the recurrent is root dominated

W(n) = O($n^{3/2}\log n$)  
.  
.  
.  
    g) $T(n)=T(n-1)+2$
Level 0: 2
Level 1: 2
Level 2: 2
Level i: 2

Work stays constant, work is balanced, work at each level = 2

number of levels: n, since no branching

multiply number of levels by work per level
.  
W(n) = O(n)  
.  
    h) $T(n)= T(n-1)+n^c$, with $c\geq 1$

Structure: Linear recursion tree where input decreases by 1 each step.
Level i: $(n-i)^c$
Height of Tree n
Total Work: $\sum_{i=0}^{n-1} (n-i)^c = 1^c + 2^c + \dots + n^c = O(n^{c+1})$ 

(Searched this up to find faulhaber's formula for summation)
.  
.  
.  
.  
    i) $T(n)=T(\sqrt{n})+1$
Level 0 (Root): n 
Level 1: $\sqrt{n}$ 
Level 2: Size $n^{1/4}$
Level i: Size $n^{1/2^i}$ 

all work is 1, tree is balanced 

number of leaves is $\log \log n$ since, branching factor is $\log_2$'d every time

W(n) = $\log \log n$
.  
.  
.  
.  
   
2. **Algorithms Comparison**
