#!/bin/sh
python ../../main_training.py --td kinome --setting 2 --cf ecfp4 --tf sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000 --chln 1024_512 --tlnaf 512 --lhln 1024_512 --lr 0.001 --bs 32 --model CompFCNNTarCNNModuleInception --dropout 0.1 --en kinase_model_training --epoch 200 --train_val_test True
sleep 1
