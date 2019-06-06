import pandas as pd
from torch.utils.data import Dataset, DataLoader, TensorDataset
import torch
import numpy as np
from torch.utils.data.sampler import SubsetRandomSampler, BatchSampler, SequentialSampler
import sklearn
from sklearn import preprocessing
import math
import os
import itertools
import torch.nn as nn
import sys
from dream_challenge_data_processing import get_prot_id_seq_dict_from_fasta_fl
cwd = os.getcwd()
training_files_path = "{}/../trainingFiles".format(cwd)

# training_data_name = "DeepDTA_davis"
# training_data_name = "DeepDTA_kiba"
training_data_name = "PDBBind"
compound_feature_list = "ecfp4".split("_")
target_feature_list = "sequencematrix1000".split("_")
compound_target_pair_dataset = "comp_targ_affinity.csv"

training_dataset_path = "{}/{}".format(training_files_path, training_data_name)
comp_tar_training_dataset_path = "{}/dti_datasets".format(training_dataset_path)
comp_feature_vector_path = "{}/compound_feature_vectors".format(training_dataset_path)
tar_feature_vector_path = "{}/target_feature_vectors".format(training_dataset_path)
helper_fl_path = "{}/helper_files".format(training_dataset_path)
data_path = "{}/data".format(training_dataset_path)
folds_path = "{}/data/folds".format(training_dataset_path)



def get_prot_seq_lengths_given_fasta(fasta_fl_path):
    from operator import itemgetter

    seq_len_dict = dict()
    prot_id_seq_dict = get_prot_id_seq_dict_from_fasta_fl(fasta_fl_path)
    seq_len_list = []
    for prot_id, seq in prot_id_seq_dict.items():
        seq_len_list.append([prot_id, len(seq)])
        seq_len_dict[prot_id] = len(seq)
    seq_len_list = sorted(seq_len_list, key=itemgetter(1))
    for prot_ind in range(len(seq_len_list)):
        print("{}\t{}\t{}".format(prot_ind, seq_len_list[prot_ind][0], seq_len_list[prot_ind][1]))
    return seq_len_list, seq_len_dict


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

def get_number_of_bioactivity_distribution_based_on_seq_len():
    import bokeh
    from bokeh.io import show, output_file
    from bokeh.plotting import figure
    from bokeh.models import ColumnDataSource, FixedTicker, PrintfTickFormatter
    from bokeh.io import export_svgs
    from bokeh.io import export_png

    seq_len_list, seq_len_dict = get_prot_seq_lengths_given_fasta("{}/targets.fasta".format(helper_fl_path))
    df_bioactivity = pd.read_csv("{}/comp_targ_affinity.csv".format(comp_tar_training_dataset_path), header=None)
    print(df_bioactivity)
    len_list = ["<=500", "501-1000", "1001-1500", ">1500"]
    count_list = [0, 0, 0, 0]
    for ind, row in df_bioactivity.iterrows():
        # print(row)
        comp_id = row[0]
        tar_id = row[1]
        seq_len = seq_len_dict[tar_id]
        if seq_len<=500:
            count_list[0] += 1
        elif seq_len>500  and seq_len<=1000:
            count_list[1] += 1
        elif seq_len>1000  and seq_len<=1500:
            count_list[2] += 1
        else:
            count_list[3] += 1
    print(count_list)

    p = figure(x_range=len_list,
               title="# of Bioactivities Based on Lengths of Sequences - Kiba Dataset",#.format(dataset_name),
               toolbar_location=None, tools="")

    p.xaxis.axis_label = 'Sequence Length'
    p.xaxis.axis_label_text_font_size = "20pt"
    p.xaxis.major_label_text_font_size = "15pt"
    p.yaxis.axis_label = 'Number of Bioactivities'
    p.yaxis.axis_label_text_font_size = "20pt"
    p.yaxis.major_label_text_font_size = "15pt"
    p.vbar(x=len_list, top=count_list, width=0.9)

    show(p)
    p.output_backend = "svg"
    export_svgs(p, filename="../figures/{}_{}_seq_length_dist.svg".format(dataset_name, interval))
    export_png(p, filename="../figures/{}_{}_seq_length_dist.png".format(dataset_name, interval))


# get_number_of_bioactivity_distribution_based_on_seq_len()


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
def get_seq_len_mean_vectors(interval, first_seq_num, first_error):
    #interval = 250
    interval_count_dict = {}
    interval_step = interval #interval * (int(first_seq_num[0] / interval) + 1)
    print(first_seq_num[-1], interval_step)
    interval_count_dict[interval_step] = []
    int_count = 0
    for seq_len_ind in range(len(first_seq_num)):
        # 0-50 51-100
        # print(first_seq_num[seq_len_ind])
        if first_seq_num[seq_len_ind] <= interval_step:
            # print(interval_step)
            interval_count_dict[interval_step].append(first_error[seq_len_ind])
            int_count += 1
            print("{}\t{}\t{}".format(interval_step, first_seq_num[seq_len_ind], first_error[seq_len_ind]))
        else:
            interval_step = interval * (int(first_seq_num[seq_len_ind] / interval) + 1)
            # interval_dist_list.append(int_count)
            interval_count_dict[interval_step] = [first_error[seq_len_ind]]
            print(" NEW {}\t{}\t{}".format(interval_step, first_seq_num[seq_len_ind], first_error[seq_len_ind]))

    interval_dist_list = []
    mean_list = []
    # print(interval_dist_list)
    starting_dict = interval
    print(interval_count_dict.keys())
    while starting_dict <= interval_step:
        if starting_dict not in interval_count_dict.keys():
            interval_count_dict[starting_dict] = 0.0
            interval_dist_list.append(starting_dict)
            mean_list.append(0.0)
        else:
            interval_dist_list.append(starting_dict)
            mean_list.append(sum(interval_count_dict[starting_dict]) / len(interval_count_dict[starting_dict]))
            interval_count_dict[starting_dict] = sum(interval_count_dict[starting_dict]) / len(
                interval_count_dict[starting_dict])
        starting_dict += interval
    return interval_dist_list, mean_list, interval_count_dict

def get_rmse_based_on_sequence_length():
    import os
    import math
    import pandas as pd
    import bokeh
    import numpy as np
    from operator import itemgetter
    from bokeh.plotting import figure, output_file, show
    from bokeh.models import ColumnDataSource, FixedTicker, PrintfTickFormatter
    from bokeh.io import export_svgs, export_png, show, output_file
    from bokeh.layouts import row
    from bokeh.core.properties import value
    from bokeh.models import ColumnDataSource
    from bokeh.transform import dodge

    seq_len_list, seq_len_dict = get_prot_seq_lengths_given_fasta("{}/targets.fasta".format(helper_fl_path))
    prediction_path_500 = "/Users/trman/OneDrive/Projects/PyTorch/resultFiles/davis_500_cnn_test_predictions"
    prediction_path_1000 = "/Users/trman/OneDrive/Projects/PyTorch/resultFiles/davis_1000_cnn_test_predictions"
    #for fl in os.listdir(prediction_path_1000):
    prediction_500_seq_len_error_list = []
    prediction_1000_seq_len_error_list = []


    #predictions_1000_df = pd.read_csv("{}/{}".format(prediction_path_1000, fl), sep="\t")
    predictions_1000_df = pd.read_csv("/Users/trman/OneDrive/Projects/PyTorch/resultFiles/davis_1000_cnn_test_predictions/128_1024_1024_0.005_16_DeepDTA_davis_full_prediction.tsv", sep="\t")
    for ind, row in predictions_1000_df.iterrows():
        tar_id = row["Tar_ID"]
        error = math.sqrt(math.fabs(row["Label"]-row["Prediction"]))
        prediction_1000_seq_len_error_list.append([seq_len_dict[tar_id], error])
    prediction_1000_seq_len_error_list = sorted(prediction_1000_seq_len_error_list, key=itemgetter(0))

    #other_fl = "{}_500.tsv".format(fl.split(".tsv")[0])
    #predictions_500_df = pd.read_csv("{}/{}".format(prediction_path_500, other_fl), sep="\t")

    predictions_500_df = pd.read_csv(
        "/Users/trman/OneDrive/Projects/PyTorch/resultFiles/davis_500_cnn_test_predictions/64_256_256_0.005_32_DeepDTA_davis_full_prediction_500.tsv",
        sep="\t")
    for ind, row in predictions_500_df.iterrows():
        tar_id = row["Tar_ID"]
        error = math.sqrt(math.fabs(row["Label"] - row["Prediction"]))
        prediction_500_seq_len_error_list.append([seq_len_dict[tar_id], error])
    prediction_500_seq_len_error_list = sorted(prediction_500_seq_len_error_list, key=itemgetter(0))



    seq_500_num = list(np.asarray(prediction_500_seq_len_error_list, dtype=int)[:,0])
    prediction_500_error = list(np.asarray(prediction_500_seq_len_error_list, dtype=float)[:, 1])

    seq_1000_num = list(np.asarray(prediction_1000_seq_len_error_list, dtype=int)[:, 0])
    prediction_1000_error = list(np.asarray(prediction_1000_seq_len_error_list, dtype=float)[:, 1])


    interval_500_dist_list, mean_500_list, interval_500_count_dict = get_seq_len_mean_vectors(500, seq_500_num, prediction_500_error)
    interval_1000_dist_list, mean_1000_list, interval_1000_count_dict = get_seq_len_mean_vectors(500,
                                                                                              seq_1000_num,
                                                                                              prediction_1000_error)


    # output_file("dodged_bars.html")

    seq_range = [str(item) for item in interval_500_dist_list]

    data = {'seq_range': seq_range}

    data["500"] = []
    for mean in mean_500_list:
        data["500"].append(mean)

    data["1000"] = []
    for mean in mean_1000_list:
        data["1000"].append(mean)

    print(data)

    source = ColumnDataSource(data=data)

    p = figure(x_range=seq_range,  plot_height=250, title="Error based on length of sequence",
               toolbar_location=None, tools="")

    p.vbar(x=dodge('seq_range', -0.25, range=p.x_range), top='500', width=0.2, source=source,
           color="#c9d9d3", legend=value("500"))

    p.vbar(x=dodge('seq_range', 0.0, range=p.x_range), top='1000', width=0.2, source=source,
           color="#718dbf", legend=value("1000"))

    #p.vbar(x=dodge('fruits', 0.25, range=p.x_range), top='2017', width=0.2, source=source,
    #       color="#e84d60", legend=value("2017"))

    p.x_range.range_padding = 0.1
    p.xgrid.grid_line_color = None
    p.legend.location = "bottom_right"
    p.legend.orientation = "horizontal"

    show(p)

# get_rmse_based_on_sequence_length()


def create_5_fold_train_test_folds():
    import pandas as pd
    from random import shuffle
    import math
    df_bioactivity = pd.read_csv("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/IDGDreamChallenge/dti_datasets/comp_targ_affinity.csv", header=None)
    shuffled_indices = list(range(len(df_bioactivity)))
    number_of_samples = len(shuffled_indices)
    shuffle(shuffled_indices)
    number_of_samples_each_fold = math.ceil(number_of_samples / 5)
    start = 0
    folds = []
    while start<number_of_samples:
        folds.append(shuffled_indices[start:start+number_of_samples_each_fold])
        start = start+number_of_samples_each_fold
    #for item in folds:
    #    print(len(item))
    # uncomment below line to create train_fold_setting1.txt
    # print(folds)
    # uncomment below line to create test
    print(folds[-1][:100])

#
# create_5_fold_train_test_folds()


def remove_bioactivities_with_no_ecfp4():
    import pandas as pd

    df_ecfp4 = pd.read_csv("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/IDGDreamChallenge/compound_feature_vectors/ecfp4_normalized.tsv", sep= "\t")
    df_ecfp4 = df_ecfp4["compound id"]
    lst_ecfp4 = list(df_ecfp4)
    dict_ecfp4 = dict()
    for item in lst_ecfp4:
        dict_ecfp4[item] = ""

    # print(len(dict_ecfp4.keys()))
    df_bioactivity = pd.read_csv(
        "/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/IDGDreamChallenge/dti_datasets/comp_targ_affinity_all_with_invalid_chembl_ids.csv",
        header=None)
    for ind, row in df_bioactivity.iterrows():
        # print(row)
        try:
            dict_ecfp4[row[0]]
            lst_row = [str(col) for col in list(row)]
            print(",".join(lst_row))
        except:
            pass
# remove_bioactivities_with_no_ecfp4()
