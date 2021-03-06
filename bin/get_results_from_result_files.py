import statistics
import os
import pandas as pd
# result_file_path = "/Users/trman/OneDrive/Projects/PyTorch/resultFiles/1000_cnn_davis_results"
# result_file_path = "/Users/trman/OneDrive/Projects/PyTorch/resultFiles/corrected_davis_500_cnn_exp_results"



def get_5_fold_results_fold_thresholds():


    from evaluation_metrics import get_validation_test_metric_list_of_scores

    # result_file_path = "/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/PyTorch/result_files/davis_dataset_kansil_only_combined_best_encoding"
    result_file_path = "/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/PyTorch/result_files/davis_dataset_ebi_gpu_only_combined_best_encoding"
    result_file_path = "/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/PyTorch/result_files/davis_filtered_dataset_ebi_gpu_only_combined_best_encoding"
    result_file_path = "/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/PyTorch/log_files/kinome_five_fold_best"
    metric_list = get_validation_test_metric_list_of_scores()

    str_header = "fl_name\tepoch_num"
    for metric in metric_list:
        str_header += "\t{}_mean\t{}_std".format(metric, metric)
    print(str_header)
    for fl in os.listdir(result_file_path):
        if fl.endswith(".tsv"):
            results_df  = pd.read_csv(os.path.join(result_file_path, fl), sep="\t")

            best_metric_result_dict=dict()
            for metric in metric_list:
                if metric != "test MSE":
                    best_metric_result_dict[metric] = [-1,-1,-1,-1,-1]
                else:
                    best_metric_result_dict[metric] = [1000000, 1000000, 1000000, 1000000, 1000000]
            # print(best_metric_result_dict)
            for ind, row in results_df.iterrows():

                for metric in metric_list:
                    fold_results = [float(rslt) for rslt in row[metric].split(",")]
                    #print(fold_results)
                    for i in range(len(fold_results)):
                        if metric == "test MSE":
                            if fold_results[i]< best_metric_result_dict[metric][i]:
                                best_metric_result_dict[metric][i] = fold_results[i]
                        else:
                            if fold_results[i]> best_metric_result_dict[metric][i]:
                                best_metric_result_dict[metric][i] = fold_results[i]

            # print(best_metric_result_dict)
            mean_std_results_dict = dict()
            for metric in metric_list:
                mean_rslt = statistics.mean(best_metric_result_dict[metric])
                stddev_rslt = statistics.pstdev(best_metric_result_dict[metric])
                mean_std_results_dict[metric] = (mean_rslt, stddev_rslt)

            # print(mean_std_results_dict["test MSE"])
            str_result = "{}\t{}".format(fl,str(100))
            for metric in metric_list:
                str_result += "\t{}\t{}".format(mean_std_results_dict[metric][0], mean_std_results_dict[metric][1])
            print(str_result)


# get_5_fold_results_fold_thresholds()


def get_train_test_validation_setting_results():
    from evaluation_metrics import get_validation_test_metric_list_of_scores

    result_file_path = "/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/PyTorch/result_files/pdbbind_refined_dataset_kansil_combined_best_encodings"
    result_file_path = "/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/PyTorch/log_files/pdbbind_refined_dataset_ebi_gpu_only_combined_best_encoding"
    result_file_path = "/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/PyTorch/log_files/kinome_dataset_ebi_gpu_only_combined_best_encoding"

    validation_test_list = get_validation_test_metric_list_of_scores()
    # print(validation_test_list)
    str_header = "\t".join(["fl_name\thyperparams\tepoch_num", "\t".join(validation_test_list)])

    print(str_header)


    for fl in os.listdir(result_file_path):
        if fl.endswith("out"):
            result_fl = open(os.path.join(result_file_path, fl), "r")
            lst_result_fl = result_fl.read().split("\n")
            result_fl.close()
            # print(lst_result_fl[0])
            h_params = None
            dict_fl_best_results = dict()

            last_val_test_result_dict = dict()
            for mt in validation_test_list:
                last_val_test_result_dict[mt] = 10000000
            last_val_test_result_dict["epoch"] = -1

            for line in lst_result_fl:
                # set initial performance for the result file
                if line.startswith("Arguments: "):
                    h_params = line.split("Arguments: ")[1]
                    dict_fl_best_results[h_params] = dict()
                    for mt in validation_test_list:
                        dict_fl_best_results[h_params][mt] = 10000000
                    dict_fl_best_results[h_params]["epoch"] = -1

                # at each new epoch check the best val scores and reset the last_val_test_result_dict
                # dict_fl_best_result[h_params] if necessary
                elif line.startswith("Epoch:") and "validation Loss" in line:
                    epoch_num = int(line.split("\t")[0].split(":")[1]) -1


                    if last_val_test_result_dict["validation MSE"] < dict_fl_best_results[h_params]["validation MSE"]:
                        last_val_test_result_dict["epoch"] = epoch_num
                        dict_fl_best_results[h_params] = last_val_test_result_dict
                        # dict_fl_best_results[h_params]["epoch"] = epoch_num
                    last_val_test_result_dict = dict()
                    last_val_test_result_dict["epoch"] = -1

                elif line.startswith("validation") or line.startswith("test"):
                    metric_name, perf_value = line.split(":\t")
                    last_val_test_result_dict[metric_name] = float(perf_value)




            str_result = "{}\t{}\t{}".format(fl, h_params, dict_fl_best_results[h_params]["epoch"])
            for metric in validation_test_list:
                str_result += "\t{}".format(dict_fl_best_results[h_params][metric])

            print(str_result)

# get_train_test_validation_setting_results()



def get_five_fold_xval_results_from_logs():
    from evaluation_metrics import get_validation_test_metric_list_of_scores, get_validation_test_metric_list_of_scores_2

    result_file_path = "/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/PyTorch/result_files/pdbbind_refined_dataset_kansil_combined_best_encodings"
    result_file_path = "/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/PyTorch/log_files/pdbbind_refined_dataset_ebi_gpu_only_combined_best_encoding"
    result_file_path = "/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/PyTorch/log_files/kinome_dataset_ebi_gpu_only_combined_best_encoding"
    result_file_path = "/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/PyTorch/log_files/kinome_five_fold_best"
    result_file_path = "/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/PyTorch/log_files/ebi_kinome_top_2_logs"
    result_file_path = "/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/PyTorch/log_files/"
    #ebi_kinome_top_2_logs
    validation_test_list = get_validation_test_metric_list_of_scores_2()
    # print(validation_test_list)
    str_header = "\t".join(["fl_name\thyperparams\tfold\tepoch_num", "\t".join(validation_test_list)])
    dict_fl_best_results = dict()
    print(str_header)


    for fl in os.listdir(result_file_path):
        #if fl.endswith("out"):
        if fl=="31_5.out":
            # print(fl)
            result_fl = open(os.path.join(result_file_path, fl), "r")
            lst_result_fl = result_fl.read().split("\n")
            result_fl.close()
            # print(lst_result_fl[0])
            h_params = None


            last_val_test_result_dict = dict()
            for mt in validation_test_list:
                last_val_test_result_dict[mt] = 10000000
            last_val_test_result_dict["epoch"] = -1

            epoch_num = 100
            fold_num = 5

            for line in lst_result_fl:
                # set initial performance for the result file
                if line.startswith("Arguments:: "):
                    h_params = line.split("Arguments:: ")[1]
                    # h_params = "{}_{}".format(fl, h_params)
                    h_params = (fl, h_params)
                    dict_fl_best_results[h_params] = dict()



                # at each new epoch check the best val scores and reset the last_val_test_result_dict
                # dict_fl_best_result[h_params] if necessary
                elif line.startswith("Fold:") and "Validation Loss" in line:
                    fold_num = int(line.split("\t")[0].split(":")[1])
                    epoch_num = int(line.split("\t")[1].split(":")[1])
                    dict_fl_best_results[h_params][(fold_num,epoch_num)] = dict()
                    # print(fold_num, epoch_num)


                elif line.startswith("Validation") or line.startswith("Test"):
                    metric_name, perf_value = line.split(":\t")
                    dict_fl_best_results[h_params][(fold_num, epoch_num)][metric_name] = float(perf_value)



    # print(dict_fl_best_results.keys())
    # print(dict_fl_best_results["1024_512-256-512_256-0.0001-32-kinome-ecfp4-sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000-0-CompFCNNTarCNNModuleInception-0.25-kinome_dataset_ebi_gpu_only_combined_best_encoding"][(1,99)])



    for h_params in dict_fl_best_results:
        for fold_epoch in dict_fl_best_results[h_params]:
            # print(h_params)
            # print(fold_epoch)
            str_result = "{}\t{}\t{}\t{}".format(h_params[0], h_params[1], fold_epoch[0], fold_epoch[1])
            # print(str_result)
            # print(dict_fl_best_results[h_params][fold_epoch])

            for metric in validation_test_list:
                str_result += "\t{}".format(dict_fl_best_results[h_params][fold_epoch][metric])

            print(str_result)



get_five_fold_xval_results_from_logs()


def get_average_5_fold_results():
    import pandas as pd
    result_file = "/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/PyTorch/result_files/kinome_dataset_5_fold_ebi_gpu_only_combined_best_encoding_best_models.tsv"
    result_file = "/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/PyTorch/result_files/ebi_kinome_top_2_logs.tsv"
    df_result = pd.read_csv(result_file, sep="\t")
    fl_fold_dict = dict()
    for ind, row in df_result.iterrows():

        fl_name = row["fl_name"]
        hype_params = row["hyperparams"]
        fold_num = row["fold"]
        test_mse = row["Test MSE"]
        val_mse = row["Validation MSE"]
        epoch_num = row["epoch_num"]
        fl_name = hype_params[:-2]
        if  fl_name not in fl_fold_dict:
            fl_fold_dict[fl_name] = [[100, 100] for _ in range(5)]

        if val_mse < fl_fold_dict[fl_name][fold_num-1][0]:
            fl_fold_dict[fl_name][fold_num - 1][0] = test_mse
            fl_fold_dict[fl_name][fold_num - 1][1] = epoch_num

    for fl in fl_fold_dict:
        total_score = 0.0
        str_result = "{}".format(fl)
        for item in fl_fold_dict[fl]:
            str_result += "\t{}".format(item[0])
            str_result += "\t{}".format(item[1])
            total_score += item[0]
        str_result += "\t{}".format(total_score/5.0)
        print(str_result)

# get_average_5_fold_results()