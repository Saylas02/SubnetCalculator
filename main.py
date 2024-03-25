def conv_dec_to_bin(dec)->str:
    # TODO: implement algorithm to convert decimal value to binary value
    return


def check_valid_input(ip_addr)->bool:
    # separate the octets to arr with 4 entries
    arr_octet = ip_addr.split(".")
    if len(arr_octet) != 4:
        print("The IP-address does not have 4 octets. Please enter valid IP-Address and run again!")
        return False

    for count, octet in enumerate(arr_octet):
        if int(octet) < 0 or int(octet) > 255:
            print(f"The range of octet {count+1} is too big. Octets must have a size between 0 and 255! Currently: {octet}")
            return False

    # Class A Net between 10.0.0.0 and 10.255.255.255
    if int(arr_octet[0]) == 10:
        print(f"Class A-Net (between 10.0.0.0 and 10.255.255.255) Currently {ip_addr}")
        return True

    # Class B Net between 172.16.0.0 and 172.31.255.255
    elif int(arr_octet[0]) == 172 and int(arr_octet[1]) < 32 and int(arr_octet[0]) == 172 and int(arr_octet[1]) > 15:
        print(f"Class B-Net (between 172.16.0.0 and 172.31.255.255) Currently {ip_addr}")
        return True

    # Class C Net between 192.168.0.0 and 192.168.255.255
    elif int(arr_octet[0]) == 192 and int(arr_octet[1]) == 168:
        print(f"Class C-Net (between 192.168.0.0 and 192.168.255.255) Currently {ip_addr}")
        return True

    else:
        print("Not declared as a private network!")
        return True


if __name__ == '__main__':
    ip_addr = "172.32.255.1"
    sn_mask = "255.255.0.0"
    check_valid_input(ip_addr)
