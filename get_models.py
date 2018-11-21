import urllib.request


if __name__ == "__main__":
    caffe_model = "http://posefs1.perception.cs.cmu.edu/OpenPose/models/pose/coco/pose_iter_440000.caffemodel"
    prototxt = "https://raw.githubusercontent.com/CMU-Perceptual-Computing-Lab/openpose/master/models/pose/mpi" \
               "/pose_deploy_linevec.prototxt "
    print("Downloading Caffe Model")
    urllib.request.urlretrieve(caffe_model, 'stance/model/pose_iter_440000.caffemodel')
    print("Downloading Prototxt File")
    urllib.request.urlretrieve(prototxt, 'stance/model/pose_deploy_linevec.prototxt')
