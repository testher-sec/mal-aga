
def get_selected_bytes():
     
    selected = idaapi.read_selection()
    curr_ea = idc.ScreenEA()
    print "[+] Processing range: %x - %x" % (selected[1],selected[2])

    if (selection_is_valid(selected, curr_ea)):
        return selected
    else:
        return None


def make_dwords():
    selected = get_selected_bytes()
    if selected:
        for ea in range(selected[1], selected[2], 4):
            if not cool_to_clobber(ea):
                print "[-] Error: Something that we shouldn't clobber at 0x%x" % ea
                break
            idaapi.doDwrd(ea,4)
            print "[+] Processed %x" % ea
    else:
        print "[-] Error: EA is not currently a selection endpoint %x" % idc.ScreenEA()