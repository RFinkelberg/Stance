# Stance
Determining the similarity between abstract scenes is a difficult problem in
cognitive computing. Humans can look at two images or videos and immediately
tell if they are similar, but this intuition is difficult to encode.


We present an application of 2D human pose estimation for accessing similarity between
motions in the space of weightlifting. Given input video of a person performing
an exercise, our system will access their form. That is, it will give a similarity
score between the user's motion and that motion performed "ideally".

## Installation
Clone the public repository

```commandline
git clone https://github.com/RFinkelberg/Stance.git
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies
```commandline
pip install -r requirements.txt
```

Download the neural net
```commandline
python get_models.py
```

## Quick Start
```commandline
cd stance/
python main.py -f example/squat.mp4
```

## Usage
```commandline
usage: main.py [-h] [-f VIDEO_PATH] [-v] [-p]

optional arguments:
  -h, --help            show this help message and exit
  -f VIDEO_PATH, --video_path VIDEO_PATH
                        filepath to video containing the user performing a
                        motion
  -v, --verbose         Verbosity level. 1 (v) displays info, 2 (vv) displays
                        debug logs
  -p, --use_pickle      uses the pickle file corresponding to the video file
                        given
```

## Using Pickle Files
There are three pickle files each containing precomputed skeletons for each
frame of the videos. To use, simply attach a "-p" to the end of the command 
with the relevant video file.

* example/squat.mp4
* example/squatbad.mp4
* example/squatpoop.mp4

```commandline
python main.py -f example/squatbad.mp4 -p
```

## Authors
* [Jorge Betancourt](https://github.com/jbeta51)
* [Roy Finkelberg](https://github.com/RFinkelberg)
* [Aadarsh Padiyath](https://github.com/aspadiyath)
* [Emilee Sisson](https://github.com/emileesisson)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

## Development
For more information on how we developed this project, check
out our [stance](https://aspadiyath.github.io/stance/stance.html) website. 