from dilipy.dilithium import *
msg = b"Signed by dilithium"
pk, sk, s1, s2, A, t1, t0 = Dilithium2.keygen()
sig, c, z, y, w, w0, w1 = Dilithium2.sign(sk, msg)
check_verify, Az_minus_ct1, w_prime = Dilithium2.verify(pk, msg, sig)