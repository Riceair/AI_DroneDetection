import os
import subprocess

def predictDarknet(img_name):
    cmd_command = "darknet detector test ../cfg_mask/obj.data ../cfg_mask/yolov4-custom.cfg ../cfg_mask/weights/yolov4-custom_final.weights\
                    -dont_show -ext_output ../dataset/public/"
    result = subprocess.check_output(cmd_command+img_name).decode("utf-8")
    #找到預測物件位置
    target_string = "milli-seconds."
    start_idx = result.find(target_string)
    pred_result = result[start_idx+len(target_string):]
    pred_result = pred_result.split("\r\n")[1:-1]

    #回傳預測物件
    label_name = ["car", "hov", "person", "motorcycle"]
    ## coord_location = left_x:, top_y, width, height
    coord_location = [3, 5, 7, 9]
    final_result = []
    for pred_obj in pred_result:
        pred_obj = pred_obj.replace(")","").replace(":","").split()
        obj_label = pred_obj[0]
        location = [pred_obj[i] for i in coord_location]
        
        for name in label_name:
            if name == obj_label:
                label = label_name.index(name)
        final_result.append([label]+location)
    return final_result