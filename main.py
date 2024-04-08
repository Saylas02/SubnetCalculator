def addr_dec_to_bin(addr) -> str:
    arr_dec_octet = addr.split(".")
    bin_octet = ""
    # convert dec to bin
    for count, octet in enumerate(arr_dec_octet):
        arr_bin, dec, i = [], int(octet), 0
        while dec != 0 or i < 8:
            if dec != 0:
                arr_bin.append(dec % 2)
                dec = dec // 2
                i += 1
            else:
                arr_bin.append(0)
                i += 1
        # read out arr_bin backwards
        x, res = 7, ""
        while x >= 0:
            res = res + str(arr_bin[x])
            x = x - 1
        if count < 3:
            bin_octet = bin_octet + str(res) + "."
        else:
            bin_octet = bin_octet + str(res)
    return bin_octet


def octet_dec_to_bin(i_dec) -> []:
    o_bin, arr_bin, i = 0, [], 0
    while i_dec != 0:
        if i_dec != 0:
            arr_bin.append(i_dec % 2)
            i_dec = i_dec // 2
            i += 1
        else:
            arr_bin.append(0)
            i += 1
    o_bin = arr_bin
    o_bin.reverse()
    return o_bin


def addr_bin_to_dec(addr) -> str:
    arr_bin_oct = addr.split(".")
    dec_octet = ""
    for count, octet in enumerate(arr_bin_oct):
        value = 0
        for exp, bit in enumerate(reversed(octet)):
            value = value + ((2 ** exp) * int(bit))
        if count < len(arr_bin_oct) - 1:
            dec_octet = dec_octet + str(value) + "."
        else:
            dec_octet = dec_octet + str(value)
    return dec_octet


def octet_bin_to_dec(i_bin) -> int:
    o_dec = 0
    for exp, bit in enumerate(reversed(i_bin)):
        o_dec = o_dec + ((2 ** exp) * int(bit))
    return o_dec


def get_subnet_information():
    # TODO: set up method (information can be such as: netID, broadcast, first/last usable IP, Gateway?)
    return


def check_valid_input(ip_address) -> bool:
    # separate the octets to arr with 4 entries
    arr_octet = ip_address.split(".")
    if len(arr_octet) != 4:
        print("The IP-address does not have 4 octets. Please enter valid IP-Address and run again!")
        return False

    for count, octet in enumerate(arr_octet):
        if int(octet) < 0 or int(octet) > 255:
            print(f"The range of octet {count+1} is too big. "
                  f"Octets must have a size between 0 and 255! Currently: {octet}")
            return False

    # Class A Net between 10.0.0.0 and 10.255.255.255
    if int(arr_octet[0]) == 10:
        print(f"Class A-Net (between 10.0.0.0 and 10.255.255.255) Currently {ip_address}")
        return True

    # Class B Net between 172.16.0.0 and 172.31.255.255
    elif int(arr_octet[0]) == 172 and int(arr_octet[1]) < 32 and int(arr_octet[0]) == 172 and int(arr_octet[1]) > 15:
        print(f"Class B-Net (between 172.16.0.0 and 172.31.255.255) Currently {ip_address}")
        return True

    # Class C Net between 192.168.0.0 and 192.168.255.255
    elif int(arr_octet[0]) == 192 and int(arr_octet[1]) == 168:
        print(f"Class C-Net (between 192.168.0.0 and 192.168.255.255) Currently {ip_address}")
        return True

    else:
        print("Not declared as a private network!")
        return True


if __name__ == '__main__':
    ip_addr = "10.10.1.2"
    sn_mask = "255.255.0.0"
