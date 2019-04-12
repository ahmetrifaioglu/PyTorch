import statistics
import os
import pandas as pd
# result_file_path = "/Users/trman/OneDrive/Projects/PyTorch/resultFiles/1000_cnn_davis_results"
# result_file_path = "/Users/trman/OneDrive/Projects/PyTorch/resultFiles/corrected_davis_500_cnn_exp_results"
result_file_path = "/Users/trman/OneDrive/Projects/PyTorch/resultFiles/corrected_davis_1000_cnn_exp_results"
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
def get_full_training_results():
    metric_list = ["test_deep_dta_rm2", "test_deep_dta_cindex", "test_deep_dta_mse", "test_pearson_score",
                   "test_spearman_score", "test_ci_score", 	"test_f1_score","test_ave_auc_score"]

    str_header = "\t".join(["fl_name\tepoch_num", "\t".join(metric_list)])

    print(str_header)
    for fl in os.listdir(result_file_path):
        results_df = pd.read_csv(os.path.join(result_file_path, fl), sep="\t")
        best_epoch_result_dict = dict()
        best_rmse = 1000000
        best_epoch_num = -1


        for ind, row in results_df.iterrows():
            results_dict = dict()
            for metric in metric_list:
                results_dict[metric] = results_df[metric]

            if row["test_deep_dta_mse"] < best_rmse:
                for metric in metric_list:
                    best_epoch_result_dict[metric] = row[metric]
                    best_epoch_num = ind + 1
        #print(fl)
        #print(best_epoch_result_dict)
        str_result = "{}\t{}".format(fl, str(best_epoch_num))
        for metric in metric_list:
            str_result += "\t{}".format(best_epoch_result_dict[metric])
        print(str_result)

get_full_training_results()