'''
Huffman code.
    First of all, consult a good book on discrete mathematics or 
    algorithms for a detailed description of Huffman codes!

    We suppose a set of symbols with their frequencies, given 
    as a list of fr(S,F) terms. Example: 
    [fr(a,45),fr(b,13),fr(c,12),fr(d,16),fr(e,9),fr(f,5)]. 
    Our objective is to construct a list hc(S,C) terms, 
    where C is the Huffman code word for the symbol S. In our example, 
    the result could be 
    Hs = [hc(a,'0'), hc(b,'101'), hc(c,'100'), hc(d,'111'), hc(e,'1101'), 
    hc(f,'1100')] [hc(a,'01'),...etc.]. 
    The task shall be performed by the predicate huffman/2 defined 
    as follows:

    % huffman(Fs,Hs) :- Hs is the Huffman code table for the frequency 
    table Fs 
'''

from collections import defaultdict

data_list = [['a', 45], ['b', 13], ['c', 12], ['d', 16], ['e', 9], ['f', 5]]


huffman_codes = defaultdict(str)

while len(data_list) > 1:
    for i in range(len(data_list)):
        for j in range(i, len(data_list)):
            if data_list[i][-1] > data_list[j][-1]:
                temp = data_list[i]
                data_list[i] = data_list[j]
                data_list[j] = temp

    element_one = data_list[0]
    element_two = data_list[1]

    li = []
    for i in range(len(element_one)-1):
        huffman_codes[element_one[i]] = '0' + huffman_codes[element_one[i]]
        li.append(element_one[i])
    for i in range(len(element_two)-1):
        huffman_codes[element_two[i]] = '1' + huffman_codes[element_two[i]]
        li.append(element_two[i])

    li.append(element_one[-1]+element_two[-1])
    data_list.pop(0)
    data_list.pop(0)
    data_list.insert(0, li)

for key in huffman_codes:
    print(f"{key}: {huffman_codes[key]}")
