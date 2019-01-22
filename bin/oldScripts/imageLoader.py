import os
training_files_path = "../trainingFiles"
result_files_path = "../resultFiles"

act_inact_fl = "act_inact_comps_10.0_20.0_chembl_preprocessed_sp_b_pchembl_data.txt"


def getFamilyBasedChEMBLIDS(trainedModelFile , family):
    families = ["enzyme", "gpcr", "ionchannel", "nuclearreceptor"]
    fam_chemblid_dict = dict()
    fam_chemblid_dict["others"] = set()
    chemblid_family_dict = dict()

    for fam in families:
        fam_chemblid_dict[fam] = set()
        fam_fl = open(os.path.join(training_files_path,"{}_targets.txt".format(fam)))
        lst_fam_fl = fam_fl.read().split("\n")
        fam_fl.close()
        while "" in lst_fam_fl:
            lst_fam_fl.remove("")

        for line in lst_fam_fl[1:]:
            chembl_id = line.split("\t")[0]
            chemblid_family_dict[chembl_id] = fam

    isFirst = True
    with open(os.path.join(result_files_path,trainedModelFile)) as f:
        for line in f:
            if isFirst:
                isFirst = False
            else:
                log_fl, modelname, target, optimizer, learning_rate, epoch, hidden1, hidden2, dropout, rotate, save_model, test_f1score, test_mcc, test_accuracy, test_precision, test_recall, test_tp, test_fp, test_tn, test_fn, test_threshold, val_auc, val_auprc, test_auc, test_auprc = line.split("\t")
                try:
                    fam_chemblid_dict[chemblid_family_dict[target]].add(target)
                except:
                    fam_chemblid_dict["others"].add(target)
    """
    for fam in families:
        print(len(fam_chemblid_dict[fam]))
    print(len(fam_chemblid_dict["others"]))
    """
    return list(fam_chemblid_dict[family])

#getFamilyBasedPerformances("ChEMBLBestModelResultsAll_v2.txt", "ionchannel")

def getActInactListForATarget(target, fl):
    act_list = []
    inact_list = []

    with open("{}/{}".format(training_files_path, fl))  as f:
        for line in f:
            if line != "":
                line=line.split("\n")[0]
                chembl_part, comps = line.split("\t")
                chembl_target_id, act_inact = chembl_part.split("_")
                if chembl_target_id == target:
                    if act_inact == "act":
                        act_list = comps.split(",")
                    else:
                        inact_list = comps.split(",")
                        break

    return act_list, inact_list



def getCompoundOverlap(family):
    target_chembl_id_list  = getFamilyBasedPerformances("ChEMBLBestModelResultsAll_v2.txt", family)
    target_act_dicts = dict()
    all_act_comps = set()
    for tar in target_chembl_id_list:
        act_comps, _ = getActInactListForATarget(tar, "act_inact_comps_10.0_20.0_chembl_preprocessed_sp_b_pchembl_data.txt")
        target_act_dicts[tar] = set(act_comps)
        print(tar, len(target_act_dicts[tar] ))
        all_act_comps = all_act_comps | target_act_dicts[tar]
        print(len(all_act_comps))

    for ind in range(len(target_chembl_id_list)):
        for ind2 in range(ind+1, len(target_chembl_id_list)):
            #print(len(target_act_dicts[target_chembl_id_list[ind]]&target_act_dicts[target_chembl_id_list[ind2]]))
            pass
    print(len(all_act_comps))

# getCompoundOverlap("gpcr")

def loadData():
    import torch
    from torchvision import transforms, datasets
    import matplotlib.pyplot as plt
    import cv2
    transform = transforms.Compose(
        [transforms.ToTensor(),
         transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    enzyme_dataset = datasets.ImageFolder(root='/Users/trman/OneDrive/Projects/DEEPScreen/tempImage/nuclearreceptor')
    print(len(enzyme_dataset))
    print(enzyme_dataset.classes)
    print(enzyme_dataset.__getitem__(10000))
    plt.imshow(enzyme_dataset.__getitem__(10000)[0])
    plt.show()
    dataset_loader = torch.utils.data.DataLoader(enzyme_dataset,
                                                 batch_size=4, shuffle=True,
                                                 num_workers=4, transform=transform)
    print(dataset_loader)


def seperateTrainingValidation():
    import os
    import random
    import subprocess
    families = ["enzyme", "gpcr", "ionchannel", "nuclearreceptor", "others"]
    for fam in families:
        fam_train_dataset_path = "/Users/trman/OneDrive/Projects/DEEPScreen/tempImage/FamilySpecificFigures/{}/train".format(fam)
        fam_val_dataset_path = "/Users/trman/OneDrive/Projects/DEEPScreen/tempImage/FamilySpecificFigures/{}/val".format(fam)
        for tar_folder in os.listdir(fam_train_dataset_path):
            if tar_folder.startswith("CHEMBL"):
                target_training_folder = os.path.join(fam_train_dataset_path, tar_folder)
                target_val_folder = os.path.join(fam_val_dataset_path, tar_folder)
                #print(target_val_folder)
                # "mkdir", target_val_folder
                subprocess.call(["mkdir", target_val_folder])

                lst_target_training_comps = os.listdir(target_training_folder)
                # print(lst_target_training_comps)
                random.shuffle(lst_target_training_comps)
                num_of_comps = len(lst_target_training_comps)
                training_size = int(num_of_comps*0.8)
                test_comps = lst_target_training_comps[training_size:]
                #print(training_size, len(test_comps), num_of_comps)
                for t_comp in test_comps:
                    subprocess.call(["mv",os.path.join(target_training_folder, t_comp), os.path.join(target_val_folder, t_comp)])
                    #print("mv", os.path.join(target_training_folder, t_comp), os.path.join(fam_val_dataset_path, t_comp))
                    # break
                #print(target_comp_list)



# seperateTrainingValidation()
# loadData()