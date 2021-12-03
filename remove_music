from inaSpeechSegmenter import Segmenter
from inaSpeechSegmenter.export_funcs import seg2csv, seg2textgrid

media = './gaiman.mp3'

# create an instance of speech segmenter
# this loads neural networks and may last few seconds
# Warnings have no incidence on the results
seg = Segmenter(detect_gender=False, vad_engine='smn')

# segmentation is performed using the __call__ method of the segmenter instance
segmentation = seg(media)

# the result is a list of tuples
# each tuple contains:
# * label in 'male', 'female', 'music', 'noEnergy'
# * start time of the segment
# * end time of the segment
#print(segmentation)
for segment in segmentation:
    if segment[0] == 'music':
        print(str(segment[1]) + " to " + str(segment[2]))
