
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

    """
    metric_list = ['test rm2', 'test CI (DEEPDTA)', 'test MSE', 'test RMSE',
       'test Pearson', 'test Spearman', 'test CI (Challenge)',
       'test Average AUC', 'test Precision 5.0', 'test Recall 5.0',
       'test F1-Score 5.0', 'test Accuracy 5.0', 'test MCC 5.0',
       'test Precision 6.0', 'test Recall 6.0', 'test F1-Score 6.0',
       'test Accuracy 6.0', 'test MCC 6.0', 'test Precision 7.0',
       'test Recall 7.0', 'test F1-Score 7.0', 'test Accuracy 7.0',
       'test MCC 7.0', 'validation rm2', 'validation CI (DEEPDTA)',
       'validation MSE', 'validation RMSE', 'validation Pearson',
       'validation Spearman', 'validation CI (Challenge)',
       'validation Average AUC', 'validation Precision 5.0',
       'validation Recall 5.0', 'validation F1-Score 5.0',
       'validation Accuracy 5.0', 'validation MCC 5.0',
       'validation Precision 6.0', 'validation Recall 6.0',
       'validation F1-Score 6.0', 'validation Accuracy 6.0',
       'validation MCC 6.0', 'validation Precision 7.0',
       'validation Recall 7.0', 'validation F1-Score 7.0',
       'validation Accuracy 7.0', 'validation MCC 7.0']

    """

    metric_list = ['test rm2', 'test CI (DEEPDTA)', 'test MSE', 'test RMSE',
                   'test Pearson', 'test Spearman', 'test CI (Challenge)',
                   'test Average AUC',

                   'test Precision 10uM', 'test Recall 10uM',
                   'test F1-Score 10uM', 'test Accuracy 10uM', 'test MCC 10uM',

                   'test Precision 1uM', 'test Recall 1uM', 'test F1-Score 1uM',
                   'test Accuracy 1uM', 'test MCC 1uM',

                   'test Precision 100nM',
                   'test Recall 100nM', 'test F1-Score 100nM', 'test Accuracy 100nM',
                   'test MCC 100nM',

                   'test Precision 30nM',
                   'test Recall 30nM', 'test F1-Score 30nM', 'test Accuracy 30nM',
                   'test MCC 30nM',

                   'validation rm2', 'validation CI (DEEPDTA)',
                   'validation MSE', 'validation RMSE', 'validation Pearson',
                   'validation Spearman', 'validation CI (Challenge)',
                   'validation Average AUC',

                   'validation Precision 10uM',
                   'validation Recall 10uM', 'validation F1-Score 10uM',
                   'validation Accuracy 10uM', 'validation MCC 10uM',

                   'validation Precision 1uM', 'validation Recall 1uM',
                   'validation F1-Score 1uM', 'validation Accuracy 1uM',
                   'validation MCC 1uM',

                   'validation Precision 100nM',
                   'validation Recall 100nM', 'validation F1-Score 100nM',
                   'validation Accuracy 100nM', 'validation MCC 100nM',

                   'validation Precision 30nM',
                   'validation Recall 30nM', 'validation F1-Score 30nM',
                   'validation Accuracy 30nM', 'validation MCC 30nM'
                   ]

def get_5_fold_results():
    metric_list = ["test_deep_dta_rm2", "test_deep_dta_cindex", "test_deep_dta_mse", "test_pearson_score",
                   "test_spearman_score", "test_ci_score", "val_f1_score", "val_ave_auc_score"]

    str_header = "fl_name\tepoch_num"
    for metric in metric_list:
        str_header += "\t{}_mean\t{}_std".format(metric, metric)
    print(str_header)
    for fl in os.listdir(result_file_path):
        results_df  = pd.read_csv(os.path.join(result_file_path, fl), sep="\t")
        best_epoch_result_dict=dict()
        best_average_rmse = 1000000
        for ind, row in results_df.iterrows():
            mean_std_results_dict = dict()
            for metric in metric_list:
                fold_results = [float(rslt) for rslt in row[metric].split(",")]
                mean_rslt = statistics.mean(fold_results)
                stddev_rslt = statistics.pstdev(fold_results)
                #print(mean_rslt, stddev_rslt)
                mean_std_results_dict[metric] = (mean_rslt, stddev_rslt)


            if mean_std_results_dict["test_deep_dta_mse"][0] < best_average_rmse:
                for metric in metric_list:
                    best_epoch_result_dict[metric] = mean_std_results_dict[metric]
                best_epoch_result_dict["epoch_num"] = ind + 1

        str_result = "{}\t{}".format(fl,str(best_epoch_result_dict["epoch_num"]))
        for metric in metric_list:
            str_result += "\t{}\t{}".format(best_epoch_result_dict[metric][0], best_epoch_result_dict[metric][1])
        print(str_result)
#test_deep_dta_rm2	test_deep_dta_cindex	test_deep_dta_mse	test_pearson_score	test_spearman_score	test_ci_score	test_f1_score	test_ave_auc_score

# get_5_fold_results()
