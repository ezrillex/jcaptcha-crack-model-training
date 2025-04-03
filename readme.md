py -3.7 -m aocr train training.tfrecords --max-width=200 --max-height=70 --steps-per-checkpoint=100


py -3.7 -m aocr test testing.tfrecords --max-width=200 --max-height=70 

docker run -t --rm -p 8501:8501 -v "D:\\JCAPTCHA PROYECT\\images\\models\\jcaptcha-model:/models/jcaptcha-model" -e MODEL_NAME=jcaptcha-model tensorflow/serving

/root/code/jcaptcha-crack-model/jcaptcha-model

docker run -t -d --rm -p 127.0.0.1:8501 -v "/root/code/jcaptcha-crack-model/jcaptcha-model:/models/jcaptcha-model" -e MODEL_NAME=jcaptcha-model tensorflow/serving

docker run -t -d --restart unless-stopped -p 127.0.0.1:8501:8501 -v "/root/code/jcaptcha-crack-model/jcaptcha-model:/models/jcaptcha-model" -e MODEL_NAME=jcaptcha-model tensorflow/serving --rest_api_num_threads=1 --tensorflow_intra_op_parallelism=1 --tensorflow_inter_op_parallelism=1 --allow_version_labels_for_unavailable_models=false