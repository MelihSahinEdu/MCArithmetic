import sys
import random
main_condition=False
sys.setrecursionlimit(25000)

golden_ratio=0.6180339887498948482045868343656381177203091798057628621354486227




# Hufmann Coding, written by ChatGPT, modified by me

class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def __str__(self):
        return self.left, self.right


def huffman_code_tree(node, binString=''):
    '''
    Function to find Huffman Code
    '''
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = {}
    d.update(huffman_code_tree(l, binString + '10'))
    d.update(huffman_code_tree(r, binString + '0'))
    return d


def make_tree(nodes):
    '''
    Function to make tree
    :param nodes: Nodes
    :return: Root of the tree
    '''
    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    return nodes[0][0]

def MC_Huffmann_encoder(word, chars, rates_raw_copy):
    freq={}


    for o in range(len(chars)):
        freq.update({chars[o]:rates_raw_copy[o]})


    string=word

    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)


    node = make_tree(freq)

    encoding = huffman_code_tree(node)
    encoded=""
    for k in range(len(string)):
        encoded+=str(encoding[string[k]])
    return encoded
# end of MC Huffmann coding

def one_time_last_character_encoder_MC_without_EOF( whole, c, d, dict,s,a,b,the_character,altta_0_mı_var,ustte_1_mi_var,s_üst,s_alt  ):
    kaç_tane_bit_eklendi=0
    half = whole // 2
    quarter = whole // 4

    zero_length = round((6180339887498948482045868343656381177203091798057628621354486227 * whole)//10000000000000000000000000000000000000000000000000000000000000000)
    one_length = whole - zero_length

    emit = []
    cond1=True
    while (cond1):

            if ((not altta_0_mı_var) and (not ustte_1_mi_var)):

                if (a>=one_length):

                    if (s>0):

                        emit.append(s_üst)

                        for t in range(s - 1):
                            emit.append(0)

                        s = 0

                    emit.append(0)
                    kaç_tane_bit_eklendi+=1

                    a = int(((a - one_length) * (zero_length)) / one_length)
                    b = int(((b - one_length) * (zero_length)) / one_length)

                    altta_0_mı_var = True
                    ustte_1_mi_var = True

                elif (b<one_length):

                    if (s>0):

                        emit.append(s_alt)

                        new_commute = 1
                        if (s_alt == 1):
                            new_commute = 0

                        for t in range(s - 1):
                            if (t % 2 == 0):
                                emit.append(new_commute)


                            else:
                                emit.append(s_alt)
                        s = 0


                    emit.append(1)
                    emit.append(0)
                    kaç_tane_bit_eklendi+=2


                    a = int((a * (whole)) / one_length)
                    b = int((b * (whole)) / one_length)

                    altta_0_mı_var = True
                    ustte_1_mi_var = True

                else:
                    alt_uzunluk=one_length-a
                    üst_uzunluk=b-one_length

                    if (üst_uzunluk>alt_uzunluk):
                        if (s > 0):

                            emit.append(s_üst)

                            for t in range(s - 1):
                                emit.append(0)

                            s = 0
                        emit.append(0)
                        kaç_tane_bit_eklendi += 1

                        a = 0
                        b = int(((b - one_length) * (zero_length)) / one_length)

                        while(True):
                            if (b>=zero_length):
                                cond1=False
                                break
                            else:
                                emit.append(0)
                                b=int((b*whole)/zero_length)
                        break

                    else:
                        if (s > 0):

                            emit.append(s_alt)

                            new_commute = 1
                            if (s_alt == 1):
                                new_commute = 0

                            for t in range(s - 1):
                                if (t % 2 == 0):
                                    emit.append(new_commute)


                                else:
                                    emit.append(s_alt)
                            s = 0

                        emit.append(1)
                        emit.append(0)
                        kaç_tane_bit_eklendi += 2
                        a = int((a * (whole)) / one_length)
                        b = whole

                        while(True):
                            if (a<0):
                                cond1=False
                                break
                            else:
                                a = int(((a - zero_length) * (whole)) / one_length)
                                emit.append(1)
                                emit.append(0)
                        break

            elif (altta_0_mı_var and (not ustte_1_mi_var)):
                if (a>=half):
                    if (s>0):
                        emit.append(s_üst)

                        for t in range(s - 1):
                            emit.append(0)

                        s = 0

                    emit.append(0)
                    kaç_tane_bit_eklendi += 1

                    a = 2 * (a - half)
                    b = 2 * (b - half)

                    altta_0_mı_var = True
                    ustte_1_mi_var = True

                elif (b<half):
                    if (s>0):
                        emit.append(s_alt)

                        new_commute = 1
                        if (s_alt == 1):
                            new_commute = 0

                        for t in range(s - 1):
                            if (t % 2 == 0):
                                emit.append(new_commute)


                            else:
                                emit.append(s_alt)
                        s=0

                    emit.append(0)
                    kaç_tane_bit_eklendi += 1



                    a = 2 * a
                    b = 2 * b

                    altta_0_mı_var = True
                    ustte_1_mi_var = True

                else:
                    üst_uzunluk=b-half
                    alt_uzunluk=half-a

                    if (üst_uzunluk>alt_uzunluk):
                        if (s > 0):
                            emit.append(s_üst)

                            for t in range(s - 1):
                                emit.append(0)

                            s = 0

                        emit.append(0)
                        kaç_tane_bit_eklendi += 1

                        a = 0
                        b = 2 * (b - half)

                        while (True):

                            if (b >= zero_length):
                                cond1 = False
                                break
                            else:
                                emit.append(0)
                                b = int((b * whole) / zero_length)

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
                        s = 0

                    emit.append(0)

                    a = 2 * a
                    b = whole

                    while (True):
                        if (a < 0):
                            cond1 = False
                            break
                        else:
                            a = int(((a - zero_length) * (whole)) / one_length)
                            emit.append(1)
                            emit.append(0)
                    break

            elif (altta_0_mı_var and ustte_1_mi_var):
                # here, s must always be 0
                if (a>=zero_length):
                    emit.append(1)
                    emit.append(0)
                    kaç_tane_bit_eklendi += 2
                    a = int( ((a - zero_length) * (whole)) / one_length)
                    b = int(((b - zero_length) * (whole)) / one_length)

                elif (b<zero_length):
                    emit.append(0)
                    kaç_tane_bit_eklendi += 1
                    a = int((a * (whole)) / zero_length)
                    b = int((b * (whole)) / zero_length)

                else:
                    üst_uzunluk=b-zero_length
                    alt_uzunluk=zero_length-a
                    if (üst_uzunluk>alt_uzunluk):
                        emit.append(1)
                        emit.append(0)
                        a = 0
                        b = int(((b - zero_length) * (whole)) / one_length)

                        while(True):
                            if (b>=zero_length):
                                cond1=False
                                break
                            else:
                                emit.append(0)
                                b = int((b * (whole)) / zero_length)
                        break


                    else:
                        emit.append(0)
                        a = int((a * (whole)) / zero_length)
                        b = whole

                        while(True):
                            if (a<0):
                                cond1=False
                                break
                            else:
                                emit.append(1)
                                emit.append(0)
                                a = int(((a - zero_length) * (whole)) / one_length)
                        break

    return emit, kaç_tane_bit_eklendi


def one_time_encoder_MC( whole, c, d, dict,s,a,b,the_character,altta_0_mı_var,ustte_1_mi_var,s_üst,s_alt  ):

    half=int(whole/2)
    quarter=whole/4

    zero_length = round((6180339887498948482045868343656381177203091798057628621354486227 * whole)//10000000000000000000000000000000000000000000000000000000000000000)
    one_length = whole - zero_length

    emit=[]

    w = b - a

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
                special_number=int(((whole*6180339887498948482045868343656381177203091798057628621354486227)*6180339887498948482045868343656381177203091798057628621354486227)//(10000000000000000000000000000000000000000000000000000000000000000**2))
                if (a >= special_number):
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
                special_number_1 = round(((whole * 2 * 6180339887498948482045868343656381177203091798057628621354486227) * 6180339887498948482045868343656381177203091798057628621354486227)//(10000000000000000000000000000000000000000000000000000000000000000**2))  # 801041=whole*(2*(phi*phi))
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
                special_number_2 = round(((whole // 2) * (10000000000000000000000000000000000000000000000000000000000000000 + 6180339887498948482045868343656381177203091798057628621354486227))//10000000000000000000000000000000000000000000000000000000000000000)
                special_number_3 = round(((whole // 2) * 6180339887498948482045868343656381177203091798057628621354486227)//10000000000000000000000000000000000000000000000000000000000000000)  # ((324028=whole/2)*phi)
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
    zero_length = round((6180339887498948482045868343656381177203091798057628621354486227 * whole)//10000000000000000000000000000000000000000000000000000000000000000)
    one_length = whole - zero_length

    the_character=0



    number_finish_now=whole
    number_now=0

    j=0
    last_index=min(20,len(sequence))  # 20 can be modified

    if (len(sequence) == 0):
        return the_seqeunce

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



    final_number=(number_finish_now+number_now)/2

    checkher=True

    for h in range(len(chars)):
        lower_bound=int((c[dict[chars[h]]]*(number_finish-number))/whole)+number
        upper_bound=int((d[dict[chars[h]]]*(number_finish-number))/whole)+number


        if ( final_number<upper_bound): # z'nin yani number_now'ın çok düşük olduğunu farzet
            the_seqeunce.append(chars[h])
            the_character=chars[h]
            checkher=False
            break
    if (checkher):
        #print("hata")
        return the_seqeunce


    emit, s, number, number_finish,  altta_0_mı_var, ustte_1_mi_var, s_alt, s_üst,s_teki_artış,saf_artış=one_time_encoder_MC( whole, c, d, dict,s,number,number_finish,the_character,altta_0_mı_var,ustte_1_mi_var,s_üst,s_alt)

    s_yedek=s
    emit_last, son_kaç_bit_var=one_time_last_character_encoder_MC_without_EOF(whole, c, d, dict, s, number, number_finish, the_character, altta_0_mı_var, ustte_1_mi_var, s_üst,s_alt)

    if ((saf_artış+s_teki_artış)>0):
        if ((saf_artış)+(s_teki_artış)-1>=len(sequence)):
            pass
        else:
            bir_önceki_bit=sequence[(saf_artış)+(s_teki_artış)-1]



    sequence = sequence[(saf_artış+s_teki_artış):]

    if (len(sequence)==len(emit_last[s_yedek:]) and sequence==emit_last[s_yedek:]):
        return the_seqeunce




    kaçıncı+=1
    return decoder(whole, sequence, c, d, dict, chars, number, number_finish, altta_0_mı_var, ustte_1_mi_var,the_seqeunce, s_üst, s_alt, s, s==0,toplam_emit,main_condition,kaçıncı,bir_önceki_bit)

def zero_order_encoder_MC_without_eof( whole, word, c, d, dict):
    a=0
    b=whole
    half=int(whole/2)
    quarter=whole/4
    s=0
    zero_length = round((6180339887498948482045868343656381177203091798057628621354486227 * whole)//10000000000000000000000000000000000000000000000000000000000000000)
    one_length = whole - zero_length
    altta_0_mı_var=True
    ustte_1_mi_var=True
    s_üst=1
    s_alt=0
    emit=[]
    for i in range(len(word)):
        the_character=word[i]
        emit_new, s, a, b, altta_0_mı_var, ustte_1_mi_var, s_alt, s_üst, s_teki_artış, saf_artış = one_time_encoder_MC(whole, c, d, dict, s, a, b, the_character, altta_0_mı_var, ustte_1_mi_var, s_üst, s_alt)
        emit+=emit_new

    emit_new,kaç_tane_bit_eklendi=one_time_last_character_encoder_MC_without_EOF(whole, c, d, dict, s, a, b, the_character, altta_0_mı_var, ustte_1_mi_var, s_üst,s_alt)
    emit+=emit_new
    return emit


def random_zero_order_text_generator_without_eof(chars, rates_raw, word_length):
    d = [rates_raw[0]]
    for r in range(len(rates_raw) - 1):
        d.append(d[r] + rates_raw[r + 1])
    the_word=[]
    for t in range(word_length):
        sayı = random.uniform(0, 1)
        the_char = 0
        for j in range(len(d)):
            if sayı<=d[j]:
                the_char=chars[j]
                break
        the_word.append(the_char)
    return "".join(the_word)

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

def get_the_arithmetic_encoding_of_a_word_without_eof(word, chars, rates_raw, bit_precision,dict,c,d):
    whole = 2 ** bit_precision
    return zero_order_encoder_MC_without_eof(whole, word, c, d, dict)


def decode_zero_order_encoding_without_eof(bit_precision, encoding, dict,c,d,chars): # returns 0 if there is an error
    whole = 2 ** bit_precision
    encoding_copy=encoding.copy()

    decoded_word=decoder(whole, encoding_copy, c, d, dict, chars, 0, whole, True, True, [], 1, 0, 0,True, 0, False, 0, 0)

    return ''.join(decoded_word)


def return_zero_order_hufmann_encoding_without_eof(chars, rates_raw):
    rates_raw_copy=rates_raw.copy()
    freq = {}
    for o in range(len(chars)):
        freq.update({chars[o]: rates_raw_copy[o]})
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    node = make_tree(freq)
    encoding = huffman_code_tree(node)

    return encoding

def encode_a_word_zero_order_hufmann_without_eof(encoding, word):
    string = word
    encoded = ""
    for k in range(len(string)):
        encoded += str(encoding[string[k]])

    returned=[]
    for t in range(len(encoded)):
        returned.append(int(encoded[t]))
    return returned

def word_arithmetic_coder_suitability_checker_without_eof(word, encoding, bit_precision, dict,c,d,chars):

    trial2=encoding.copy()+[] # minimum case


    word2=decode_zero_order_encoding_without_eof(bit_precision, trial2, dict,c,d,chars)

    if (word2==word):
        return 0 # can be encoded by arithmetic
    else:
        print("*****")
        print(word)
        print(word2)

        return 1 # must be encoded by huffmann


