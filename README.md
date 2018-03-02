#Tightloop
##A Challenge to Solve Simple Problems Fast

        produce functions to solve a test in any way
        must have the same result as the reference
        need not be the same algorithm as the reference

The first challenges are:

  - checksum a list
  - sort a list
  - shuffle the numbers 0..n-1

The only restriction on the way problems are solved is that problems must
produce the same checksum as the reference (ref) implementation.  Further, to
defeat caching results, an int is passed to each solution to seed a
pseudo-random number generator.  Further, the generator must produce the same
numbers as the ref.  see [ref.h|ref.h] for the
generator.

There are seven types used in the tests.  The tests are run on linux, so it's
known that these are:


| Type          | sizeof  | typedef |alias |
|:------------- |:-------:|:--------|:----:|
| char          | 1       | int8_t  | G    |
| short         | 2       | int16_t | H    |
| int           | 4       | int32_t | I    |
| long long     | 8       | int64_t | J    |
| float         | 4       |         | E    |
| double        | 8       |         | F    |
| pointer       | 8       |         | *    |




## Test 0

Find the BSD checksum for a random sequence of ints.

The sequence of random numbers must be identical to the sequence produced by
the ref with given seed.

## Test 1

Sort a list.

Using the generator, sort the sequence and return the BSD checksum of the
sorted list.

## Test 2

Shuffle the numbers 0..n using the Fisher–Yates shuffle

Again, use the generator for the shuffle.
