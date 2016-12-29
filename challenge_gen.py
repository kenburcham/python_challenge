# Ken Burcham - Fun little programming challenge - Dec 19, 2016
# generate our required text file

import challenge

to_encode = [6111,340,-2628,-255,7550]
to_decode = [["0a","0a"],["00","29"],["3f","0f"],["44","00"],["5e","7f"]]

text_file = open("ConvertedData.txt", "w")

for i_in in to_encode:
    text_file.write("{0}\n".format(challenge.fEncode(i_in)))

for sa_in in to_decode:
    text_file.write("{0}\n".format(challenge.fDecode(sa_in[0],sa_in[1])))

text_file.close()
