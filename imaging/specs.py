from imagekit.specs import ImageSpec 
from imagekit import processors 

class ResizeImagingThumb(processors.Resize): 
  width = 200 
  height = 200 
  crop = True

class ResizeSmallThumb(processors.Resize): 
  width = 200 
  height = 200 
  crop = True

class ResizeDisplay(processors.Resize):
  width = 600 

class ImagingThumbnail(ImageSpec): 
  access_as = 'imaging_thumbnail' 
  pre_cache = True 
  processors = [ResizeImagingThumb] 

class Display(ImageSpec):
  processors = [ResizeDisplay]

class SmallThumbnail(ImageSpec): 
  access_as = 'small_thumbnail' 
  pre_cache = True 
  processors = [ResizeSmallThumb] 
