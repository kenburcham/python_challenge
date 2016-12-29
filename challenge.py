# Ken Burcham - Fun little programming challenge - Dec 18, 2016
# Call "python challenge.py" to enter interactive mode

#how far shall we arbitrarily shift the encoding?
i_shiftval = 8192

#encode an integer to hex according to challenge specification
def fEncode(a_int):
    i_in = a_int + i_shiftval               #add shift value
    i_low = i_in & 0x007F                   #mask with 00000001111111
    i_high = i_in & 0x3F80                  #mask with 11111110000000
    i_final = i_low + (i_high << 1)         #combine and shift left

    x_return = format(i_final,'x').zfill(4) #pad hex result to 4 chars

    return x_return

#decode high and low hex bytes to integer according to challenge specification
def fDecode(a_high, a_low):
    i_low = int(a_low,16)                   #a_low will be something like 0a, convert to int
    i_high = int(a_high+'00',16) >> 1       #make a_high to be something like 0a00, then shift right
    i_final = (i_low + i_high)-i_shiftval   #recombine and subtract the shift value

    return i_final;

#give us a simple interactive prompt
def interactive():
    while(1):
        s_input = raw_input("Integer to encode (<enter> to decode):")

        if(s_input == ""):
            break

        try:
            print fEncode(int(s_input));
        except:
            print "Invalid input."

    while(1):
        s_high = raw_input("High hex (2 char) to decode (<enter> to quit):")

        if(s_high != ""):
            s_low = raw_input("Low hex (2 char) to decode:")

        if(s_high == ""):
            break

        try:
            print fDecode(s_high, s_low);
        except:
            print "Invalid input."


if __name__ == '__main__':
    interactive()
