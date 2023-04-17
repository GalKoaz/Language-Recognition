# Language-Recognition
Language Recognition 


## X vector torch
This repo contains the implementation of the paper "Spoken Language Recognition using X-vectors" in torch (Pytorch)

Paper: [2018 odyssey X vector lid](https://danielpovey.com/files/2018_odyssey_xvector_lid.pdf)

Tutorial : [X-vectors: Robust DNN embeddings for speaker recognition](https://www.youtube.com/watch?v=8nZjiXEdMH0)

Source repo : [X vector repository](https://github.com/KrishnaDN/x-vector-pytorch)

### Create manifest files for training and testing
This step creates training and testing files.
```Python
python datasets.py --processed_data  /media/newhd/youtube_lid_data/download_data --meta_store_path meta/ 
```


### Create and prepare the data
* Download data from commonVoice
* Convert with the Convertor.py script the .mp3 files to .wav by the following command:
```Python
python DataConvertor.py path_folder1 path_folder2
```
* Create the txt files with the CreateData.py script by the following command:
```Python
python DataCreator.py input_folder output_txt number_label
```
