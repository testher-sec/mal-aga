import idaapi
import idc
import inspect

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


def dump_address_names():
    selected = get_selected_bytes()
    if selected:
        for ea in range(selected[1], selected[2], 4):
            if not cool_to_clobber(ea):
                print "[-] Error: Something that we shouldn't clobber at 0x%x" % ea
                break
            print "[+] Processed %x,%s" % (ea,idaapi.get_name(ea))
    else:
        print "[-] Error: EA is not currently a selection endpoint %x" % idc.ScreenEA()

dump_address_names()