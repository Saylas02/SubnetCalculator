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


def get_subnet_information(i_ip_addr_bin: str, i_cidr: int):
    """TODO: set up method (information can be such as: netID, broadcast, first/last usable IP, Gateway?)"""
    # split the ip_addr into one string for better iterating
    sep_ip_addr_bin = i_ip_addr_bin.split(".")
    concat_ip_addr = sep_ip_addr_bin[0] + sep_ip_addr_bin[1] + sep_ip_addr_bin[2] + sep_ip_addr_bin[3]
    # set concatenated_ip_addr into list
    arr_ip_addr_bin = []
    # set cidr for net and bc loop
    net_cidr, bc_cidr = i_cidr, i_cidr
    for char in concat_ip_addr:
        arr_ip_addr_bin.append(char)
    arr_net_id, arr_bc_id = arr_ip_addr_bin.copy(), arr_ip_addr_bin.copy()
    # getting net-ID
    while net_cidr < 32:
        arr_net_id[net_cidr] = '0'
        net_cidr += 1
    # declare output variable
    o_net_id = ""
    for count, values in enumerate(arr_net_id):
        if count % 8 == 0 and count != 0:
            o_net_id = o_net_id + "." + values
        else:
            o_net_id = o_net_id + values
    print(f"Net-ID (bin): {o_net_id}\n"
          f"Net-ID (dec): {addr_bin_to_dec(o_net_id)}")
    # getting bc-ID
    while bc_cidr < 32:
        arr_bc_id[bc_cidr] = '1'
        bc_cidr += 1
    # declare output variable
    o_bc_id = ""
    for count, values in enumerate(arr_bc_id):
        if count % 8 == 0 and count != 0:
            o_bc_id = o_bc_id + "." + values
        else:
            o_bc_id = o_bc_id + values
    print(f"BC-ID (bin): {o_bc_id}\n"
          f"BC-ID (dec): {addr_bin_to_dec(o_bc_id)}")


def cidr_to_subnet_mask(i_cidr: int) -> str:
    i, sn_mask = 0, ""
    while i < 32:
        if i < i_cidr and i % 8 != 0:
            sn_mask = sn_mask + "1"
        elif i < i_cidr and i % 8 == 0:
            if i == 0:
                sn_mask = sn_mask + "1"
            else:
                sn_mask = sn_mask + ".1"
        elif i >= i_cidr and i % 8 != 0:
            sn_mask = sn_mask + "0"
        else:
            if i == 0:
                sn_mask = sn_mask + "0"
            else:
                sn_mask = sn_mask + ".0"
        i += 1
    return sn_mask


def check_valid_cidr(input_cidr: int) -> bool:
    if input_cidr not in range(0, 32):
        print(f"Given CIDR /{input_cidr} is not valid!\n")
        return False
    else:
        return True


def get_net_class(ip_addr, i_cidr) -> bool:
    arr_octet = ip_addr.split(".")
    # Class A Net between 10.0.0.0 and 10.255.255.255 and CIDR >= 8
    if int(arr_octet[0]) == 10 and i_cidr >= 8 <= 32:
        print(f"Class A-Net (between 10.0.0.0 and 10.255.255.255), Currently {ip_addr}")
        return True

    # Class B Net between 172.16.0.0 and 172.31.255.255 and CIDR >= 16
    elif int(arr_octet[0]) == 172 and int(arr_octet[1]) < 32 and int(arr_octet[0]) == 172 and int(arr_octet[1]) > 15 \
            and i_cidr >= 16 <= 32:
        print(f"Class B-Net (between 172.16.0.0 and 172.31.255.255), Currently {ip_addr}")
        return True

    # Class C Net between 192.168.0.0 and 192.168.255.255 and CIDR >= 24
    elif int(arr_octet[0]) == 192 and int(arr_octet[1]) == 168 and 16 <= i_cidr <= 32:
        print(f"Class C-Net (between 192.168.0.0 and 192.168.255.255), Currently {ip_addr}")
        return True

    else:
        print("Not declared as a private network!")
        return True


def check_valid_ip(ip_addr) -> bool:
    arr_octet = ip_addr.split(".")
    if len(arr_octet) != 4:
        print("The IP-address does not have 4 correct octets. Please enter valid IP-Address and run again!")
        return False

    for count, octet in enumerate(arr_octet):
        if int(octet) < 0 or int(octet) > 255:
            print(f"The range of octet {count+1} is too big. "
                  f"Octets must have a size between 0 and 255! Currently: {octet}")
            return False
    return True


if __name__ == '__main__':
    # setting flags
    valid_ip, valid_cidr = False, False
    # create array for separated input values ([0]IP_addr, [1]SN_mask)
    arr_input_values = []
    # initialize ip_address and cidr variable
    ip_address, cidr = None, None
    # loop as long as ip or sn mask are not valid
    while not valid_ip or not valid_cidr:
        # user input
        user_input = input("Please enter IP-address in CIDR notation. (Like: '1.2.3.4 /24')\n"
                           "==>")
        # check if "/" is in input
        if "/" in user_input:
            # split the input to arr_input_values[0] = ip address, arr_input_values[1] = CIDR
            arr_input_values = user_input.split("/")
            # loop over all elements to remove spaces
            for index, elements in enumerate(arr_input_values):
                # remove all spaces in arr_input_values
                arr_input_values[index] = arr_input_values[index].replace(" ", "")
            # assign values to variables
            ip_address, cidr = arr_input_values[0], int(arr_input_values[1])
            # check validation of ip address
            valid_ip = check_valid_ip(ip_address)
            # check valid cidr
            valid_cidr = check_valid_cidr(cidr)
            # get net class
            get_net_class(ip_address, cidr)
        else:
            # print invalid format
            print("The format is not correct! Please set CIDR with '/' and try again!. ")
    # get ip address as one String
    ip_addr_bin, sn_mask_bin = addr_dec_to_bin(arr_input_values[0]), cidr_to_subnet_mask(int(arr_input_values[1]))
    # print out IP-address and Subnet Mask in binary
    print(f"IP-Address in binary: {ip_addr_bin}\n"
          f"Subnet Mask in binary: {sn_mask_bin}")

    get_subnet_information(ip_addr_bin, cidr)
