import idaapi
import idc
import inspect
import csv

def selection_is_valid(selection, ea):
    if not (ea == selection[1] or ea == selection[2]-1):
        return False
    else:
        return True

def cool_to_clobber(ea):
    if idc.GetMnem(ea):
        return False
    else:
        return True

def get_selected_bytes():
    selected = idaapi.read_selection()
    curr_ea = idc.ScreenEA()
    print "[+] Processing range: %x - %x" % (selected[1],selected[2])

    if (selection_is_valid(selected, curr_ea)):
        return selected
    else:
        return None

def load_by_referred_addr():
    with open('out.txt', mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {rows[2]:rows[1] for rows in reader}
    return mydict


def load_by_static_addr():
    with open('out.txt', mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]:rows[1] for rows in reader}
    return mydict


def dump_address_names():
    # load dictionary by referenced address
    byReferencedAddr = load_by_referred_addr();
    
    # load dictionary by address. 2nd option of behaviour. to be implemented :)
    byStaticAddr = load_by_static_addr();
    
    selected = get_selected_bytes()
    if selected:
        for ea in range(selected[1], selected[2], 4):
            # Check in map and rename
            key = hex(idaapi.get_dword(ea))[2:]
            if key in byReferencedAddr:
                new_name = byReferencedAddr[key]
                idaapi.set_name(ea, new_name, idaapi.SN_NOWARN)
                print "Processed %x , %s in %x" % (idaapi.get_dword(ea), new_name, ea)
            else:
                print "[+] NOT Processed %x,%s,%x" % (ea,idaapi.get_name(ea), idaapi.get_dword(ea))
    else:
        print "[-] Error: EA is not currently a selection endpoint %x" % idc.ScreenEA()

dump_address_names()
