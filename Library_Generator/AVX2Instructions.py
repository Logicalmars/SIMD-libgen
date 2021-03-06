

# Copyright (c) 2011, Hua Huang and Robert D. Cameron.
# Licensed under the Academic Free License 3.0. 

from types import *
from Utility import configure

AVX2BuiltIns = \
{
	"simd_and":\
	{
		"signature":["SIMD_type _mm256_and_si256(SIMD_type arg1, SIMD_type arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[1]],
	},
	"simd_andc":\
	{
		"signature":["SIMD_type _mm256_andnot_si256(SIMD_type arg2, SIMD_type arg1)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[1]],
	},
	"simd_or":\
	{
		"signature":["SIMD_type _mm256_or_si256(SIMD_type arg1, SIMD_type arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[1]],
	},
	"simd_xor":\
	{
		"signature":["SIMD_type _mm256_xor_si256(SIMD_type arg1, SIMD_type arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[1]],
	},	
	"simd_ifh":\
	{
		"signature":["SIMD_type _mm256_blendv_epi8(SIMD_type arg3, SIMD_type arg2, SIMD_type arg1)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type", "arg3":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[8]],
	},
	"simd_add":\
	{
		"signature":["SIMD_type _mm256_add_epi$fw$(SIMD_type arg1, SIMD_type arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[8, 16, 32, 64]],
	},
	"simd_sub":\
	{
		"signature":["t _mm256_sub_epi$fw$(t arg1, t arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[8, 16, 32, 64]],
	},

	# CAUSION: Simd umult is not exactly what we want. 
	# For _mm256_mul_epu32:
	#   Multiply the low unsigned 32-bit integers from each packed 64-bit element in a and b, 
	#   and store the unsigned 64-bit results in dst.
	"simd_umult":\
	{
		"signature":["t _mm256_mul_epu32(t arg1, t arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[32]],
	},	
	"simd_mult":\
	{
		"signature":["t _mm256_mullo_epi$fw$(t arg1, t arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[16, 32]],
	},
	"simd_eq":\
	{
		"signature":["t _mm256_cmpeq_epi$fw$(t arg1, t arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[8, 16, 32, 64]],
	},
	"simd_gt":\
	{
		"signature":["t _mm256_cmpgt_epi$fw$(t arg1, t arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[8, 16, 32, 64]],
	},
	"simd_max":\
	{
		"signature":["t _mm256_max_epi$fw$(t arg1, t arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[8, 16, 32]],
	},
	"simd_umax":\
	{
		"signature":["t _mm256_max_epu$fw$(t arg1, t arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[8, 16, 32]],
	},
	"simd_min":\
	{
		"signature":["t _mm256_min_epi$fw$(t arg1, t arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[8, 16, 32]],
	},
	"simd_umin":\
	{
		"signature":["t _mm256_min_epu$fw$(t arg1, t arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[8, 16, 32]],
	},
	"simd_srli":\
	{
		"signature":["t _mm256_srli_epi$fw$(t arg1, t sh)"],
		"args_type":{"arg1":"SIMD_type", "sh":"signed_int(32)"},
		"return_type":"SIMD_type",
		"fws":[[16, 32, 64]],
	},

	"simd_srl":\
	{
		"signature":["t _mm256_srl_epi$fw$(t arg1, __m128i shift_mask)"],
		"args_type":{"arg1":"SIMD_type", "shift_mask":"__m128i"},
		"return_type":"SIMD_type",
		"fws":[[16, 32, 64]],
	},

	"simd_slli":\
	{
		"signature":["t _mm256_slli_epi$fw$(t arg1, t sh)"],
		"args_type":{"arg1":"SIMD_type", "sh":"signed_int(32)"},
		"return_type":"SIMD_type",
		"fws":[[16, 32, 64]],
	},

	"simd_sll":\
	{
		"signature":["t _mm256_sll_epi$fw$(t arg1, t shift_mask)"],
		"args_type":{"arg1":"SIMD_type", "shift_mask":"__m128i"},
		"return_type":"SIMD_type",
		"fws":[[16, 32, 64]],
	},

	"simd_srai":\
	{
		"signature":["t _mm256_srai_epi$fw$(t arg1, t sh)"],
		"args_type":{"arg1":"SIMD_type", "sh":"signed_int(32)"},
		"return_type":"SIMD_type",
		"fws":[[16, 32]],
	},

	"simd_sra":\
	{
		"signature":["t _mm256_sra_epi$fw$(t arg1, t shift_mask)"],
		"args_type":{"arg1":"SIMD_type", "shift_mask":"__m128i"},
		"return_type":"SIMD_type",
		"fws":[[16, 32]],
	},

	"simd_constant":\
	{
		"signature":["SIMD_type _mm256_set1_epi$fw$(int val)"],
		"args_type":{"val":"signed_int(32)"},
		"return_type":"SIMD_type",
		"fws":[[8, 16, 32]],
	},
	"simd_abs":\
	{
		"signature":["t _mm256_abs_epi$fw$(t arg1)"],
		"args_type":{"arg1":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[8, 16, 32]],
	},	

	"mvmd_fill":\
	{
		"signature":["SIMD_type (SIMD_type)_mm256_set1_epi$fw$(int val1)"],
		"args_type":{"val1":"signed_int(32)"},
		"return_type":"SIMD_type",
		"fws":[[8, 16, 32]],
	},
	"mvmd_fill4":\
	{
		"signature":["SIMD_type (SIMD_type)_mm256_set_epi$fw$(int val1, int val2, int val3, int val4, int val1, int val2, int val3, int val4)"],
		"args_type":{"val1":"signed_int(32)", "val2":"signed_int(32)", "val3":"signed_int(32)", "val4":"signed_int(32)"},
		"return_type":"SIMD_type",
		"fws":[[32]],
	},
	"mvmd_fill8":\
	{
		"signature":["SIMD_type (SIMD_type)_mm256_set_epi$fw$(int val1, int val2, int val3, int val4, int val5, int val6, int val7, int val8, int val1, int val2, int val3, int val4, int val5, int val6, int val7, int val8)"],
		"args_type":{"val1":"signed_int(32)", "val2":"signed_int(32)", "val3":"signed_int(32)", "val4":"signed_int(32)", \
					"val5":"signed_int(32)", "val6":"signed_int(32)", "val7":"signed_int(32)", "val8":"signed_int(32)"},
		"return_type":"SIMD_type",
		"fws":[[16]],
	},
	"mvmd_fill16":\
	{
		"signature":["SIMD_type (SIMD_type)_mm256_set_epi$fw$(int val1, int val2, int val3, int val4, int val5, int val6, int val7, int val8, int val9, int val10, int val11, int val12, int val13, int val14, int val15, int val16, int val1, int val2, int val3, int val4, int val5, int val6, int val7, int val8, int val9, int val10, int val11, int val12, int val13, int val14, int val15, int val16)"],
		"args_type":{"val1":"signed_int(32)", "val2":"signed_int(32)", "val3":"signed_int(32)", "val4":"signed_int(32)", \
					"val5":"signed_int(32)", "val6":"signed_int(32)", "val7":"signed_int(32)", "val8":"signed_int(32)", \
					"val9":"signed_int(32)", "val10":"signed_int(32)", "val11":"signed_int(32)", "val12":"signed_int(32)", \
					"val13":"signed_int(32)", "val14":"signed_int(32)", "val15":"signed_int(32)", "val16":"signed_int(32)"},
		"return_type":"SIMD_type",
		"fws":[[8]],
	},
	"bitblock_load_aligned":\
	{
		"signature":["SIMD_type _mm256_load_si256(SIMD_type* arg1)"],
		"args_type":{"arg1":"SIMD_type*"},
		"return_type":"SIMD_type",
		"fws":[[256]],
	},
	"bitblock_store_aligned":\
	{
		"signature":["void _mm256_store_si256(SIMD_type* arg2, SIMD_type arg1)"],
		"args_type":{"arg2":"SIMD_type*", "arg1":"SIMD_type"},
		"return_type":"void",
		"fws":[[256]],
	},
	"bitblock_load_unaligned":\
	{
		"signature":["SIMD_type _mm256_loadu_si256(SIMD_type* arg1)"],
		"args_type":{"arg1":"SIMD_type*"},
		"return_type":"SIMD_type",
		"fws":[[256]],
	},
	"bitblock_store_unaligned":\
	{
		"signature":["void _mm256_storeu_si256(SIMD_type* arg2, SIMD_type arg1)"],
		"args_type":{"arg2":"SIMD_type*", "arg1":"SIMD_type"},
		"return_type":"void",
		"fws":[[256]],
	},

	"hsimd_signmask":\
	{
		"signature":["int _mm256_movemask_epi8(SIMD_type arg1)"],
		"args_type":{"arg1":"SIMD_type"},
		"return_type":"int",
		"fws":[[8]],	
	},

	"_mm256_movemask_pd":\
	{
		"signature":["t _mm256_movemask_pd(t arg1)"],
		"args_type":{"arg1":"__m256d"},
		"return_type":"int",
		"fws":[[64]],
	},

	"_mm256_movemask_ps":\
	{
		"signature":["t _mm256_movemask_ps(t arg1)"],
		"args_type":{"arg1":"__m256"},
		"return_type":"int",
		"fws":[[32]],
	},

	"_mm256_castsi256_pd":\
	{
		"signature":["t _mm256_castsi256_pd(t arg1)"],
		"args_type":{"arg1":"SIMD_type"},
		"return_type":"__m256d",
		"fws":[[256]],
	},

	"_mm256_castsi256_ps":\
	{
		"signature":["t _mm256_castsi256_ps(t arg1)"],
		"args_type":{"arg1":"SIMD_type"},
		"return_type":"__m256",
		"fws":[[256]],
	},

	"_mm256_srl_epi64":\
	{
		"signature":["t _mm256_srl_epi64(t arg1, t arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"__m128i"},
		"return_type":"SIMD_type",
		"fws":[[64]],
	},

	"_mm256_sll_epi64":\
	{
		"signature":["t _mm256_sll_epi64(t arg1, t arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"__m128i"},
		"return_type":"SIMD_type",
		"fws":[[64]],
	},

	"_mm256_packs_epi16":\
	{
		"signature":["t _mm256_packs_epi16(t arg1, t arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[16]],
	},

	"_mm256_packs_epi32":\
	{
		"signature":["t _mm256_packs_epi32(t arg1, t arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[32]],
	},

	"_mm256_packus_epi16":\
	{
		"signature":["t _mm256_packus_epi16(t arg1, t arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[16]],
	},

	"_mm256_packus_epi32":\
	{
		"signature":["t _mm256_packus_epi32(t arg1, t arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[32]],
	},

	"_mm256_hadd_epi16":\
	{
		"signature":["t _mm256_hadd_epi16(t arg1, t arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[16]],
	},

	"_mm256_hadd_epi32":\
	{
		"signature":["t _mm256_hadd_epi32(t arg1, t arg2)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type"},
		"return_type":"SIMD_type",
		"fws":[[32]],
	},

	"_mm256_permute2x128_si256":\
	{
		"signature":["t _mm256_permute2x128_si256(t arg1, t arg2, t imm)"],
		"args_type":{"arg1":"SIMD_type", "arg2":"SIMD_type", "imm":"signed_int(32)"},
		"return_type":"SIMD_type",
		"fws":[[256]],
	},

	"_mm256_set_epi32":\
	{
		"signature":["SIMD_type _mm256_set_epi32(int val1, int val2, int val3, int val4, int val5, int val6, int val7, int val8)"],
		"args_type":{"val1":"signed_int(32)", "val2":"signed_int(32)", "val3":"signed_int(32)", "val4":"signed_int(32)", \
					"val5":"signed_int(32)", "val6":"signed_int(32)", "val7":"signed_int(32)", "val8":"signed_int(32)"},
		"return_type":"SIMD_type",
		"fws":[[32]],
	},
	"_mm256_castsi128_si256":\
	{
		"signature":["SIMD_type _mm256_castsi128_si256(__m128i arg1)"],
		"args_type":{"arg1":"__m128i"},
		"return_type":"SIMD_type",
		"fws":[[256]],
	},
	"_mm_cvtsi64_si128":\
	{
		"signature":["__m128i _mm_cvtsi64_si128(t arg1)"],
		"args_type":{"arg1":"signed_int(64)"},
		"return_type":"__m128i",
		"fws":[[128]],
	},
	"_mm_sad_epu8":\
	{
		"signature":["__m128i _mm_sad_epu8(__m128i arg1, __m128i arg2)"],
		"args_type":{"arg1":"__m128i", "arg2":"__m128i"},
		"return_type":"__m128i",
		"fws":[[8]],
	},
	"_mm_set1_epi32":\
	{
		"signature":["__m128i _mm_set1_epi32(int val1)"],
		"args_type":{"val1":"signed_int(32)"},
		"return_type":"__m128i",
		"fws":[[32]],
	},
	"_mm_extract_epi8":\
	{
		"signature":["int _mm_extract_epi8(__m128i arg1, int pos)"],
		"args_type":{"arg1":"__m128i", "pos":"signed_int(32)"},
		"return_type":"signed_int(32)",
		"fws":[[8]],
	},
	"_mm_extract_epi16":\
	{
		"signature":["int _mm_extract_epi16(__m128i arg1, int pos)"],
		"args_type":{"arg1":"__m128i", "pos":"signed_int(32)"},
		"return_type":"signed_int(32)",
		"fws":[[16]],
	},
	"_mm_extract_epi32":\
	{
		"signature":["int _mm_extract_epi32(__m128i arg1, int pos)"],
		"args_type":{"arg1":"__m128i", "pos":"signed_int(32)"},
		"return_type":"signed_int(32)",
		"fws":[[32]],
	},
	"_mm256_testz_si256":\
	{
		"signature":["int _mm256_testz_si256(SIMD_type arg1, SIMD_type arg1)"],
		"args_type":{"arg1":"SIMD_type"},
		"return_type":"signed_int(32)",
		"fws":[[256]],
	},
	"_mm_movemask_epi8":\
	{
		"signature":["int _mm_movemask_epi8(__m128i arg1)"],
		"args_type":{"arg1":"__m128i"},
		"return_type":"signed_int(32)",
		"fws":[[8]],
	},
	"_mm_unpackhi_epi8":\
	{
		"signature":["__m128i _mm_unpackhi_epi8(__m128i arg2, __m128i arg1)"],
		"args_type":{"arg1":"__m128i", "arg2":"__m128i"},
		"return_type":"__m128i",
		"fws":[[8]],
	},
	"_mm_unpackhi_epi16":\
	{
		"signature":["__m128i _mm_unpackhi_epi16(__m128i arg2, __m128i arg1)"],
		"args_type":{"arg1":"__m128i", "arg2":"__m128i"},
		"return_type":"__m128i",
		"fws":[[16]],
	},
	"_mm_unpackhi_epi32":\
	{
		"signature":["__m128i _mm_unpackhi_epi32(__m128i arg2, __m128i arg1)"],
		"args_type":{"arg1":"__m128i", "arg2":"__m128i"},
		"return_type":"__m128i",
		"fws":[[32]],
	},
	"_mm_unpackhi_epi64":\
	{
		"signature":["__m128i _mm_unpackhi_epi64(__m128i arg2, __m128i arg1)"],
		"args_type":{"arg1":"__m128i", "arg2":"__m128i"},
		"return_type":"__m128i",
		"fws":[[64]],
	},
	"_mm_unpacklo_epi8":\
	{
		"signature":["__m128i _mm_unpacklo_epi8(__m128i arg2, __m128i arg1)"],
		"args_type":{"arg1":"__m128i", "arg2":"__m128i"},
		"return_type":"__m128i",
		"fws":[[8]],
	},
	"_mm_unpacklo_epi16":\
	{
		"signature":["__m128i _mm_unpacklo_epi16(__m128i arg2, __m128i arg1)"],
		"args_type":{"arg1":"__m128i", "arg2":"__m128i"},
		"return_type":"__m128i",
		"fws":[[16]],
	},
	"_mm_unpacklo_epi32":\
	{
		"signature":["__m128i _mm_unpacklo_epi32(__m128i arg2, __m128i arg1)"],
		"args_type":{"arg1":"__m128i", "arg2":"__m128i"},
		"return_type":"__m128i",
		"fws":[[32]],
	},
	"_mm_unpacklo_epi64":\
	{
		"signature":["__m128i _mm_unpacklo_epi64(__m128i arg2, __m128i arg1)"],
		"args_type":{"arg1":"__m128i", "arg2":"__m128i"},
		"return_type":"__m128i",
		"fws":[[64]],
	},

	"_mm_cvtsi32_si128":\
	{
		"signature":["__m128i _mm_cvtsi32_si128(int arg1)"],
		"args_type":{"arg1":"signed_int(32)"},
		"return_type":"__m128i",
		"fws":[[128]],
	},	

	"_mm_cvtsi128_si32":\
	{
		"signature":["int _mm_cvtsi128_si32(__m128i arg1)"],
		"args_type":{"arg1":"__m128i"},
		"return_type":"uint32_t",
		"fws":[[128]],
	},	

	"_mm256_srl_epi64":\
	{
		"signature":["SIMD_type _mm256_srl_epi64(SIMD_type arg1, __m128i sh)"],
		"args_type":{"arg1":"SIMD_type", "sh":"__m128i"},
		"return_type":"SIMD_type",
		"fws":[[256]],
	},	

	"_mm256_permute4x64_epi64":\
	{
		"signature":["SIMD_type _mm256_permute4x64_epi64(SIMD_type arg1, int sh)"],
		"args_type":{"arg1":"SIMD_type", "sh":"signed_int(32)"},
		"return_type":"SIMD_type",
		"fws":[[256]],
	},	

	"_mm256_set_epi64x":\
	{
		"signature":["SIMD_type _mm256_set_epi64x(t arg1, t arg2, t arg3, t arg4)"],
		"args_type":{"arg1":"signed_int(64)", "arg2":"signed_int(64)", "arg3":"signed_int(64)", "arg4":"signed_int(64)"},
		"return_type":"SIMD_type",
		"fws":[[256]],
	},		

	"__builtin_popcountll":\
	{
		"signature":["int __builtin_popcountll(t arg1)"],
		"args_type":{"arg1":"unsigned_int(64)"},
		"return_type":"int",
		"fws":[[256]],
	},

	"_mm_insert_epi16":\
	{
		"signature":["__m128i _mm_insert_epi16(t arg1, t i, t imm)"],
		"args_type":{"arg1":"__m128i", "i":"signed_int(32)", "imm":"signed_int(32)"},
		"return_type":"__m128i",
		"fws":[[16]],
	},		
}

