import json, os, shutil


def unpack(base_dir, 
           target_dir, 
           train='ILSVRC2012_img_train.tar',
           class_json='ImageNet_class_index.json'):
    
    # path
    train_dir = os.path.join(base_dir, train)
    json_dir  = os.path.join(base_dir, class_json)

    target_train_dir = os.path.join(target_dir, 'train')

    # dictionary for class to num
    class2num = {}
    with open(json_dir) as json_file:
        json_data = json.load(json_file)
        for num in json_data:
            class2num[json_data[num][0]] = num
    
    # unzip train dataset
    shutil.unpack_archive(train_dir, target_train_dir)
    for class_zip in sorted(os.listdir(target_train_dir)):
        class_, _ = class_zip.split('.')
        shutil.unpack_archive(os.path.join(target_train_dir, class_zip), 
                              os.path.join(target_train_dir, class2num[class_]))
        os.remove(os.path.join(target_train_dir, class_zip))
        

if __name__ == '__main__':
    base_dir   = '/Users/jason/Desktop/data'
    target_dir = '/Users/jason/Desktop/data/ImageNet'
    unpack(base_dir, target_dir)
