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

training_data_name = "DeepDTA_kiba"
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
    starting_dict = 0
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
    adj_interval_dist_list = [item - interval / 2 for item in interval_dist_list]
    print(count_list)
    p = figure(plot_width=1400, plot_height=700,
               title="Distribution of Sequence Lenghts - {} Dataset".format(dataset_name),
               toolbar_location=None, tools="")

    p.vbar(x=adj_interval_dist_list, top=count_list, width=40)

    p.xgrid.grid_line_color = None
    p.x_range.start = 0
    p.y_range.start = 0
    p.xaxis.axis_label = 'Sequence Length'
    p.xaxis.axis_label_text_font_size = "20pt"
    p.xaxis.major_label_text_font_size = "15pt"
    p.yaxis.axis_label = 'Number of Protein Sequences'
    p.yaxis.axis_label_text_font_size = "20pt"
    p.yaxis.major_label_text_font_size = "15pt"

    p.xaxis.ticker = FixedTicker(ticks=list(range(0, interval_step, 250)), minor_ticks=interval_dist_list)
    # p.minor_ticks = interval_dist_list
    show(p)
    p.output_backend = "svg"
    export_svgs(p, filename="../figures/{}_seq_length_dist.svg".format(dataset_name))
    export_png(p, filename="../figures/{}_seq_length_dist.png".format(dataset_name))


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
    export_svgs(p, filename="../figures/{}_seq_length_bioactivity_dist.svg".format(training_data_name))
    export_png(p, filename="../figures/{}_seq_length_bioactivity_dist.png".format(training_data_name))


get_number_of_bioactivity_distribution_based_on_seq_len()