Rule of divisor by three
########################

.. TODO: find out how to use math formulas

:status: draft

Maybe many of you already know this simple trick to check if a number
is divisible by three.

If summing up all the digits from a number sums up to a multiple of 3
then the number is divisible by three.

For example:

- 57 -> 5 + 7 = 12, 12 is divisible by 3 thus 57 is divisible by 3
- 23 -> 2 + 4 = 5, 5 is not divisible by 3 thus 23 is not divisible by 3

There are many similar tricks to check other divisors, but to me it's
more interesting to know *why* it works, and *how* can I actually
prove it.

Looks like it's easier than I thought.  First observe that every
natural number can be written as:

n = 10^n*x_n + 10^(n-1)x_(n-1) + .. + 10x1 + x0

this representation makes it easy to compute the sum of the digits,
which is simply the sum of all x_i for i 0 -> n.

So proving for n = 0 is trivial, because 3, 6 and 9 are divisible by 3.

Suppose the number has 2 digits, so can be written as

n = 10a + b

saying that the sum of the digits is divisible by three means that
a + b % 3 = 0

