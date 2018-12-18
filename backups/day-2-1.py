import time

ids = ['myhposlqgeauywfikztndcvrqr', 'mbhposlxfeauywoikztndcvjqi', 'mbhpoulxgeagywfikytndcvjqr', 'jbhposlxgeauywdikztndcvjqk', 'mbhpsslxueauywfikzfndcvjqr', 'mbhposnxgeauzyfikztndcvjqr', 'ibhposlxgetvywfikztndcvjqr', 'mbcposlxgeauywfikztxdcvjqv', 'mlhposltgeauywfikitndcvjqr', 'mbhpostxgeauywfikztndjvjqy', 'mboboslxglauywfikztndcvjqr', 'mbhpoglxgeahywfikztndcvjqp', 'mbhposlxgeapydpikztndcvjqr', 'mbhposlxseauywfikztnncljqr', 'mbhposlxgeauydfisztndcvjqj', 'mbhposlxgeaugwwikzlndcvjqr', 'mbhpoklxgeauywfikztndvvmqr', 'mbhposlxgeauywfikdtndcmjqx', 'mbhposlxaeauapfikztndcvjqr', 'mbwposgxgeauymfikztndcvjqr', 'mbhposlxgeauvwfirzcndcvjqr', 'mbhpozlxgeaqywfykztndcvjqr', 'mahqoslxgeauywfikzgndcvjqr', 'mbhposlcgexbywfikztndcvjqr', 'ykhposlxgeeuywfikztndcvjqr', 'mbhgoswxgeauywfikztndhvjqr', 'mbhposlxgeauywfikztnocmjqp', 'mbvposfageauywfikztndcvjqr', 'mbhpnslxgeauywfikztndgejqr', 'mblposfxgeauypfikztndcvjqr', 'mbhposlxyeauywfikzpndcvmqr', 'ibhposlbgeauywfikotndcvjqr', 'mbmposlxgeauywfiktwndcvjqr', 'mbhposlxgeduywfikztndfvoqr', 'mbhpoklxdeauywfikztndcvuqr', 'mbhposlxgeauywfikltnlcvuqr', 'mbhposlbgsauywfikztndsvjqr', 'mbhposlxgeauywfirzfndcbjqr', 'mphposlxgeauywfikztndcvjgg', 'mohposlcgeauywfikzsndcvjqr', 'mbhpovlxgeauyqfikotndcvjqr', 'qbhpgslxgeauywqikztndcvjqr', 'mbhposlxweauywfikztndtvjqm', 'pbhposlxgeauywfikztnncvjqm', 'mbbposlxpeauuwfikztndcvjqr', 'mbhposlxgmauyrfikztndcvjir', 'pbhposlqgefuywfikztndcvjqr', 'mbhkoslxgeauywfikztndciwqr', 'mbtpoflxgeauywfikztndrvjqr', 'mbhcoslxveguywfikztndcvjqr', 'mbhpovlxgeauywfhkdtndcvjqr', 'mbhposlxgeauywftrztndcujqr', 'mbhposlxgeaoywfdkzpndcvjqr', 'mbnposlxgeyuywfikztldcvjqr', 'mbaposlxweauywfikftndcvjqr', 'mbhposljgeauywfikztcdcvvqr', 'nbhpkslxgeauywfikzwndcvjqr', 'mbhtoslxgeauywfikzkndcvjdr', 'mbhposxxgeaxywfikztndsvjqr', 'mbdpoflxgeauywfisztndcvjqr', 'mbhposvxgeauywfikztnscvnqr', 'mbcposlxghauywfikztndcgjqr', 'mbhpovlxgeauywpckztndcvjqr', 'mbhpfslxgeauywbikntndcvjqr', 'mbhpowyxgeauywfikztndcvjcr', 'mbhposlxoeatywfikztndcvoqr', 'mchpfslxgeauywfikztidcvjqr', 'mbhposvxgearywfikztndcvjcr', 'mbhposlxgeauywfpcztnduvjqr', 'mbhposlxgmauyyfiqztndcvjqr', 'mbhposlxteauuwfikwtndcvjqr', 'mbhpotlspeauywfikztndcvjqr', 'mbhpoelxgeauywfikztndckjkr', 'mbhpnslxgeauywfikztndcvkqs', 'mbhpksfxgwauywfikztndcvjqr', 'mxhwoglxgeauywfdkztndcvjqr', 'mbhphsbjgeauywfikztndcvjqr', 'mbhposlxgeauwifixztndcvjqr', 'mbhposqxguauywfikztndcwjqr', 'mbhposlngeauywfikztedcvjor', 'nbhposlxgeauywiikztndcyjqr', 'mbhposlxgeauawfykztndcvbqr', 'mbhplslxgeauywcikztndcvjrr', 'fshposlxgeagywfikztndcvjqr', 'mbhposlxgeauymcikztndcxjqr', 'mbhponlxgeauyloikztndcvjqr', 'mbhposrxzeanywfikztndcvjqr', 'mbhtoslxgeajyifikztndcvjqr', 'mbhposixkeauywfikhtndcvjqr', 'mahhoslxgeaufwfikztndcvjqr', 'mbhpdslxteauywfikzvndcvjqr', 'mfhposlxgeauywfiqttndcvjqr', 'mbhplslxheauywfikztnscvjqr', 'mbhpoylxgeauywbizztndcvjqr', 'mbhposlhgeawywfjkztndcvjqr', 'mbhkoslxgkauywfilztndcvjqr', 'mbhposnxgeauywfikztkdcvlqr', 'mvhpxslxgevuywfikztndcvjqr', 'mbhpohlxgeauyrficztndcvjqr', 'mbhsosuxgewuywfikztndcvjqr', 'mbhpoxlxgeauywuikztnhcvjqr', 'mbhposlxqeauyqfikztndcvrqr', 'mbhpchlxgeauywfikztnhcvjqr', 'mbhposlxgeauywoikztndcfqqr', 'pbhposlxgeagmwfikztndcvjqr', 'mxhwoglxgeauywfikztndcvjqr', 'mbhpospxgaauywfikstndcvjqr', 'mbhwoxlxgeauywfgkztndcvjqr', 'mbhposlxgeauywfikvtndhvsqr', 'mbbposlxgesuywfikztnicvjqr', 'mhhjoslxgeauywfikztndccjqr', 'mbhkoslxgeagywffkztndcvjqr', 'mbhposlxgesqywfukztndcvjqr', 'mbdposlxgeauywfilztndcvjqp', 'mbhposlxgeakqwfikztedcvjqr', 'mbhposuxgeayywficztndcvjqr', 'mbhposlxgeauywfxkztndcloqr', 'mchposlxgeauywoiiztndcvjqr', 'tbhporlxgeauywfikztndcvyqr', 'mbhposlxoevuywfikzindcvjqr', 'qbhposlxfevuywfikztndcvjqr', 'mbhposlxfeauvwfikztndcvgqr', 'mbjposlxgsauywfikztnwcvjqr', 'vbhposlxgeauvwfikztndcvjqk', 'pbhposlxguauyrfikztndcvjqr', 'mbhposlcgeauywfiketndcviqr', 'mbsposlxgvauywfikztndcviqr', 'mbhposlxgeauynfxkztndcvjbr', 'mbhposlxtentywfikztndcvjqr', 'mbhposlxgeavywfikztndhvjnr', 'mbhpsvlxgeauywfikztndcvzqr', 'mzhpotlxgeauywfiyztndcvjqr', 'mbhposkqgeauywfiwztndcvjqr', 'mbhposlxoeakywfikztndcvjqt', 'mbhposlxghauywfikbdndcvjqr', 'mbhpossxgeauywfikqxndcvjqr', 'mbhposlxgearywhikztydcvjqr', 'mbhposlxgeaiywfikztndfvjur', 'mbhpxslxgoazywfikztndcvjqr', 'mbhposlxneauywfibqtndcvjqr', 'mnheoslxteauywfikztndcvjqr', 'mbhposlxgeauywfmkztrdcvuqr', 'mbhzowlxgeauywfizztndcvjqr', 'mbhloslxgeauyofikztnucvjqr', 'mbhposlxneagywfbkztndcvjqr', 'mbhposongeauywfikztnzcvjqr', 'mwyposlxgeauywfikztnqcvjqr', 'mbhpnqaxgeauywfikztndcvjqr', 'mboposlxzeauywfioztndcvjqr', 'mbhposledeauywfikztndqvjqr', 'mphpaslxgeauywfbkztndcvjqr', 'mbhposrxgeauywlikbtndcvjqr', 'ybhnoslxgeauywfihztndcvjqr', 'mbhposlxgeauywfikntxccvjqr', 'mbhposlxgeauqwfikutndcfjqr', 'mbhposlxglabywfikztidcvjqr', 'mbhpollxgeauywfikxtnscvjqr', 'mboposlggeaufwfikztndcvjqr', 'mbhposlxgeauywpikedndcvjqr', 'mbhpoklxgeauywpikztndcvjlr', 'mbhposhxgeauywfifztndcvpqr', 'mbhposlxgwagywfikztndcvjwr', 'mbhpokldgeauywfikztngcvjqr', 'nbhposlxgeauywfiketndcvjxr', 'mbhhoslxgexuywfikrtndcvjqr', 'mbhposlxgefujwfikztkdcvjqr', 'mbhposlxggagywfikztndchjqr', 'mbhposlxgeauyvfilztnicvjqr', 'mbhposlkgeauywfikzxndcvoqr', 'mbhposlxgeauvqfikztndcvuqr', 'zbhposlxgfauylfikztndcvjqr', 'mbhyoshxgeauywfikztndcvjqa', 'sbhposlxgeauyxfikztndavjqr', 'mlhposlxgeauywfikzmndcqjqr', 'mbhpaslxgekuywfikztnncvjqr', 'ibhhoslxteauywfikztndcvjqr', 'mbhposlxgeauyodibztndcvjqr', 'mbhposlxgkaoywfikztndcvpqr', 'mbhonslxgearywfikztndcvjqr', 'mbdpoolxgealywfikztndcvjqr', 'mbepfslxgvauywfikztndcvjqr', 'mbhposlygeauywfikztfdcvaqr', 'mthpoalxgeauywnikztndcvjqr', 'mbhpesbogeauywfikztndcvjqr', 'mbhposlxgjauywfikztnmcvjqj', 'mbhnoslxgeauydfikgtndcvjqr', 'mbhpxslxgeauywfikztndcvjcx', 'muhposlxgwauywfipztndcvjqr', 'mbhpcslxgeauywfiqztndcvjbr', 'mbhpomlxgeauywfioftndcvjqr', 'mbhposlfgepuywfikzmndcvjqr', 'mbhsosliteauywfikztndcvjqr', 'mbwposlxgeauywfikztnycveqr', 'mbhpfslxgeauywfqkztndcvjhr', 'mxhbvslxgeauywfikztndcvjqr', 'fbhposlxgeauywfikzcnmcvjqr', 'mbhfosfxgeauywfikztnduvjqr', 'tbhporlxgeauywfikztndcvjqm', 'mhhposlxgeauywfikctnecvjqr', 'mbhposlxgeqtywfikztnmcvjqr', 'qbhpjslxgeauywfikztndevjqr', 'tbhpxslxgeaunwfikztndcvjqr', 'wbhposlxgeadywfikztndcujqr', 'mbhposlvgeauywfpkotndcvjqr', 'mbhposlxgeagywfingtndcvjqr', 'mbnposlxgeauywfikztnvcjjqr', 'mohpoilxgeadywfikztndcvjqr', 'mbhposlsgeauywfikztnxcvgqr', 'mbhposlogeauywfikqtndcvjor', 'mbhroslxgeauypfikztndcvjqg', 'mblposuxgetuywfikztndcvjqr', 'mbhposlogeiuywfikztodcvjqr', 'mbhposlxgeauylfikztedcvrqr', 'mbhfoslxgeautwxikztndcvjqr', 'mbhouslxgeauywfikztnycvjqr', 'mbhposlxgeauywfvkqtndlvjqr', 'mbfposltgeauytfikztndcvjqr', 'mbhposlxgcapywfikztnddvjqr', 'hbhposlxgeasywfikztnxcvjqr', 'mbhposntgeauywfikztcdcvjqr', 'mbhponlxgfauywfirztndcvjqr', 'mbhposlxgeatywlikztndcvrqr', 'mohroslzgeauywfikztndcvjqr', 'mbhpojaxgeauywfifztndcvjqr', 'rbhposlxgwauywfikztndovjqr', 'mbhpoclxgeaeywfikztndcvjqo', 'mbhposllgeauywfikzondcvmqr', 'mbhpxslxgeauywfikzymdcvjqr', 'mbhposlxgeasywxikztndkvjqr', 'mbhposlxgeauywfivztndcmjqx', 'qbhposlxgpauywfikgtndcvjqr', 'mbhposlxgeauyqdikztqdcvjqr', 'cbhposlxgeauywfikttjdcvjqr', 'mbhgoslxgeanywfihztndcvjqr', 'mbhposlxgeajywfhkztndcvjvr', 'mbhpozlxgeauewfmkztndcvjqr', 'mbhposlxgeagywfbiztndcvjqr', 'mbhmoslxgeauywfikztndrnjqr', 'ybhposmxgeauywfikztndcviqr', 'mrwposlxgeauywfikztndpvjqr', 'mbhposlxneauywfikztndcbjqh', 'mbhpowlxheauywfikztndcojqr', 'mbeposlxgeauywfiwztnycvjqr', 'mbhposixgeapywfikztndcvvqr', 'mbhposlxgeauywfikztnbcvjap', 'mzhposixgenuywfikztndcvjqr', 'mbhposgxgeauywyikztndvvjqr', 'mbhposajgeauywfikztzdcvjqr', 'mbhyoslxgeauywfikzsndcvxqr', 'mbhposlxgdauywfikmtndcljqr', ]


alpha = 'abcdefghijlkmnopqrstuvwxyz'

def has(count, id):
    for letter in alpha:
        if id.count(letter) == count:
            return True
    return False

pair_count = 0
triplet_count = 0

start_time = time.time()

for id in ids:
    if has(2, id):
        pair_count += 1
    if has(3, id):
        triplet_count += 1

end_time = time.time()

print('Pair count: {}'.format(pair_count))
print('Triple count: {}'.format(triplet_count))

print('Checksum: {}'.format(pair_count * triplet_count))

print('finished in {:.4f} seconds'.format(end_time - start_time))