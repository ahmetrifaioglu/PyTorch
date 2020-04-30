#!/bin/sh
python ../../main_training.py --td ACE2 --setting 2 --cf ecfp4 --tf sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000 --chln 512_512 --tlnaf 128 --lhln 256_128 --lr 0.0001 --bs 32 --model CompFCNNTarCNNModuleInception --dropout 0.1 --en ACE2_model_training --epoch 200 --train_val_test 0 --ext_test_feat_vec drugbank_ecfp4_normalized.tsv
sleep 1
