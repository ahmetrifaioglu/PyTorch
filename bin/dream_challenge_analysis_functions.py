datasets_path = "../trainingFiles/IDGDreamChallenge"
import pandas as pd
"""
awk -F ',' '{print $1}' idg_comp_targ_test.csv  > idg_train_test_comp_ids.txt
awk -F ',' '{print $1}' idg_comp_targ_uniq_inter_filtered.csv >> idg_train_test_comp_ids.txt

awk -F ',' '{print $2}' idg_comp_targ_test.csv  > idg_train_test_prot_ids.txt
awk -F ',' '{print $2}' idg_comp_targ_uniq_inter_filtered.csv  >> idg_train_test_prot_ids.txt

"""
def getAverageRMSEResult():
    import os
    import numpy as np
    file_dict_rmse = dict()
    file_dict_training_loss = dict()
    file_dict_val_loss = dict()
    result_file_path = "../resultFiles"
    for fl in os.listdir(result_file_path):
        if fl.startswith("ecfp4_trigram_best_result."):
            fl_id = fl.split("_")[1][0]
            file_dict_rmse[fl_id] = [[] for _ in range(5)]
            file_dict_training_loss[fl_id] = [[] for _ in range(5)]
            file_dict_val_loss[fl_id] = [[] for _ in range(5)]

            fl_result = open("{}/{}".format(result_file_path, fl) , "r")
            lst_result_fl = fl_result.read().split("\n")
            fl_result.close()
            for line in lst_result_fl:
                if line.startswith("Fold:"):
                    fold_id, epoch_id, rmse, training_loss, validation_loss = line.split("\t")
                    fold_id, epoch_id, rmse, training_loss, validation_loss = int(fold_id.split(":")[1]), \
                                                                              int(epoch_id.split(":")[1]), \
                                                                              float(rmse.split(":")[1]), \
                                                                              float(training_loss.split(":")[1]), \
                                                                              float(validation_loss.split(":")[1])
                    # print(fold_id, epoch_id, rmse, training_loss, validation_loss)
                    # print(line)
                    file_dict_rmse[fl_id][fold_id-1].append(rmse)
                    file_dict_training_loss[fl_id][fold_id - 1].append(training_loss)
                    file_dict_val_loss[fl_id][fold_id - 1].append(validation_loss)

    #print(len(file_dict_rmse["1"][4]))

    arr_all_mean_fold_rmse  = []
    arr_all_mean_fold_training = []
    arr_all_mean_fold_val = []

    for key in file_dict_rmse.keys():
        arr_mean_fold_rmse = np.array(file_dict_rmse[key]).mean(axis=0)
        arr_all_mean_fold_rmse.append(arr_mean_fold_rmse)

        arr_mean_fold_training = np.array(file_dict_training_loss[key]).mean(axis=0)
        arr_all_mean_fold_training.append(arr_mean_fold_training)

        arr_mean_fold_val = np.array(file_dict_val_loss[key]).mean(axis=0)
        arr_all_mean_fold_val.append(arr_mean_fold_val)

    arr_all_mean_fold_rmse = np.array(arr_all_mean_fold_rmse).mean(axis=0)
    arr_all_mean_fold_train = np.array(arr_all_mean_fold_training).mean(axis=0)
    arr_all_mean_fold_val = np.array(arr_all_mean_fold_val).mean(axis=0)

    for ind in range(len(arr_all_mean_fold_rmse)):
        print("{}\t{}\t{}\t{}".format(ind, arr_all_mean_fold_rmse[ind], arr_all_mean_fold_train[ind], arr_all_mean_fold_val[ind]))
    # print(arr_all_mean_fold_rmse)

getAverageRMSEResult()
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