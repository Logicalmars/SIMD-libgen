#ifndef LLVM_HEADER_H
#define LLVM_HEADER_H

#ifndef USE_SSE
typedef int SIMD_type __attribute__((__vector_size__(16)));
#endif

extern "C" {
SIMD_type llvm_add_8(SIMD_type a, SIMD_type b);
SIMD_type llvm_add_16(SIMD_type a, SIMD_type b);
SIMD_type llvm_add_32(SIMD_type a, SIMD_type b);
SIMD_type llvm_add_64(SIMD_type a, SIMD_type b);
SIMD_type llvm_add_128(SIMD_type a, SIMD_type b);
SIMD_type llvm_sub_8(SIMD_type a, SIMD_type b);
SIMD_type llvm_sub_16(SIMD_type a, SIMD_type b);
SIMD_type llvm_sub_32(SIMD_type a, SIMD_type b);
SIMD_type llvm_sub_64(SIMD_type a, SIMD_type b);
SIMD_type llvm_sub_128(SIMD_type a, SIMD_type b);
SIMD_type llvm_mul_8(SIMD_type a, SIMD_type b);
SIMD_type llvm_mul_16(SIMD_type a, SIMD_type b);
SIMD_type llvm_mul_32(SIMD_type a, SIMD_type b);
SIMD_type llvm_mul_64(SIMD_type a, SIMD_type b);
SIMD_type llvm_and_8(SIMD_type a, SIMD_type b);
SIMD_type llvm_and_16(SIMD_type a, SIMD_type b);
SIMD_type llvm_and_32(SIMD_type a, SIMD_type b);
SIMD_type llvm_and_64(SIMD_type a, SIMD_type b);
SIMD_type llvm_and_128(SIMD_type a, SIMD_type b);
SIMD_type llvm_or_8(SIMD_type a, SIMD_type b);
SIMD_type llvm_or_16(SIMD_type a, SIMD_type b);
SIMD_type llvm_or_32(SIMD_type a, SIMD_type b);
SIMD_type llvm_or_64(SIMD_type a, SIMD_type b);
SIMD_type llvm_or_128(SIMD_type a, SIMD_type b);
SIMD_type llvm_xor_8(SIMD_type a, SIMD_type b);
SIMD_type llvm_xor_16(SIMD_type a, SIMD_type b);
SIMD_type llvm_xor_32(SIMD_type a, SIMD_type b);
SIMD_type llvm_xor_64(SIMD_type a, SIMD_type b);
SIMD_type llvm_xor_128(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_eq_8(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_eq_16(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_eq_32(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_eq_64(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_eq_128(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_sgt_8(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_sgt_16(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_sgt_32(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_sgt_64(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_sgt_128(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_ugt_8(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_ugt_16(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_ugt_32(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_ugt_64(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_ugt_128(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_slt_8(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_slt_16(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_slt_32(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_slt_64(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_slt_128(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_ult_8(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_ult_16(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_ult_32(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_ult_64(SIMD_type a, SIMD_type b);
SIMD_type llvm_icmp_ult_128(SIMD_type a, SIMD_type b);
SIMD_type llvm_shl_8(SIMD_type a, SIMD_type b);
SIMD_type llvm_shl_16(SIMD_type a, SIMD_type b);
SIMD_type llvm_shl_32(SIMD_type a, SIMD_type b);
SIMD_type llvm_lshr_8(SIMD_type a, SIMD_type b);
SIMD_type llvm_lshr_16(SIMD_type a, SIMD_type b);
SIMD_type llvm_lshr_32(SIMD_type a, SIMD_type b);
SIMD_type llvm_ashr_8(SIMD_type a, SIMD_type b);
SIMD_type llvm_ashr_16(SIMD_type a, SIMD_type b);
SIMD_type llvm_ashr_32(SIMD_type a, SIMD_type b);
SIMD_type llvm_ashr_64(SIMD_type a, SIMD_type b);
int llvm_extractelement_32(SIMD_type a, int idx);
short llvm_extractelement_16(SIMD_type a, int idx);
long long llvm_extractelement_64(SIMD_type a, int idx);
SIMD_type llvm_insertelement_32(SIMD_type a, int val, int idx);
SIMD_type llvm_insertelement_16(SIMD_type a, short val, int idx);
SIMD_type llvm_insertelement_64(SIMD_type a, long long val, int idx);
SIMD_type llvm_load_aligned(SIMD_type *a);
SIMD_type llvm_load_unaligned(SIMD_type *a);
void llvm_store_aligned(SIMD_type a, SIMD_type *addr);
void llvm_store_unaligned(SIMD_type a, SIMD_type *addr);
SIMD_type llvm_ifh_8(SIMD_type mask, SIMD_type a, SIMD_type b);
SIMD_type llvm_ifh_16(SIMD_type mask, SIMD_type a, SIMD_type b);
SIMD_type llvm_ifh_32(SIMD_type mask, SIMD_type a, SIMD_type b);
SIMD_type llvm_ifh_64(SIMD_type mask, SIMD_type a, SIMD_type b);
SIMD_type llvm_ifh_128(SIMD_type mask, SIMD_type a, SIMD_type b);
SIMD_type llvm_constant_32(int val);
SIMD_type llvm_constant_16(short val);
SIMD_type llvm_constant_64(long long val);
}
#endif //LLVM_HEADER_H
