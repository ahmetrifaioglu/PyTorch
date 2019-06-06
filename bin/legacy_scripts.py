
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