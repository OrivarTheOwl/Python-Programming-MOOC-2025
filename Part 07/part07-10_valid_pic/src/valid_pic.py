from datetime import datetime

def is_it_valid(pic: str):
    if len(pic) != 11:
        return False


    day = int(pic[0:2])
    month = int(pic[2:4])
    year = int(pic[4:6])
    century_marker = pic[6]
    identifier = int(pic[7:10])
    control = pic[10]
    
    if century_marker == "+":
        century = 1800
    elif century_marker == "-":
        century = 1900
    elif century_marker == "A":
        century = 2000
    else:
        return False

    full_year = century + year

    if day > 31 or day < 1:
        return False
    if month > 12 or month < 1:
        return False
    
    control_base = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    control_string = pic[0:6] + pic[7:10]
    control_int = int(control_string)
    control_calc = control_int % 31
    control_char = control_base[control_calc]

    if control != control_char:
        return False
    
    try:
        dob = datetime(full_year, month, day)
    except:
        return False


    return True





if __name__ == "__main__":
    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))
    print(is_it_valid("290200-1239"))