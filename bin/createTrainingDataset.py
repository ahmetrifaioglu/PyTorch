def target():
    import math
    tar_fl = open("/Users/trman/OneDrive/Projects/PyTorch/bin/data/encoding.tsv", "r")
    lst_tar_fl = tar_fl.read().split("\n")
    tar_fl.close()

    tar_dict= dict()

    for line in lst_tar_fl[1:]:
        if line!="":
            try:
                target_id = (line.split("\t")[0]).split("|")[1]
                descriptors = line.split("\t")[1:]
                str_desc = ""
                for item in descriptors[:-1]:
                    str_desc += "{},".format(item)
                str_desc += descriptors[-1]
                tar_dict[target_id] = str_desc
            except:
                pass

    comp_fl = open("/Users/trman/OneDrive/Projects/PyTorch/bin/data/ecfp4desc.csv", "r")
    lst_comp_fl = comp_fl.read().split("\n")
    comp_fl.close()

    com_dict = dict()

    for line in lst_comp_fl:
        if line!="":
            comp_id = line.split(",")[0]

            descriptors = line.split(",")[1:]
            str_desc = ""
            for item in descriptors[:-1]:
                str_desc += "{},".format(item)
            str_desc += descriptors[-1]
            com_dict[comp_id] = str_desc

    assoc_fl = open("/Users/trman/OneDrive/Projects/PyTorch/bin/data/Dtc_comp_targ_uniq_inter_filtered_onlykinase.txt", "r")
    lst_assoc_fl = assoc_fl.read().split("\n")
    assoc_fl.close()
    #print(len(tar_dict.keys()), len(com_dict.keys()))
    for line in lst_assoc_fl:
        if line!="":
            comp_id, tar_id, bioac_va = line.split(",")
            bioac_va = -1*math.log10(10e-9*float(bioac_va))
            try:
                str_prt = "{},{},{},{},{}".format(comp_id, tar_id, str(bioac_va),com_dict[comp_id],tar_dict[tar_id])
                print(str_prt)

            except:
                pass

def test():

    import math
    tar_fl = open("/Users/trman/OneDrive/Projects/PyTorch/bin/data/encoding_test.tsv", "r")
    lst_tar_fl = tar_fl.read().split("\n")
    tar_fl.close()

    tar_dict = dict()

    for line in lst_tar_fl[1:]:
        if line != "":
            try:
                target_id = (line.split("\t")[0]).split("|")[1]
                descriptors = line.split("\t")[1:]
                str_desc = ""
                for item in descriptors[:-1]:
                    str_desc += "{},".format(item)
                str_desc += descriptors[-1]
                tar_dict[target_id] = str_desc
            except:
                pass
    #print(len(tar_dict))
    comp_fl = open("/Users/trman/OneDrive/Projects/PyTorch/bin/data/test_ecfp4desc.csv", "r")
    lst_comp_fl = comp_fl.read().split("\n")
    comp_fl.close()

    com_dict = dict()

    for line in lst_comp_fl:
        if line != "":
            comp_id = line.split(",")[0]

            descriptors = line.split(",")[1:]
            str_desc = ""
            for item in descriptors[:-1]:
                str_desc += "{},".format(item)
            str_desc += descriptors[-1]
            com_dict[comp_id] = str_desc

    assoc_fl = open("/Users/trman/OneDrive/Projects/PyTorch/bin/data/round_1_template.csv", "r")

    lst_assoc_fl = assoc_fl.read().split("\n")
    assoc_fl.close()
    # print(len(tar_dict.keys()), len(com_dict.keys()))
    for line in lst_assoc_fl[1:]:
        if line != "":
            #print(line)
            comp_id = line.split(",")[2]
            tar_id = line.split(",")[3]
            bioac_va = "1.0"

            str_prt = "{},{},{},{},{}".format(comp_id, tar_id, str(bioac_va), com_dict[comp_id],
                                                  tar_dict[tar_id])
            print(str_prt)

            #except:
            #    pass

test()