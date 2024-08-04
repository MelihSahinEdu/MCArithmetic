"""
Copyright 2023 Melih Şahin

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from zero_order_encoding_without_EOF import *

chars=['A','T','C','G'] # last character is the end-of-file symbol, in our case "d"
rates= [0.27,0.26,0.24,0.23] # rates of the chars in order
bit_precision=20
dict, c, d=zero_order_dict_c_d_returner(chars, rates.copy(), bit_precision)

exemplary_word="GTAACGTAGTATTATGTAAA"

arithmetic_encoding=get_the_arithmetic_encoding_of_a_word_without_eof(exemplary_word, chars, rates, bit_precision,dict,c,d)
decoded_word=decode_zero_order_encoding_without_eof(bit_precision, arithmetic_encoding, dict,c,d,chars)

print("print True if can be encoded by MoAC")
print(word_arithmetic_coder_suitability_checker_without_eof(exemplary_word,arithmetic_encoding,bit_precision,dict,c,d,chars))

print("encoded word is "+exemplary_word)
print("its encoding is: ")
print(arithmetic_encoding)
print("its decoding is: "+ decoded_word)
print("Do original and resultant words match:")
print(decoded_word==exemplary_word)
