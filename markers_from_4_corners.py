# "Markers from 4 Corners"
# Author: Michael G Chu - https://github.com/michaelgchu
# Last updated: November 24 2023
# Based off original code posted by user "emu" on this thread:
# https://blender.stackexchange.com/questions/51810/is-it-possible-to-use-four-corners-of-a-single-marker-for-a-plane-track
#
# Purpose:
# This Blender Python code will generate 4 Tracking Markers from the corners
# of a single Marker.
# These 4 new markers can then be used to create a Plane Track that will rotate
# and deform like the original marker.
# IMPORTANT NOTE: this code will process a frame range - either the entire 
# frame range of the scene, or a subsection if you set some of the variables
# below. There cannot be any untracked frames within this range, otherwise the
# code will fail!
# 
# Instructions:
# 1. Import your source video into the Motion Tracking workspace
#    (Movie Clip Editor)
# 2. (Optional) Rename this clip (right now it has the same name as the file)
# 3. Create a Tracking Marker in Blender's Movie Clip Editor, using the Motion
#    Model tracking model that makes sense
# 4. (Optional) Name this track (the first track per clip is named "Track")
# 5. Add a Text Editor into your workspace
# 6. If you downloaded this .py file then use the Open button to open it now.
#    Otherwise, click the New button and paste in the contents of this script
# 7. Change the 2-4 variables below as follows:
# 7a. For yourMovieClip, set it to the name of your clip. It will be the name
#     of the source video file or the name you gave in step 2 above
# 7b. For yourMarker, set it to the name of your Tracking Marker. It might be
#     "Track" or the name you gave in step 4 above
# 7c. If you did not start tracking from the very first frame of the scene,
#     then set first to the first frame that you did track
# 7d. If you did not track all the way to the last frame of the scene, then set
#     last to the last frame that you did track
# 8. Click the play button to run the code. (You may need to expand the width
#    of this region or pan across the Text Editor's menu bar to see the button.)
# After following these steps, you should have 4 new tracking markers, which
# you can now use to create a Plane Track :)
# 

##############################################################################
## BEFORE RUNNING: Update the first 2 variables below, and the last 2 if you
## did not track the entire scene.
##############################################################################

# yourMovieClip : This is what you named the movie clip *within* Blender
yourMovieClip = 'your_movie_clip.mp4'
# yourMarker    : This is the name of the marker you created
yourMarker    = 'Track'
# first : Set this to the first tracked frame IF you did not track throughout the entire scene
first = 0
# final : Set this to the final tracked frame IF you did not track throughout the entire scene
final = 0

##############################################################################
## No changes required below this point
##############################################################################

import bpy
D = bpy.data
C = bpy.context

tracking = D.movieclips[yourMovieClip].tracking
begin = first if first else C.scene.frame_start
end   = final if final else C.scene.frame_end

corners = [tracking.tracks.new(frame=begin) for i in range(4)]
track = tracking.tracks[yourMarker]
for frame in range(begin, end+1):
     track_marker = track.markers.find_frame(frame)
     for i, corner in enumerate(corners):
        corner.markers.insert_frame(frame)
        corner_marker = corner.markers.find_frame(frame)
        corner_marker.co = track_marker.pattern_corners[i]
        corner_marker.co += track_marker.co
#EOF
