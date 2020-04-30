#!/bin/sh
python ../../main_training.py --td ACE2 --setting 2 --cf ecfp4 --tf sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000 --chln 1024_256 --tlnaf 128 --lhln 256_128 --lr 0.0001 --bs 32 --model CompFCNNTarCNNModuleInception --dropout 0.25 --en ACE2_model_training --epoch 200 --train_val_test 0
sleep 1
