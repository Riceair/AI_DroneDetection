from predictDarknet import predictDarknet
from glob import glob
import csv
import os

img_folder = "dataset/public"
img_path = glob(img_folder+"/*")
img_names = [path.replace(img_folder,"").replace("\\","") for path in img_path]

# darknet prediction
os.chdir("darknet_gpu")
final_result = []
for img_name in img_names:
    pred_results = predictDarknet(img_name)
    save_form = [[img_name.replace(".png","")]+result for result in pred_results]
    final_result += save_form

with open('../output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for line in final_result:
        writer.writerow(line)