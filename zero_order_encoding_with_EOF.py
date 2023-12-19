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


main_condition=False


golden_ratio=0.6180339887498948482045868343656381177203091798057628621354486227

def one_time_last_character_encoder_MC( whole,s,a,b,altta_0_mı_var,ustte_1_mi_var,s_üst,s_alt  ):
    half = whole / 2


    zero_length = round(golden_ratio * whole)
    one_length = whole - zero_length

    emit = []

    while (True):

        if (s>0):
            if ((not altta_0_mı_var) and (not ustte_1_mi_var)):

                if ((a==0 and b>=one_length) or (b==whole and a<one_length)):
                    if ((b==whole and a<one_length)):
                        emit.append(s_üst)

                        for t in range(s - 1):
                            emit.append(0)



                        emit.append(0)
                        break

                    if ((a==0 and b>=one_length)):
                        emit.append(s_alt)

                        new_commute = 1
                        if (s_alt == 1):
                            new_commute = 0

                        for t in range(s - 1):
                            if (t % 2 == 0):
                                emit.append(new_commute)


                            else:
                                emit.append(s_alt)

                        emit.append(1)
                        emit.append(0)
                        break


                else:
                    a_nın = one_length - a
                    b_nin = b - one_length

                    if (a_nın>=b_nin):
                        emit.append(s_alt)

                        new_commute = 1
                        if (s_alt == 1):
                            new_commute = 0

                        for t in range(s - 1):
                            if (t % 2 == 0):
                                emit.append(new_commute)


                            else:
                                emit.append(s_alt)

                        emit.append(1)
                        emit.append(0)

                        s = 0

                        b = whole
                        a = int((a*whole)/one_length)

                        if (a>=zero_length):
                            emit.append(1)
                            emit.append(0)
                            break

                    else:
                        emit.append(s_üst)

                        for t in range(s - 1):
                            emit.append(0)

                        s = 0

                        emit.append(0)

                        a = 0
                        b = int(((b-one_length)*whole)/((whole-one_length)))

                        if (b<zero_length):
                            emit.append(0)
                            break


                    altta_0_mı_var = True
                    ustte_1_mi_var = True

            elif (altta_0_mı_var and (not ustte_1_mi_var)):

                if (a==0 and b>=half) or (b==whole and a<half):
                    if (b==whole and a<half):
                        emit.append(s_üst)

                        for t in range(s - 1):
                            emit.append(0)
                        emit.append(0)
                        break


                    else:
                        emit.append(s_alt)

                        new_commute = 1
                        if (s_alt == 1):
                            new_commute = 0

                        for t in range(s - 1):
                            if (t % 2 == 0):
                                emit.append(new_commute)


                            else:
                                emit.append(s_alt)

                        emit.append(0)
                        break

                else:

                    a_nın = half - a
                    b_nin = b - half

                    if (a_nın >= b_nin):
                        emit.append(s_alt)

                        new_commute = 1
                        if (s_alt == 1):
                            new_commute = 0

                        for t in range(s - 1):
                            if (t % 2 == 0):
                                emit.append(new_commute)


                            else:
                                emit.append(s_alt)

                        emit.append(0)
                        s = 0

                        a=2*a
                        b=whole
                    else:
                        emit.append(s_üst)

                        for t in range(s - 1):
                            emit.append(0)

                        s = 0

                        emit.append(0)

                        a=0
                        b=int((b-half)*2)

                    altta_0_mı_var = True
                    ustte_1_mi_var = True





        else: # s is 0


            if (altta_0_mı_var and ustte_1_mi_var):
                if ((a==0 and b>=zero_length) or (b==whole and a<zero_length)):

                    if (b==whole and a<zero_length):
                        emit.append(1)
                        emit.append(0)
                        break

                    else:
                        emit.append(0)
                        break

                else:


                    a_nın=zero_length-a
                    b_nin=b-zero_length



                    if (a_nın>=b_nin):
                        emit.append(0)
                        b=whole
                        a=int((a*whole)/one_length)

                    else:


                        emit.append(1)
                        emit.append(0)
                        a=0
                        b=int(((b-one_length)*whole)/one_length)





            elif ((not altta_0_mı_var) and (not ustte_1_mi_var)):
                if (a==0 and b>=one_length) or (b==whole and a<one_length):
                    if  (b==whole and a<one_length):
                        emit.append(0)
                        break


                    else:
                        emit.append(1)
                        emit.append(0)
                        break

                else:

                    a_nın=one_length-a
                    b_nin=b-one_length

                    if (a_nın>=b_nin):

                        emit.append(1)
                        emit.append(0)
                        b = whole
                        a = int((a * whole) / zero_length)

                    else:
                        emit.append(0)

                        a=0
                        b = int(((b - zero_length) * whole) / zero_length)

                    altta_0_mı_var=True
                    ustte_1_mi_var=True



            elif (altta_0_mı_var and (not ustte_1_mi_var)):
                if (a==0 and b>=half) or (b==whole and a<half):
                    if (a==0 and b>=half):
                        emit.append(0)
                        break
                    else:
                        emit.append(0)
                        break
                else:

                    a_nın=half-a
                    b_nin=b-half

                    if (a_nın>=b_nin):
                        emit.append(0)
                        a = 2 * a
                        b = whole

                    else:
                        emit.append(0)

                        a = 0
                        b = int((b - half) * 2)

                    altta_0_mı_var=True
                    ustte_1_mi_var=True
    return emit

def one_time_encoder_MC( whole, c, d, dict,s,a,b,the_character,altta_0_mı_var,ustte_1_mi_var,s_üst,s_alt  ):

    half=whole/2
    zero_length = round(golden_ratio * whole)
    one_length = whole - zero_length

    emit=[]


    s_teki_artış=0
    saf_artış=0

    if (True):




        our_char=the_character
        word_number=dict[our_char]

        w = b - a
        fake_a = a
        a = a + int((c[word_number] * w) / whole)
        b = fake_a + int((d[word_number] * w) / whole)


        if (s==0):

            if ((not altta_0_mı_var) and (not ustte_1_mi_var)):
                if (b<one_length or a>=one_length):
                    if (b<one_length):
                        emit.append(1)
                        emit.append(0)
                        saf_artış+=2

                        a=int((a*(whole))/one_length)
                        b=int((b*(whole))/one_length)



                    else:
                        emit.append(0)
                        saf_artış += 1
                        a=int(((a-one_length)*(zero_length))/one_length)
                        b=int(((b-one_length)*(zero_length))/one_length)




                    altta_0_mı_var=True
                    ustte_1_mi_var=True

            if (altta_0_mı_var and not ustte_1_mi_var): # alt üst ikisi de 0
                if (b<half):
                    emit.append(0)
                    saf_artış += 1

                    a=2*a
                    b=2*b

                    altta_0_mı_var=True
                    ustte_1_mi_var=True

                if (a>=half):
                    emit.append(0)
                    saf_artış += 1

                    a=2*(a-half)
                    b=2*(b-half)

                    altta_0_mı_var=True
                    ustte_1_mi_var=True

            if (altta_0_mı_var and ustte_1_mi_var):
                while (b<zero_length or a>=zero_length):
                    if (b<zero_length):
                        emit.append(0)
                        saf_artış += 1
                        a = int((a * (whole)) / zero_length)
                        b = int((b * (whole)) / zero_length)


                    else:
                        emit.append(1)
                        emit.append(0)
                        saf_artış += 1
                        saf_artış += 1
                        a=int(((a-zero_length)*(whole))/one_length)
                        b=int(((b-zero_length)*(whole))/one_length)


        if (s>0):
            if (altta_0_mı_var and ustte_1_mi_var):
                # buraya gelmesi mantıken imkansız
                pass


            if ((not altta_0_mı_var) and (not ustte_1_mi_var)):
                if (b<one_length or a>=one_length):
                    if (b<one_length):

                        a=int((a*(whole))/one_length)
                        b=int((b*(whole))/one_length)



                        emit.append(s_alt)

                        new_commute=1
                        if (s_alt==1):
                            new_commute=0


                        for t in range(s-1):
                            if (t % 2 == 0):
                                emit.append(new_commute)


                            else:
                                 emit.append(s_alt)




                        emit.append(1)
                        emit.append(0)
                        saf_artış += 1
                        saf_artış += 1
                        s=0


                    else: #üste gelirse 0000

                        emit.append(s_üst)

                        for t in range(s-1):
                            emit.append(0)


                        s=0


                        emit.append(0)
                        saf_artış += 1

                        a=int(((a-one_length)*(zero_length))/one_length)
                        b=int(((b-one_length)*(zero_length))/one_length)



                    altta_0_mı_var=True
                    ustte_1_mi_var=True

            if (altta_0_mı_var and (not ustte_1_mi_var)): # alt üst ikisi de 0
                if (b<half): #alt

                    emit.append(s_alt)

                    new_commute=1
                    if (s_alt==1):
                        new_commute=0


                    for t in range(s-1):
                        if (t % 2 == 0):
                            emit.append(new_commute)


                        else:
                            emit.append(s_alt)




                    emit.append(0)
                    saf_artış += 1
                    s=0

                    a=2*a
                    b=2*b

                    altta_0_mı_var=True
                    ustte_1_mi_var=True

                elif (a>=half): #üst
                    emit.append(s_üst)

                    for t in range(s-1):
                        emit.append(0)


                    s=0

                    emit.append(0)
                    saf_artış += 1

                    a=2*(a-half)
                    b=2*(b-half)

                    altta_0_mı_var=True
                    ustte_1_mi_var=True

            if (altta_0_mı_var and ustte_1_mi_var):
                while (b<zero_length or a>=zero_length):
                    if (b<zero_length):
                        emit.append(0)
                        saf_artış += 1
                        a = int((a * (whole)) / zero_length)
                        b = int((b * (whole)) / zero_length)


                    else:
                        emit.append(1)
                        emit.append(0)
                        saf_artış += 1
                        saf_artış += 1
                        a=int(((a-zero_length)*(whole))/one_length)
                        b=int(((b-zero_length)*(whole))/one_length)


        # phi:=1/golden_ratio
        condition = True
        while (condition):
            if (altta_0_mı_var and ustte_1_mi_var):
                special_number=int((whole*golden_ratio)*golden_ratio) # 648056=whole*phi*phi
                if (a >= special_number):  # 648056=whole*phi*phi
                    condition = True
                    a = int(((a - special_number) * (whole)) / (whole - special_number))
                    b = int(((b - special_number) * (whole)) / (whole - special_number))

                    if (s == 0):
                        s_üst = 1
                        s_alt = 0

                    s += 1
                    s_teki_artış+=1

                    altta_0_mı_var = False
                    ustte_1_mi_var = False


                else:
                    condition = False

            if ((not altta_0_mı_var) and (not ustte_1_mi_var)):
                special_number_1 = round((whole * 2 * golden_ratio) * golden_ratio)  # 801041=whole*(2*(phi*phi))
                if (b < special_number_1):  # 801041=whole*(2*(phi*phi))
                    a = int((a * (whole)) / special_number_1)
                    b = int((b * (whole)) / special_number_1)

                    if (s == 0):
                        s_üst = 0
                        s_alt = 1

                    s += 1
                    s_teki_artış += 1

                    altta_0_mı_var = True
                    ustte_1_mi_var = False


                else:
                    condition = False

            if (altta_0_mı_var and (not ustte_1_mi_var)):
                special_number_2 = round((whole / 2) * (1 + golden_ratio))
                special_number_3 = round((whole / 2) * golden_ratio)  # ((324028=whole/2)*phi)
                if (b < special_number_2 and a >= special_number_3):
                    condition = True
                    a = int(((a - special_number_3) * (whole)) / (whole / 2))
                    b = int(((b - special_number_3) * (whole)) / (whole / 2))

                    if (s == 0):
                        s_üst = 0
                        s_alt = 0

                    s += 1
                    s_teki_artış += 1

                    altta_0_mı_var = False
                    ustte_1_mi_var = False




                else:
                    condition = False

    return emit, s, a, b, altta_0_mı_var, ustte_1_mi_var, s_alt, s_üst, s_teki_artış,saf_artış


def decoder(whole, sequence, c, d, dict, chars, number, number_finish, altta_0_mı_var, ustte_1_mi_var,the_seqeunce, s_üst, s_alt, s, is_s_0,toplam_emit,main_condition,kaçıncı,bir_önceki_bit):
    #print(''.join(the_seqeunce))
    zero_length = round(golden_ratio * whole)
    one_length = whole - zero_length

    the_character=0



    number_finish_now=whole
    number_now=0

    j=0
    last_index=min(20,len(sequence))  # 20 can be modified

    if (len(sequence) == 0):
        return the_seqeunce, sequence

    if (altta_0_mı_var and ustte_1_mi_var):

        pass

    elif (not altta_0_mı_var and not ustte_1_mi_var):
        if sequence[0]==0:
            number_now=one_length
            j+=1
        else:
            number_finish_now=one_length
            j+=2

    elif (altta_0_mı_var and not ustte_1_mi_var):
        if bir_önceki_bit==0:
            number_now=round(whole/2)
            j+=1
        else:
            number_finish_now = round(whole / 2)
            j+=1

    while j<last_index:

        if sequence[j]==0:
            number_finish_now=number_now + round(((number_finish_now-number_now)*zero_length)/whole)
        else:
            number_now=number_now + round(((number_finish_now-number_now)*zero_length)/whole)
            j+=1
        j+=1



    final_number=(number_now+number_now)/2

    for h in range(len(chars)):
        lower_bound=int((c[dict[chars[h]]]*(number_finish-number))/whole)+number
        upper_bound=int((d[dict[chars[h]]]*(number_finish-number))/whole)+number


        if ( final_number<upper_bound): # z'nin yani number_now'ın çok düşük olduğunu farzet
            the_seqeunce.append(chars[h])
            the_character=chars[h]
            if (h==len(chars)-1): # len(chars)-1 is EOF index
                emit, s, number, number_finish, altta_0_mı_var, ustte_1_mi_var, s_alt, s_üst, s_teki_artış, saf_artış = one_time_encoder_MC(whole, c, d, dict, s, number, number_finish, the_character, altta_0_mı_var, ustte_1_mi_var, s_üst,s_alt)
                sequence = sequence[(saf_artış) + (s_teki_artış):]
                encoded=one_time_last_character_encoder_MC(whole, s, number, number_finish, altta_0_mı_var,ustte_1_mi_var, s_üst, s_alt)
                sequence=sequence[len(encoded)-s_teki_artış:]
                return the_seqeunce, sequence
            break
        if h==len(chars)-1: # şu anki durumuyla buraya asla gelmeyecek,
            #print("hata")
            return the_seqeunce, sequence # hata çıktı

    emit, s, number, number_finish,  altta_0_mı_var, ustte_1_mi_var, s_alt, s_üst,s_teki_artış,saf_artış=one_time_encoder_MC( whole, c, d, dict,s,number,number_finish,the_character,altta_0_mı_var,ustte_1_mi_var,s_üst,s_alt)
    if ((saf_artış+s_teki_artış)>0):
        if ((saf_artış)+(s_teki_artış)-1>=len(sequence)):
            pass
        else:
            bir_önceki_bit=sequence[(saf_artış)+(s_teki_artış)-1]
    sequence = sequence[(saf_artış)+(s_teki_artış):]


    kaçıncı+=1
    return decoder(whole, sequence, c, d, dict, chars, number, number_finish, altta_0_mı_var, ustte_1_mi_var,the_seqeunce, s_üst, s_alt, s, s==0,toplam_emit,main_condition,kaçıncı,bir_önceki_bit)

def zero_order_encoder_MC_with_eof( whole, word, c, d, dict):
    a=0
    b=whole
    s=0
    altta_0_mı_var=True
    ustte_1_mi_var=True
    s_üst=1
    s_alt=0
    emit=[]
    for i in range(len(word)):
        the_character=word[i]
        emit_new, s, a, b, altta_0_mı_var, ustte_1_mi_var, s_alt, s_üst, s_teki_artış, saf_artış = one_time_encoder_MC(whole, c, d, dict, s, a, b, the_character, altta_0_mı_var, ustte_1_mi_var, s_üst, s_alt)
        emit+=emit_new
    emit+=one_time_last_character_encoder_MC(whole, s, a, b, altta_0_mı_var, ustte_1_mi_var, s_üst,s_alt)
    return emit



def zero_order_dict_c_d_returner(chars, rates_raw, bit_precision):
    whole = 2 ** bit_precision
    dict = {}
    for v in range(len(chars)):
        dict.update({chars[v]: v})

    rates = []
    for u in range(len(chars)):
        if (u != len(chars) - 1):
            rates.append(round(whole * rates_raw[u]))
        else:
            rates.append(whole - sum(rates))
    c = [0]
    for r in range(len(chars) - 1):
        c.append(c[r] + rates[r])
    d = [rates[0]]
    for r in range(len(chars) - 1):
        d.append(d[r] + rates[r + 1])

    return dict, c, d

def get_the_arithmetic_encoding_of_a_word_with_eof(word, chars, rates_raw, bit_precision,dict,c,d):
    whole = 2 ** bit_precision
    return zero_order_encoder_MC_with_eof(whole, word, c, d, dict)

def decode_zero_order_encoding_with_eof(bit_precision, encoding, dict,c,d,chars): # returns 0 if there is an error
    whole = 2 ** bit_precision
    encoding_copy=encoding.copy()

    decoded_word, remaining_encoding=decoder(whole, encoding_copy, c, d, dict, chars, 0, whole, True, True, [], 1, 0, 0,True, 0, False, 0, 0)

    if decoded_word!=0:
        return ''.join(decoded_word), remaining_encoding
    else:
        return 0, remaining_encoding




def word_arithmetic_coder_suitability_checker_with_eof(word, encoding, bit_precision, dict,c,d,chars):
    trial1=encoding.copy()+[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1] # maximum case
    trial2=encoding.copy()+[] # minimum case

    word1,z1=decode_zero_order_encoding_with_eof(bit_precision, trial1, dict,c,d,chars)
    word2,z1=decode_zero_order_encoding_with_eof(bit_precision, trial2, dict,c,d,chars)


    if (word1==word and word2==word):
        return 0 # can be encoded by arithmetic
    else:
        return 1 # must be encoded by huffmann

