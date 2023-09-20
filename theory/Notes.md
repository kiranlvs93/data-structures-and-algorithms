### Types of Data Structures

* Physical DS - Array, List
* Logical DS - Hash, Stack, Graph, Queues, Tress

### Big O Notation

* This is used to measure the time or space complexity
* Time complexity is the measure of time taken for algorithms to execute with the increase in input size
* O(1) - Constant time complexity - The execution time is constant irrespective of the input size. This is best time
  complexity
* O(N) - Linear time complexity - The execution time is proportional to the input size.
* O(N^2) - The execution time increases exponentially with the increase in input size.

### Asymptotic analysis : Study of behaviour of a function f(N) as N tends to infinity
So, the below is true in asymptotic analysis, because as N tends to infinity, N and 1 become insignificant compared to
N^2

`O(N^2+N+1) = O(N^2)`

Few *common complexities* (both time and space) in the increasing order are below:

* O(1) - Constant time (Best complexity)
* O(log(N)) - Logarithmic time
* O(N) - Linear time
* O(Nlog(N)) - N * Logarithmic time
* O(N^2) - Quadratic
* O(N^3) - Quadratic
* O(N^4) - Quadratic
* O(2^N) - Exponential
* O(N!) - Factorial (Worst complexity)

However, when there are two variables say M and N, we need to preserve both the variables.

* O(N + M) != O(N)
* O(N^2 + 2M) = O(N^2 + M)
  * Dropped 2, as 2 is insignificant compared to M, 
  * But we need to preserve M
* O(N! + log(M) + 2N + 3) = O(N! + log(M)) 
  * Dropped 2N as its insignificant compared to M
  * Dropped 3 as its constant and insignificant compared to other complexities 

An algorithm would have `best, average or worst case` scenarios, depending on the input order, but the complexity is
always denoted in worst case scenario

### Logarithm
In computer science, logarithm is always to the base of 2 i.e., `BINARY LOGARITHM`.


### Hash Table
* Time complexity - O(1) - Search and write operations (insertion and deletion) in a hash table are of constant
* Space complexity - O(N) - As the space depends on number of elements stored 
* Hash tables are built on dynamic array of linked lists
* All keys are derived from the ASCII
* E.g., ASCII value of FOO - 70+79+79 = 228 and then a hashing function is used to map them to indices
* Collision in hash table refers to a condition where two keys have same ASCII value. In this case, the keys are stored
as LinkedList.
* To avoid the collision, powerful hashing algorithms are developed such that the hashed keys are always unique
* So, best time complexity - O(1) and worst time complexity - O(N) in case of collision
* Resizing - Hash tables are resized as the number of keys to be stored increase

