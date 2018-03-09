# Tightloop

## A Challenge to Code Simple Problems Efficiently

        write a program to solve a problem
        the result must by the same as the reference implementation
        the program does not have to use the same algorithm as the reference

The first challenges are:

  - checksum a list
  - sort a list
  - shuffle the numbers 0..n-1

The reference implementation (ref) has simple solutions for these three
problems.  See functions tcheck(), tsort(), tshuf() in [ref.c](ref.c).

The tests are run on linux-x64.

All programs must produce a checksum of the result for verification.  The
checksum is an int and should be written to stdout.
Further, to defeat result prediction, a seed is passed to each solution for a
pseudo-random number generator. This generator is used in every test and an
implementation can be seen here: [ref.h](ref.h).


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

Again, use the generator for the shuffle and return the checksum



## Types

There are seven types used in the tests.  On linux-x64, these are:

| Type    | sizeof  | aka     |alias |
|:------- |:-------:|:--------|:----:|
| char    | 1       | int8_t  | G    |
| short   | 2       | int16_t | H    |
| int     | 4       | int32_t | I    |
| long    | 8       | int64_t | J    |
| float   | 4       |         | E    |
| double  | 8       |         | F    |
| pointer | 8       |         | *    |


## Results

Currently jfa beats the reference implementation

    +-----+-------+
    | exe |  time |
    +-----+-------+
    | jfa | 0.144 |
    | ref | 0.178 |
    +-----+-------+

