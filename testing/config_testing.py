config = {
    'data_path': '../datasets',
    # 'test_data_path': '../dataset_test', # for now it is not available
    'model_path': '../classification_model/model_res18', ##### '../model/res18_epoch', '../model/wasteCNN_epoch', '../model/CNN_epoch'
    # 'preprocess_result_path': '',
    'image_size': 128,  # 256
    'batch_size': 32,
#     'test_percentage': 0.2,
    'val_percentage': 0.2,
    'lr': 1e-3,
    'epoch': 50,
    'classifier_model': 'model',
#     'classifier_param': "../model/classifier.ckpt",
#     'skip_preprocessing': True
}

