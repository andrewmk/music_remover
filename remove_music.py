from inaSpeechSegmenter import Segmenter
from inaSpeechSegmenter.export_funcs import seg2csv, seg2textgrid

media = './gaiman.mp3'

# create an instance of speech segmenter
# this loads neural networks and may last few seconds
# Warnings have no incidence on the results
###seg = Segmenter(detect_gender=False, vad_engine='smn')

# segmentation is performed using the __call__ method of the segmenter instance
###segs = seg(media)

# the result is a list of tuples
# each tuple contains:
# * label in 'speech', 'music', 'noise'
# * start time of the segment
# * end time of the segment

# Dummy data while working on alogorithm as proper segmentation is very slow
segs = [
('music', 0.0, 1.32),
('music', 27.0, 43.78),
('speech', 43.78, 283.32),
('music', 283.32, 309.44),
('music', 312.44, 314.52),
('speech', 312.44, 706.68),
('music', 706.6800000000001, 736.66),
('music', 905.94, 935.9200000000001),
('music', 1127.54, 1137.84),
('music', 1142.4, 1156.74),
('music', 1335.9, 1367.7),
('music', 1584.5, 1615.06),
('music', 1818.96, 1849.38),
('music', 1992.06, 2008.02),
('music', 2037.04, 2044.9),
('music', 2045.54, 2046.46),
('music', 2094.14, 2096.46)
]

print(f'Original: {segs}')

# Filter for just music segments
music_segs = []
for segment in segs:
    if segment[0] == 'music':
        music_segs += [(segment[1], segment[2]), ]

print(f'Just music: {music_segs}')

# Coalesce close segments (<10s from end of one to start of next)
new_segs = []
seg = 0
start = music_segs[seg][0]
end = music_segs[seg][1]

while seg < (len(music_segs) - 1):
    if ((music_segs[seg + 1][0]) - end) > 10:
        new_segs += [(start, end), ]
        start = music_segs[seg + 1][0]
    seg += 1
    end = music_segs[seg][1]
new_segs += [(start, end), ]

print(f'Coalesced: {new_segs}')


# adjust timestamps (add 5s to beginning and subtract 2s from end)

# segment

# remove music segments (>20s <45s ?)

# reassemble and write output file
