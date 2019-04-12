
def create_ecfp4_fingerprint_file():
    from operator import itemgetter
    import math
    import numpy as np
    from rdkit import Chem
    from rdkit.Chem import AllChem
    path = "/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/IDGDreamChallenge/helper_files/"
    fl_name = "comp_smiles.txt"

    rep_fl = open("%s/%s" % (path, fl_name), "r")
    lst_rep_fl = rep_fl.read().split("\n")
    rep_fl.close()
    if "" in lst_rep_fl:
        lst_rep_fl.remove("")

    compound_smiles_inchi_dict = dict()
    for line in lst_rep_fl:
        # compund_id, smiles, inchi = line.split("\t")
        compund_id, smiles = line.split("\t")
        # compound_smiles_inchi_dict[compund_id] = [smiles, inchi]
        compound_smiles_inchi_dict[compund_id] = smiles

    # compound_ecfp4_vectors = open("../compound_ecfp4_vectors.tsv", "w")
    failureCount = 0
    str_header = "compound id\t" + "\t".join([str(num) for num in range(1024)])
    print(str_header)
    for comp in compound_smiles_inchi_dict.keys():
        isSmilesFailed = False
        fp = ""
        #try:
        m = Chem.MolFromSmiles(compound_smiles_inchi_dict[comp])
        fp = AllChem.GetMorganFingerprintAsBitVect(m, 2, nBits=1024).ToBitString()
        #except:
        #    isSmilesFailed = True
        """
        isInChiFailed = False
        if isSmilesFailed:
            try:
                m = Chem.MolFromInchi(compound_smiles_inchi_dict[comp][1])
                fp = AllChem.GetMorganFingerprintAsBitVect(m, 2, nBits=1024).ToBitString()
            except:
                isInChiFailed = True
        if isInChiFailed:
            print("%s\tBoth Failed" % (comp))
            failureCount += 1
        else:
            compound_ecfp4_vectors.write("%s\t%s\n" % (comp, fp))
        """

        if not isSmilesFailed:
            print(comp + "\t" + "\t".join([str(float(dim)) for dim in fp]))
            #print("{}\t{}".format(comp, fp))
            #print("")
        else:
            print("Failed")

# create_ecfp4_fingerprint_file()