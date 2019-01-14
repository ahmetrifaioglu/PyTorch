
import sys
from rdkit.Chem.AtomPairs import Torsions
from rdkit.Chem.Pharm2D import Generate

def getSMILEsFromFileWithHeader(rep_fl):
    isFirst = True
    prob_count = 0
    # there should be a header in the smiles file
    compound_smiles_dict = dict()
    # print("DENEME../trainingFiles/{}".format(rep_fl))
    #with open("/Users/trman/OneDrive/Projects/DEEPScreen/trainingFiles/{}".format(rep_fl)) as f:
    with open("/Users/trman/Desktop/DEEPScreen_19102018/trainingFiles/{}".format(rep_fl)) as f:
        for line in f:
            if isFirst:
                isFirst = False
            else:
                # print(line)
                line = line.split("\n")[0]
                temp_parts = line.split("\t")
                # print(temp_parts)
                chembl_id, smiles = temp_parts[0], temp_parts[1]
                #chembl_id, smiles, _, _ = line.split("\t")
                # print(chembl_id, smiles)
                compound_smiles_dict[chembl_id] = smiles
    return compound_smiles_dict

def training(feature_type):
    from rdkit.Chem import AllChem
    from rdkit import Chem

    feature_dict = dict()
    compound_smiles_dict = getSMILEsFromFileWithHeader("chembl_24_1_chemreps.txt")

    # print(compound_smiles_dict["CHEMBL3545297"])
    file_path = "/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/IDGDreamChallenge/Dtc_comp_targ_uniq_inter_filtered_onlykinase.txt"
    count =0
    nbits = 1024

    str_header = "compound id"
    for i in range(1024):
        str_header+="\t{}".format(i)
    print(str_header)

    with open(file_path) as f:
        for line in f:

            chembl_id = line.split(",")[0]
            found = False
            try:
                feature_dict[chembl_id]
                found = True

            except:
                pass

            if not found:
                try:
                    #print(count)
                    count = count + 1
                    feature_dict[chembl_id] = ""
                    smiles_str = compound_smiles_dict[chembl_id]
                    m1 = Chem.MolFromSmiles(smiles_str)
                    feature_values = None

                    if feature_type=="ecfp4":
                        feature_values = list(AllChem.GetMorganFingerprintAsBitVect(m1, 2, nBits=nbits))
                    elif feature_type=="rdk5":
                        feature_values = list(Chem.RDKFingerprint(m1, maxPath=5, fpSize=nbits, nBitsPerHash=2))
                    elif feature_type=="fcfp4":
                        feature_values = list(AllChem.GetMorganFingerprintAsBitVect(m1, 2, useFeatures=True,
                                                                                      nBits=nbits))


                    str_desc= "{}\t".format(chembl_id)
                    for item in feature_values[:-1]:
                        str_desc += str(item)+ "\t"
                    str_desc+= str(feature_values[-1])

                    print(str_desc)

                except:
                    pass


training("ecfp4")
"""
python generate_compound_descriptors.py > ../trainingFiles/IDGDreamChallenge/compound_feature_vectors/ecfp4.tsv
python generate_compound_descriptors.py > ../trainingFiles/IDGDreamChallenge/compound_feature_vectors/rdk5.tsv
python generate_compound_descriptors.py > ../trainingFiles/IDGDreamChallenge/compound_feature_vectors/fcfp4.tsv

"""


def test():
    from dataProcessing import getSMILEsFromFileWithHeader
    from rdkit.Chem import AllChem
    from rdkit import Chem
    ECFP4_dict = dict()
    file_path = "/Users/trman/OneDrive/Projects/PyTorch/bin/data/round_1_template.csv"
    count = 0
    with open(file_path) as f:
        for line in f:

            smiles_str = line.split(",")[0]
            compound_name = line.split(",")[2]

            found = False
            try:
                ECFP4_dict[compound_name]
                found = True
            except:
                pass
            if not found:
                try:
                    # print(count)
                    count = count + 1
                    ECFP4_dict[compound_name] = ""
                    m1 = Chem.MolFromSmiles(smiles_str)
                    ecp4 = list(AllChem.GetMorganFingerprintAsBitVect(m1, 2, nBits=1024))
                    str_desc = "{},".format(compound_name)
                    for item in ecp4[:-1]:
                        str_desc += str(item) + ","
                    str_desc += str(ecp4[-1])

                    print(str_desc)
                    # break
                except:
                    pass

#test()