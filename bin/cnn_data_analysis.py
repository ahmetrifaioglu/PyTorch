import pandas as pd
from torch.utils.data import Dataset, DataLoader, TensorDataset
import torch
import numpy as np
from torch.utils.data.sampler import SubsetRandomSampler, BatchSampler, SequentialSampler
import sklearn
from sklearn import preprocessing
import math

import itertools
import torch.nn as nn
from cnn_common_modules import get_prot_id_seq_dict_from_fasta_fl
import sys
from evaluation_metrics import get_scores_generic, get_list_of_scores

import os
cwd = os.getcwd()
training_files_path = "{}/../trainingFiles".format(cwd)

# training_data_name = "Davis"
#training_data_name = "Davis_Filtered"
#training_data_name = "KIBA"
training_data_name = "PDBBind_Refined"
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
    sorted_seq_len_list = sorted(seq_len_list, key=itemgetter(1))
    seq_len_list = [seq_len for prot_id, seq_len in sorted_seq_len_list]
    for prot_ind in range(len(seq_len_list)):
         print("{}\t{}\t{}".format(prot_ind, sorted_seq_len_list[prot_ind][0], sorted_seq_len_list[prot_ind][1]))
    return seq_len_list, seq_len_dict


def plot_seq_length_quad(fasta_fl_path, interval, dataset_name):
    import bokeh
    from bokeh.io import show, output_file
    from bokeh.plotting import figure
    from bokeh.models import ColumnDataSource, FixedTicker, PrintfTickFormatter
    from bokeh.io import export_svgs
    from bokeh.io import export_png
    from bokeh.models import HoverTool

    sorted_seq_len_list, _ = get_prot_seq_lengths_given_fasta(fasta_fl_path)
    tools = "pan,wheel_zoom,box_zoom,reset"
    p = figure(tools=tools, plot_width=1400, plot_height=700,
               title="Distribution of Sequence Lenghts - {} Dataset".format(dataset_name),
               x_axis_label='Sequence Length',
               y_axis_label='Number of Protein Sequences')


    p.title.text_font_size = '20pt'
    p.title.align = "center"
    # print((sorted_seq_len_list))
    arr_hist, edges = np.histogram(sorted_seq_len_list,
                                   bins=list(range(0, 2750, interval)),
                                   range=[0, 2750])

    delays = pd.DataFrame({'arr_length': arr_hist,
                           'left': edges[:-1],
                           'right': edges[1:]})
    delays['f_interval'] = ['%d - %d' % (left, right) for left, right in zip(delays['left'], delays['right'])]
    delays['f_count'] = ['%d' % (count) for count in delays['arr_length']]

    src = ColumnDataSource(delays)
    print(src.data.keys())
    p.quad(bottom=0, left="left", right="right", top="arr_length",  source=src,
           fill_color='red', line_color='black')

    hover = HoverTool(tooltips=[('Sequence Length', '@f_interval'), ('Count', '@f_count')])
    p.add_tools(hover)

    p.xgrid.grid_line_color = None
    # p.x_range.start = 0
    p.y_range.start = 0
    p.xaxis.axis_label = 'Sequence Length'
    p.xaxis.axis_label_text_font_size = "20pt"
    p.xaxis.major_label_text_font_size = "15pt"
    p.yaxis.axis_label = 'Number of Protein Sequences'
    p.yaxis.axis_label_text_font_size = "20pt"
    p.yaxis.major_label_text_font_size = "15pt"

    show(p)
    p.output_backend = "svg"
    export_svgs(p, filename="../figures/{}_{}_seq_length_dist.svg".format(dataset_name, interval))
    export_png(p, filename="../figures/{}_{}_seq_length_dist.png".format(dataset_name, interval))

# plot_seq_length_quad("{}/targets.fasta".format(helper_fl_path), 50, training_data_name)

def plot_bioact_dist_quad(fasta_fl_path, interval, dataset_name):
    import bokeh
    from bokeh.io import show, output_file
    from bokeh.plotting import figure
    from bokeh.models import ColumnDataSource, FixedTicker, PrintfTickFormatter
    from bokeh.io import export_svgs
    from bokeh.io import export_png
    from bokeh.models import HoverTool
    from bokeh.models import SingleIntervalTicker, LinearAxis

    df_bioactivity = pd.read_csv("{}/comp_targ_affinity.csv".format(comp_tar_training_dataset_path), header=None)
    sorted_bioactivities_list = sorted(df_bioactivity.iloc[:,2].values)

    tools = "pan,wheel_zoom,box_zoom,reset"
    p = figure(tools=tools, plot_width=1400, plot_height=700,
               title="Distribution of Bioactivity Values - {} Dataset".format(dataset_name),
               # x_axis_label='Bioacitivity Value (-log(Ki/Kd))',
               y_axis_label='Number of Bioactivities')

    p.title.text_font_size = '20pt'
    p.title.align = "center"

    # print((sorted_seq_len_list))
    arr_hist, edges = np.histogram(sorted_bioactivities_list,
                                   bins=list(np.arange(5, 12.0, interval)),
                                   range=[5, 12.0])

    delays = pd.DataFrame({'arr_length': arr_hist,
                           'left': edges[:-1],
                           'right': edges[1:]})
    delays['f_interval'] = ['%d - %d' % (left, right) for left, right in zip(delays['left'], delays['right'])]
    delays['f_count'] = ['%d' % (count) for count in delays['arr_length']]

    src = ColumnDataSource(delays)
    print(src.data.keys())
    p.quad(bottom=0, left="left", right="right", top="arr_length",  source=src,
           fill_color='red', line_color='black')

    hover = HoverTool(tooltips=[('Bioactivity Value Range', '@f_interval'), ('Count', '@f_count')])
    p.add_tools(hover)

    p.xgrid.grid_line_color = None
    # p.x_range.start = 0
    p.y_range.start = 0
    ticker = SingleIntervalTicker(interval=interval, num_minor_ticks=5)
    p.xaxis.ticker = ticker
    #xaxis = LinearAxis(ticker=ticker)
    #p.xaxis
    p.xaxis.axis_label = 'Bioacitivity Value (-log(Ki/Kd))'
    p.xaxis.axis_label_text_font_size = "20pt"
    p.xaxis.major_label_text_font_size = "10pt"
    p.yaxis.axis_label = 'Number of Bioactivities'
    p.yaxis.axis_label_text_font_size = "20pt"
    p.yaxis.major_label_text_font_size = "15pt"

    show(p)

    p.output_backend = "svg"
    export_svgs(p, filename="../figures/{}_{}_bioact_val_dist.svg".format(dataset_name, interval))
    export_png(p, filename="../figures/{}_{}_bioact_val_dist.png".format(dataset_name, interval))


# plot_bioact_dist_quad("{}/targets.fasta".format(helper_fl_path), 0.25, training_data_name)

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





def draw_distribution_of_contacts():
    import os
    import zipfile
    from bokeh.plotting import figure, output_file, show
    import numpy as np
    with zipfile.ZipFile('/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/target_feature_vectors/aadistancematrix500.zip') as z:
        for dist_fl_name in z.namelist():
            if not os.path.isdir(dist_fl_name) and dist_fl_name.endswith("tsv"):
                print(dist_fl_name)
                dist_lst = []
                prot_id = dist_fl_name.split(".")[0]
                #dist_fl = open("{}/{}".format(dist_folder_path, dist_fl_name), "r")
                with z.open(dist_fl_name) as f:
                    row_ind = 0
                    for line in f:
                        col_values = str(line).split("\\t")
                        # print(col_values)

                        for col_ind in range(len(col_values)):
                            dist = 0
                            if col_ind > row_ind:
                                if col_ind==row_ind or (col_ind!=row_ind and col_values[col_ind]!="0.0"):
                                    try:
                                        dist = float(col_values[col_ind])
                                        dist_lst.append(dist)

                                    except:
                                        pass
                        row_ind += 1
                dist_lst = sorted(dist_lst)
                # print(dist_lst)
                output_file("line.html")

                p = figure(plot_width=400, plot_height=400)
                lst_indices = list(range(len(dist_lst)))

                # print(lst_indices)
                # add a circle renderer with a size, color, and alpha

                arr_hist, edges = np.histogram(dist_lst,
                                               bins=1000,
                                               range=[0.0, 1.0])

                # Put the information in a dataframe
                distances = pd.DataFrame({'arr_dist': arr_hist,
                                       'left': edges[:-1],
                                       'right': edges[1:]})
                # print(distances)

                # Create the blank plot
                p = figure(plot_height=600, plot_width=600,
                           title='Histogram distances of aminoacids on 3D',
                           x_axis_label='Aminoacid pairs',
                           y_axis_label='Distance')

                # Add a quad glyph
                p.quad(bottom=0, top=distances['arr_dist'],
                       left=distances['left'], right=distances['right'],
                       fill_color='red', line_color='black')
                print(pd.DataFrame(dist_lst).describe())
                # Show the plot
                show(p)

                import numpy as np
                from scipy.stats import norm
                import matplotlib.pyplot as plt

                # Generate some data for this demonstration.
                data = np.asarray(dist_lst)
                print(type(data))
                # Fit a normal distribution to the data:
                mu, std = norm.fit(np.asarray(data))

                # Plot the histogram.
                plt.hist(data, bins=100, density=True, alpha=0.6, color='g')

                # Plot the PDF.
                xmin, xmax = plt.xlim()
                x = np.linspace(xmin, xmax, 100)
                p = norm.pdf(x, mu, std)
                plt.plot(x, p, 'k', linewidth=2)
                title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
                plt.title(title)

                plt.show()


# draw_distribution_of_contacts()

def calculate_performances_for_deepchem_pdbind():
    df_predictions = pd.read_csv("{}/PDBBind_Refined/helper_files/refined_report.csv".format(training_files_path),
                                 sep=",")

    lst_methods = df_predictions.columns.values[3:]
    for method in lst_methods:

        method_specific_predictions = df_predictions.loc[:,["id", "assign", "-logKd/Ki", method]].dropna()
        method_specific_test_predictions = method_specific_predictions.loc[method_specific_predictions['assign'] == "test"]
        labels_values =np.asarray(method_specific_test_predictions["-logKd/Ki"].values, dtype=float)
        predictions = np.asarray(method_specific_test_predictions[method].values, dtype=float)
        # print(labels_values[:10])
        # print(predictions[:10])
        print("======================== METHOD: {} ======================== ".format(method))
        get_scores_generic(labels_values, predictions, "test", True)




# calculate_performances_for_deepchem_pdbind()

def calculate_performances_for_simboost():
    from evaluation_metrics import get_validation_test_metric_list_of_scores

    result_file_path = "../result_files/simboost_predictions/Davis_Filtered"

    for i in range(3):
        # print(i)
        df_predictions = pd.read_csv("{}/test_pred_fold_{}_.csv".format(result_file_path, i+1),
                                     sep=",")

        df_labels = pd.read_csv("{}/test_label_fold_{}_.csv".format(result_file_path, i+1),
                                     sep=",")

        predictions = list(df_predictions.loc[:, "x"])
        labels_values = list(df_labels.loc[:, "x"])
        # print(predictions)
        get_scores_generic(labels_values, predictions, "test", True)

# calculate_performances_for_simboost()

def plot_predicted_vs_real_figures(method_name, dataset_name):
    from bokeh.plotting import figure, show, output_file
    import numpy as np
    from bokeh.io import export_svgs
    from bokeh.io import export_png
    method_name_corrected = ""
    method_name_corrected = "MDeePred" if method_name=="mbapred" else method_name_corrected
    method_name_corrected = "DeepDTA" if method_name == "deepdta" else method_name_corrected
    method_name_corrected = "SimBoost" if method_name == "simboost" else method_name_corrected
    method_name_corrected = "CGKronRLS" if method_name == "simboost" else method_name_corrected

    df = pd.read_csv("../result_files/{}_predictions/{}/{}_test_label_predicted_fold_1.tsv".format(method_name, dataset_name, method_name), sep="\t")
    # print(df)
    p = figure(plot_width=1400, plot_height=1400, title="{} - {}".format(method_name_corrected, dataset_name))
    p.circle(df["Label"], df["Pred"], size=20, color="navy", alpha=0.5)
    p.line(list(np.arange(2.0,11.0, 0.5)),list(np.arange(2.0,11.0, 0.5)), line_color='red', line_width=5, line_dash="dashed")

    p.xaxis.axis_label = 'Measured Bioactivity Value (pKd)'
    p.xaxis.axis_label_text_font_size = "40pt"
    p.xaxis.major_label_text_font_size = "40pt"
    p.yaxis.axis_label = 'Predicted Bioactivity Value (pKd)'
    p.yaxis.axis_label_text_font_size = "40pt"
    p.yaxis.major_label_text_font_size = "40pt"
    p.title.text_font_size = '40pt'
    p.title.align = "center"
    show(p)
    p.output_backend = "svg"
    export_svgs(p, filename="../figures/{}_{}_measured_predicted.svg".format(method_name, dataset_name))
    export_png(p, filename="../figures/{}_{}_measured_predicted.png".format(method_name, dataset_name))

# plot_predicted_vs_real_figures("mbapred", "Davis_Filtered")
# plot_predicted_vs_real_figures("mbapred", "Davis")
# plot_predicted_vs_real_figures("mbapred", "PDBBind_Refined")

# plot_predicted_vs_real_figures("deepdta", "Davis_Filtered")
# plot_predicted_vs_real_figures("deepdta", "Davis")

# plot_predicted_vs_real_figures("simboost", "Davis")

# plot_predicted_vs_real_figures("mbapred", "kinome")
# plot_predicted_vs_real_figures("mbapred", "PDBBind_Refined")

def add_channel_column_to_results(results_fl_path):
    fl_results = open("../result_files/pdbbind_refined_different_channel_perf_results_combined.txt", "r")
    lst_fl_results = fl_results.read().split("\n")
    fl_results.close()
    for line in lst_fl_results:
        cols  = line.split("\t")
        if "Inception" in cols[0]:
            features = cols[0].split("ecfp4-")[1].split("-")[0]
            print("{}\t{}".format(features, "\t".join(cols)))

# add_channel_column_to_results("")

def plot_performance_results_based_on_channels():
    from bokeh.plotting import figure, show, output_file
    import numpy as np
    from bokeh.io import export_svgs
    from bokeh.io import export_png
    from bokeh.io import show, output_file
    from bokeh.models import ColumnDataSource
    from bokeh.palettes import Spectral7
    from bokeh.transform import factor_cmap


    output_file("colormapped_bars.html")

    """
    encoding_ZHAC000103_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500
    sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500
    sequencematrix500_ZHAC000103LEQ500_blosum62LEQ500
    sequencematrix500_GRAR740104LEQ500_SIMK990101LEQ500
    sequencematrix500_GRAR740104LEQ500_blosum62LEQ500
    sequencematrix500_blosum62LEQ500
    sequencematrix500
    """

    fruits = ["proposed_encoding+ZHAC000103+GRAR740104+SIMK990101+blosum62", "proposed_encoding+GRAR740104+SIMK990101", "proposed_encoding+ZHAC000103+blosum62", "proposed_encoding+GRAR740104+blosum62", "proposed_encoding+ZHAC000103+GRAR740104",  "proposed_encoding+blosum62", "proposed_encoding"]
    #fruits = ["encoding_ZHAC000103_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500", "2",
    #          "3", "4",
    #          "5", "6", "7"]
    counts = [2.494448545, 2.532216751, 2.563455896, 2.625423895, 2.635092517,  2.653060487, 2.695833344]

    source = ColumnDataSource(data=dict(fruits=fruits, counts=counts))

    p = figure(x_range=fruits, plot_height=1500, plot_width=2800, toolbar_location=None, title="")
    p.vbar(x='fruits', top='counts', width=0.9, source=source,
           line_color='white', legend="fruits", fill_color=factor_cmap('fruits', palette=Spectral7, factors=fruits))

    p.xgrid.grid_line_color = None
    p.y_range.start = 2.45
    p.y_range.end = 2.75
    p.xaxis.axis_label = 'Input Channel'
    p.xaxis.axis_label_text_font_size = "30pt"
    p.xaxis.major_label_text_font_size = "30pt"
    p.yaxis.axis_label = 'Mean Squared Error'
    p.yaxis.axis_label_text_font_size = "30pt"
    p.yaxis.major_label_text_font_size = "30pt"
    p.title.text_font_size = '30pt'
    p.title.align = "center"
    p.legend.label_text_font_size = "20pt"

    p.xaxis.major_label_text_font_size = '0pt'
    # p.legend.location = (660, 0)
    # p.legend.orientation = "horizontal"
    # p.legend.location = "top_center"

    show(p)

    p.output_backend = "svg"
    export_svgs(p, filename="../figures/pdbbind_refined_channel_error_bars.svg")
    export_png(p, filename="../figures/pdbbind_refined_channel_error_bars.png")

# plot_performance_results_based_on_channels()

def get_human_kinome_target_ids_chembl_ids_dict():
    kinome_chembl_sing_prot_uniprot_dict = dict()
    kinome_uniprot_chembl_sing_prot_dict = dict()
    uniprot_chembl_mapping_fl = open("../trainingFiles/others/chembl25_uniprot_mapping.txt")
    lst_uniprot_chembl_mapping_fl  = uniprot_chembl_mapping_fl.read().split("\n")
    uniprot_chembl_mapping_fl.close()

    for line in lst_uniprot_chembl_mapping_fl[1:-1]:
        uniprot_id, chembl_id, name, t_type = line.split("\t")
        if t_type == "SINGLE PROTEIN":
            kinome_chembl_sing_prot_uniprot_dict[chembl_id] = uniprot_id
            kinome_uniprot_chembl_sing_prot_dict[uniprot_id] = chembl_id
    # print(kinome_chembl_sing_prot_uniprot_dict)
    human_kinome_uniprot_id_fl = open("../trainingFiles/others/human_kinome_target_ids.tab")
    lst_human_kinome_uniprot_id = human_kinome_uniprot_id_fl.read().split("\n")
    human_kinome_uniprot_id_fl.close()

    human_kinome_available_chembl_id_dict = dict()
    for line in lst_human_kinome_uniprot_id[1:-1]:
        uniprot_id, entry_name, gene_names, status, length = line.split("\t")

        if uniprot_id in kinome_uniprot_chembl_sing_prot_dict:
            human_kinome_available_chembl_id_dict[kinome_uniprot_chembl_sing_prot_dict[uniprot_id]] = 0
    return human_kinome_available_chembl_id_dict, kinome_chembl_sing_prot_uniprot_dict

# print(len(get_human_kinome_target_ids_chembl_ids_dict()))

def get_chemblid_smiles_dict():
    isFirst = True
    prob_count = 0
    # there should be a header in the smiles file
    compound_smiles_dict = dict()
    # print("DENEME../trainingFiles/{}".format(rep_fl))
    with open("/Users/trman/Downloads/chembl_25_chemreps.txt") as f:
        for line in f:
            if isFirst:
                isFirst = False
            else:
                # print(line)
                line = line.split("\n")[0]
                temp_parts = line.split("\t")
                # print(temp_parts)
                chembl_id, smiles = temp_parts[0], temp_parts[1]
                # chembl_id, smiles, _, _ = line.split("\t")
                # print(chembl_id, smiles)
                compound_smiles_dict[chembl_id] = smiles
    return compound_smiles_dict

def get_bioactivities_for_aval_human_kinome():
    import pandas as pd
    import math
    human_kinome_available_chembl_id_dict, kinome_chembl_sing_prot_uniprot_dict = get_human_kinome_target_ids_chembl_ids_dict()

    df_bioact_data = pd.read_csv("../../Bioactivity-Space-Visualization-Data-Analysis/inputFiles/chembl25_preprocessed_sp_b_pchembl_data.txt" , sep = "\t", index_col=False)
    for ind, row in df_bioact_data.iterrows():
        if row["Target_CHEMBL_ID"] in human_kinome_available_chembl_id_dict:
            human_kinome_available_chembl_id_dict[row["Target_CHEMBL_ID"]] += 1
            print("{},{},{}".format(row["Target_CHEMBL_ID"], row["Compound_CHEMBL_ID"], -1*math.log10(row["standard_value"]*(10**-6))))

    """
    # This part is used to create human_kinome_chembl_bioact_count file under helper files.
    # ../trainingFiles/kinome/helper_files/human_kinome_chembl_bioact_count.tsv
    print("ChEMBLID\tcount")
    for key in human_kinome_available_chembl_id_dict:
        print("{}\t{}".format(key, human_kinome_available_chembl_id_dict[key]))
    """
    """
    bioact_data_fl = open("../../Bioactivity-Space-Visualization-Data-Analysis/inputFiles/chembl25_preprocessed_sp_b_pchembl_data.txt", "r")
    lst_bioact_data = bioact_data_fl.read().split("\n")
    bioact_data_fl.close()
    for line in lst_bioact_data:
        print(line)
    """

# get_biaoctivities_for_aval_human_kinome()

def cluster_fps(fps,cutoff=0.2):
    from rdkit import DataStructs
    from rdkit.ML.Cluster import Butina

    # first generate the distance matrix:
    dists = []
    nfps = len(fps)
    # print(fps)
    for i in range(1,nfps):
        sims = DataStructs.BulkTanimotoSimilarity(fps[i],fps[:i])
        dists.extend([1-x for x in sims])

    # now cluster the data:
    cs = Butina.ClusterData(dists,nfps,cutoff,isDistData=True)
    return cs

def cluster_compounds():
    import pandas as pd
    import rdkit
    from rdkit.Chem import AllChem
    from rdkit import Chem
    chembl25_smiles_dict = get_chemblid_smiles_dict()
    df_kinome_biact = pd.read_csv("/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/PyTorch/trainingFiles/kinome/dti_datasets/comp_targ_affinity.csv", header = None)
    set_target_ids = set(df_kinome_biact[0])
    # print(set_target_ids)
    grouped_by_target_ids = df_kinome_biact.groupby([0])
    prob_count = 0
    original_total = 0
    clustered_total  = 0

    for target in set_target_ids:
        lst_target_comp_ids = list(grouped_by_target_ids.get_group(target)[1])
        fingerprints = []
        valid_comp_ids = []
        for comp_id in lst_target_comp_ids:
            try:
                sml = chembl25_smiles_dict[comp_id]
                #print(sml)
                m1 = Chem.MolFromSmiles(sml)

                fp1 = AllChem.GetMorganFingerprintAsBitVect(m1, 2,1024)
                #print(fp1)
                fingerprints.append(fp1)
                valid_comp_ids.append(comp_id)

            except:
                prob_count += 1
        clusters = cluster_fps(fingerprints, cutoff=0.3)
        original_total += len(fingerprints)
        clustered_total += len(clusters)
        # print(len(fingerprints), len(clusters))
        # print(clusters)
        for clust in clusters:
            rep_comp_ind = clust[0]
            bioact_val = float(df_kinome_biact[(df_kinome_biact[0] ==target) & (df_kinome_biact[1] == valid_comp_ids[rep_comp_ind]) ][2])
            # print(row)
            print("{},{},{}".format(target, valid_comp_ids[rep_comp_ind], bioact_val))

    # print(original_total, clustered_total)

    # print(prob_count)
        # print(lst_target_comp_ids)

# cluster_compounds()

def analyze_kinase_predictions():
    df_preprocessed_chembl25 = pd.read_csv("/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/Bioactivity-Space-Visualization-Data-Analysis/inputFiles/chembl25_preprocessed_sp_b_pchembl_data.txt", sep="\t", index_col=False)
    # print(df_preprocessed_chembl25)
    df_prediction_file = pd.read_csv("/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/PyTorch/result_files/mbapred_kinase_model_predictions_four_drug.tsv", sep="\t")
    # Drug Name	Gene Names	Entry Name	Target UniProt ID	Target ChEMBL ID	Predicted Value
    drug_name_dict = {"Rapamycin":"CHEMBL413", "BEZ235":"CHEMBL1879463", "Alsterpaullone":"CHEMBL50894", "Staurosporine":"CHEMBL388978"}
    for ind, row in df_prediction_file.iterrows():
        tar_chem_id = row["Target ChEMBL ID"]
        drug_name = row["Drug Name"]
        comp_chembl_id = drug_name_dict[drug_name]
        prediction = row["Predicted Value"]
        chembl25_row = df_preprocessed_chembl25[((df_preprocessed_chembl25['Target_CHEMBL_ID'] == tar_chem_id) & (df_preprocessed_chembl25['Compound_CHEMBL_ID'] == comp_chembl_id))]


        if not chembl25_row.empty:
            measured_value = chembl25_row["standard_value"]
            measured_value = str(measured_value.values.tolist()[0])
            lst_parts = [str(part) for part in row.values.tolist()]
            lst_parts.append(measured_value)
            print("\t".join(lst_parts))
        else:
            lst_parts = [str(part) for part in row.values.tolist()]
            print("\t".join(lst_parts))
        # Target_CHEMBL_ID	Compound_CHEMBL_ID

# analyze_kinase_predictions()


def produce_final_accr_predictions():
    import pandas as pd
    five_fold_pred_df = pd.read_csv("../result_files/aacr_drugs_five_fold_prediction.tsv", sep="\t")
    human_kinome_target_ids_df = pd.read_csv("../trainingFiles/others/human_kinome_target_ids.tab", sep="\t")
    print("DrugID\tTargetUniProtID\tTargetChEMBLID\tEntryName\tGeneNames\tPredictedBioactVal")
    for ind, row in five_fold_pred_df.iterrows():
        #print(row)
        #print(row["DrugID"])
        uniprot_id, chembl_id = row["TargetID"].split("_")
        entry_name = human_kinome_target_ids_df.loc[human_kinome_target_ids_df["Entry"]==uniprot_id]["Entry name"].values[0]
        gene_names = human_kinome_target_ids_df.loc[human_kinome_target_ids_df["Entry"]==uniprot_id]["Gene names"].values[0]
        predictions = [row["Fold{}".format(i+1)]for i in range(5)]
        #print(predictions)
        predictions = sorted(predictions)
        #print(predictions)
        if abs(predictions[2]-predictions[1])<0.25 and abs(predictions[2]-predictions[3])<0.25:
            print("{}\t{}\t{}\t{}\t{}\t{}".format(row["DrugID"], uniprot_id, chembl_id, entry_name, gene_names, (10**-row["Fold2"])*10**6))
        elif min(predictions)<5.0:
            print("{}\t{}\t{}\t{}\t{}\t{}".format(row["DrugID"], uniprot_id, chembl_id, entry_name, gene_names, (10**-min(predictions))*10**6))

produce_final_accr_predictions()