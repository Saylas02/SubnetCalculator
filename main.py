def conv_dec_to_bin(dec)->str:
    arr_dec_octet = ip_addr.split(".")
    arr_bin_octet = ""
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
            arr_bin_octet = arr_bin_octet + str(res) + "."
        else:
            arr_bin_octet = arr_bin_octet + str(res)
    print(f"IP-address in binary: {arr_bin_octet}")
    return arr_bin_octet


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
    ip_addr = "10.01.1.1"
    sn_mask = "255.255.0.0"
    check_valid_input(ip_addr)
    conv_dec_to_bin("172.32.255.1")

