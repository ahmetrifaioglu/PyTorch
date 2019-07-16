
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

def plot_seq_length(fasta_fl_path, interval, dataset_name):
    import bokeh
    from bokeh.io import show, output_file
    from bokeh.plotting import figure
    from bokeh.models import ColumnDataSource, FixedTicker, PrintfTickFormatter
    from bokeh.io import export_svgs
    from bokeh.io import export_png

    seq_len_list, _ = get_prot_seq_lengths_given_fasta(fasta_fl_path)

    interval_count_dict = {}
    interval_step = interval * (int(seq_len_list[0][1] / interval) + 1)

    interval_count_dict[interval_step] = 0
    int_count = 0
    for prot_id, seq_len in seq_len_list:
        # 0-50 51-100
        if seq_len <= interval_step:
            int_count += 1
            # print("{}\t{}\t{}".format(prot_id, seq_len, interval_step))
        else:
            # interval_dist_list.append(int_count)
            interval_count_dict[interval_step] = int_count
            interval_step = interval * (int(seq_len / interval) + 1)
            int_count = 1
            #  print("{}\t{}\t{}".format(prot_id, seq_len, interval_step))
    interval_count_dict[interval_step] = int_count
    #  print(interval_count_dict)
    interval_dist_list = []
    count_list = []
    # print(interval_dist_list)
    starting_dict = interval
    while starting_dict <= interval_step:
        if starting_dict not in interval_count_dict.keys():
            interval_count_dict[starting_dict] = 0
            interval_dist_list.append(starting_dict)
            count_list.append(0)
        else:
            interval_dist_list.append(starting_dict)
            count_list.append(interval_count_dict[starting_dict])
        starting_dict += interval

    # print(sum(interval_dist_list))
    print(interval_count_dict)
    # print(interval_dist_list[-1])
    # interval_dist_list = [item for item in interval_dist_list]
    adj_interval_dist_list = interval_dist_list#[item - interval / 2 for item in interval_dist_list]
    print(count_list)
    len_list = ["<=500", "501-1000", "1001-1500", "1501-2000", "2001-2500", "2501-3000", "3001-3500", "3501-4000","4001-4500","4501-5000"]
    p = figure(x_range=len_list, plot_width=1400, plot_height=700,
               title="Distribution of Sequence Lenghts - {} Dataset".format(dataset_name),
               toolbar_location=None, tools="")

    p.vbar(x=len_list, top=count_list, width=0.9)

    p.xgrid.grid_line_color = None
    #p.x_range.start = 0
    p.y_range.start = 0
    p.xaxis.axis_label = 'Sequence Length'
    p.xaxis.axis_label_text_font_size = "20pt"
    p.xaxis.major_label_text_font_size = "15pt"
    p.yaxis.axis_label = 'Number of Protein Sequences'
    p.yaxis.axis_label_text_font_size = "20pt"
    p.yaxis.major_label_text_font_size = "15pt"

    # p.xaxis.ticker = FixedTicker(ticks=list(range(0, interval_step+1, interval)), minor_ticks=interval_dist_list)
    # p.minor_ticks = interval_dist_list
    show(p)
    p.output_backend = "svg"
    export_svgs(p, filename="../figures/{}_{}_seq_length_dist.svg".format(dataset_name, interval))
    export_png(p, filename="../figures/{}_{}_seq_length_dist.png".format(dataset_name, interval))

# plot_seq_length("{}/targets.fasta".format(helper_fl_path), 500, training_data_name)
# plot_seq_length("{}/targets.fasta".format(helper_fl_path), 500, training_data_name)


def convert_wrongly_created_result_files_into_proper_format(result_folder_name):
    import os
    # "davis_500_cnn_exp_results"
    for fl in os.listdir("../resultFiles/{}".format(result_folder_name)):
        str_fl = open("../resultFiles/{}/{}".format(result_folder_name,fl), "r")
        lst_fl= str_fl.read().split("\n")
        str_fl.close()
        corrected_fl = open("../resultFiles/corrected_{}/corrected_{}".format(result_folder_name, fl), "w")
        header = lst_fl[0]
        corrected_fl.write(header+ "\n")
        #print(lst_fl[1])
        fold_results_lst = lst_fl[1].split("\t")
        #print(fold_results_lst)
        for line in fold_results_lst:
            correct_line = "\t".join(line[1:-1].split(", "))
            corrected_fl.write("{}\n".format(correct_line))
            # print("\t".join(line[1:-1].split(", ")))
            #print(line)
        corrected_fl.close()


# convert_wrongly_created_result_files_into_proper_format("davis_500_cnn_exp_results")
# convert_wrongly_created_result_files_into_proper_format("davis_1000_cnn_exp_results")

