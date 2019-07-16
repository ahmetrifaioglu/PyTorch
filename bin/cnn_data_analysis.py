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
from cnn_common_modules import get_prot_id_seq_dict_from_fasta_fl
from evaluation_metrics import get_scores_generic

cwd = os.getcwd()
training_files_path = "{}/../trainingFiles".format(cwd)

# training_data_name = "Davis"
#training_data_name = "Davis_Filtered"
#training_data_name = "Kiba"
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
        get_scores_generic(labels_values, predictions, "test")
        #print(labels_values)
        #print(method_specific_test_predictions)




calculate_performances_for_deepchem_pdbind()