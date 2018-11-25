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
python main.py -v example/squat.mp4
```

## Usage
```commandline
python main.py -v path/to/video/file.mp4
```

## Using Pickle Files
There are three pickle files each containing precomputed skeletons for each
frame of the videos. To use, simply attach a "-p" to the end of the command 
with the relevant video file.

* example/squat.mp4
* example/squatbad.mp4
* example/squatpoop.mp4

```commandline
python main.py -v example/squatbad.mp4 -p
```

## Authors
* Jorge Betancourt
* Roy Finkelberg
* Aadarsh Padiyath
* Emilee Sisson

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

## Etc
For more information on how we developed this project, check
out our [stance](https://aspadiyath.github.io/stance/stance.html) website. 