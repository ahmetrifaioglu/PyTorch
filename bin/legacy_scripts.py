
# useless function
def create_ecfp4_feature_file_for_pdbbind():
    from rdkit import Chem
    """

    m = Chem.SDMolSupplier(path)
    m
    <rdkit.Chem.rdmolfiles.SDMolSupplier object at 0x1104adb90>
    # >>> print(mol.GetNumAtoms())


    # >>> print(m.GetNumAtoms())
    for mol in m:
    ...     print(mol)
    ...
    <rdkit.Chem.rdchem.Mol object at 0x11e2c7b70>
    # >>> for mol in m:
    # ...     print(mol.GetNumAtoms())
    :return:
    """
    path = "/Users/trman/Downloads/v2015"
    for folder in os.listdir(path):
        if os.path.isdir(os.path.join(path, folder)):
            for fl in os.listdir(os.path.join(path, folder)):
                if fl.endswith(".sdf"):
                    print(os.path.join(path, folder, fl))
                    try:

                        m = Chem.SDMolSupplier(os.path.join(path, folder, fl))
                        for mol in m:
                            print(mol.GetNumAtoms())
                    except:
                        pass
        # print(folder)
    return 0
# create_ecfp4_feature_file_for_pdbbind()


"""
import matplotlib.pyplot as plt
for key in dict_target_features.keys():
    #fig = plt.figure()
    print(dict_target_features[key].reshape(500,500).shape)
    plt.imshow(dict_target_features[key].reshape(500,500))
    plt.colorbar()
    # fig.show()
    plt.show()
"""


"""
for i, data in enumerate(train_loader):
    # get the inputs
    print(i)
    comp_feature_vectors, target_feature_vectors, labels, comp_ids, tar_ids = data
    print(target_feature_vectors.shape)
    print(comp_feature_vectors.shape)
"""
"""
loader_fold_dict, test_loader = get_cnn_test_val_folds_train_data_loader()
train_loader = loader_fold_dict[0][1]
for i, data in enumerate(train_loader):
    # get the inputs
    print(i)
    comp_feature_vectors, target_feature_vectors, labels, comp_ids, tar_ids = data
    print(target_feature_vectors.shape)
    print(comp_feature_vectors.shape)
"""


def get_scores_full(labels, predictions, validation_test, total_training_loss, total_validation_test_loss, epoch, comp_tar_pair_dataset, fold_epoch_results):
    deep_dta_rm2 = get_rm2(np.asarray(labels), np.asarray(
        predictions))
    # deep_dta_aupr = get_aupr(np.asarray(labels), np.asarray(
    #    predictions))
    deep_dta_cindex = get_cindex(np.asarray(labels), np.asarray(
        predictions))
    deep_dta_mse = mse(np.asarray(labels), np.asarray(
        predictions))

    rmse_score = rmse(np.asarray(labels), np.asarray(
        predictions))
    pearson_score = pearson(np.asarray(labels), np.asarray(predictions))
    spearman_score = spearman(np.asarray(labels), np.asarray(predictions))
    ci_score = ci(np.asarray(labels), np.asarray(predictions))
    prec_rec_f1_acc_mcc_threshold_dict = prec_rec_f1_acc_mcc(np.asarray(labels), np.asarray(predictions))
    ave_auc_score = average_AUC(np.asarray(labels), np.asarray(predictions))
    fold_epoch_results.append([deep_dta_rm2, deep_dta_cindex, deep_dta_mse, pearson_score, spearman_score, ci_score, f1_score, ave_auc_score])
    print("Epoch:{}\tTraining Loss:{}\t{} Loss:{}".format(epoch, total_training_loss, validation_test, total_validation_test_loss))
    print("{} RM2:\t{}".format(validation_test, deep_dta_rm2))
    print("{} MSE\t{}".format(validation_test, deep_dta_mse))
    print("{} RMSE\t{}".format(validation_test, rmse_score))
    print("{} c-index\t{}".format(validation_test, deep_dta_cindex))
    print("{} Pearson:\t{}".format(validation_test, pearson_score))
    print("{} Spearman:\t{}".format(validation_test, spearman_score))
    print("{} Ci:\t{}".format(validation_test, ci_score))
    print("{} Average_AUC:\t{}".format(validation_test, ave_auc_score))

    for key in prec_rec_f1_acc_mcc_threshold_dict.keys():
        print("{} {}:\t{}".format(validation_test, key, prec_rec_f1_acc_mcc_threshold_dict[key]))
