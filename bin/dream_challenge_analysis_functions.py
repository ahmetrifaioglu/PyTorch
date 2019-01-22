datasets_path = "../trainingFiles/IDGDreamChallenge"
import pandas as pd
"""
awk -F ',' '{print $1}' idg_comp_targ_test.csv  > idg_train_test_comp_ids.txt
awk -F ',' '{print $1}' idg_comp_targ_uniq_inter_filtered.csv >> idg_train_test_comp_ids.txt

awk -F ',' '{print $2}' idg_comp_targ_test.csv  > idg_train_test_prot_ids.txt
awk -F ',' '{print $2}' idg_comp_targ_uniq_inter_filtered.csv  >> idg_train_test_prot_ids.txt

"""
def getMissingCompoundTargetIDs():
    fl_prot_ids = open("{}/{}".format(datasets_path, "idg_train_test_prot_ids.txt"))
    lst_prot_ids = fl_prot_ids.read().split("\n")
    fl_prot_ids.close()
    # lst_prot_ids.remove("")
    # print(lst_prot_ids)

    fl_comp_ids = open("{}/{}".format(datasets_path, "idg_train_test_comp_ids.txt"))
    lst_comp_ids = fl_comp_ids.read().split("\n")
    fl_comp_ids.close()


    set_all_comp_ids = set()
    set_all_prot_ids = set()
    fl_train = open("{}/{}/{}".format(datasets_path, "compound_feature_vectors", "ecfp4.tsv"))
    lst_train = fl_train.read().split("\n")
    fl_train.close()
    

    for line in lst_train:
        line_parts = line.split("\t")
        set_all_comp_ids.add(line_parts[0])


    fl_test = open("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/IDGDreamChallenge/DreamChallengeHeval/feature_vectors/APAAC.tsv", "r")
    lst_test = fl_test.read().split("\n")
    fl_test.close()


    for line in lst_test:
        line_parts = line.split("\t")
        set_all_prot_ids.add(line_parts[0])

    print(len(set(lst_prot_ids)))
    print(len(set(lst_prot_ids)&set_all_prot_ids))





# getMissingCompoundTargetIDs()