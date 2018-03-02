//j0: prng state or seed
static long long j0=-314159; 

//seed: set the seed for prng
static void seed(int s) {
  j0=s;
}

//prng: a pseudo random number generator
static inline int prng() {
  return j0=4294957665L*j0+(j0>>32);
}
