_base_ = "./resnest50d_AugCosyAAE_BG05_mlBCE_DoubleMask_visib10_ycbvRealKuwPbr_100e_01_02MasterChefCan_bop_test.py"
OUTPUT_DIR = (
    "output/DGNPose/ycbv/resnest50d_AugCosyAAE_BG05_mlBCE_DoubleMask_visib10_ycbvRealKuwPbr_100e_SO/02_03CrackerBox"
)
DATASETS = dict(TRAIN=("ycbv_003_cracker_box_train_real_aligned_Kuw", "ycbv_003_cracker_box_train_pbr"))
