from os import remove
from os.path import basename, dirname
from django.core.files import File

def rescale(data, width, height, force=False):
	"""Rescale the given image, optionally cropping it to make sure the result image has the specified width and height."""
	import Image as pil
	from cStringIO import StringIO
	
	max_width = width
	max_height = height

	input_file = StringIO(data)
	img = pil.open(input_file)
	if not force:
		img.thumbnail((max_width, max_height), pil.ANTIALIAS)
	else:
		src_width, src_height = img.size
		src_ratio = float(src_width) / float(src_height)
		dst_width, dst_height = max_width, max_height
		dst_ratio = float(dst_width) / float(dst_height)
		
		if dst_ratio < src_ratio:
			crop_height = src_height
			crop_width = crop_height * dst_ratio
			x_offset = float(src_width - crop_width) / 2
			y_offset = 0
		else:
			crop_width = src_width
			crop_height = crop_width / dst_ratio
			x_offset = 0
			y_offset = float(src_height - crop_height) / 3
		img = img.crop((x_offset, y_offset, x_offset+int(crop_width), y_offset+int(crop_height)))
		img = img.resize((dst_width, dst_height), pil.ANTIALIAS)
		
	tmp = StringIO()
	img.save(tmp, 'JPEG')
	tmp.seek(0)
	output_data = tmp.getvalue()
	input_file.close()
	tmp.close()
	
	return output_data

#TODO: obsluga wyjatkow
def create_thumb(imgfield, size_x, size_y, suffix="_thumb_", force_aspect=False):
    imgfield.file.open()
    thumb_data = rescale(imgfield.file.read(), size_x, size_y, force_aspect)
    image_filename = basename(imgfield.file.name)
    thumb_name = image_filename[:image_filename.rfind(".")]+suffix+".jpg"
    file = open(dirname(imgfield.path)+'/'+thumb_name, "w")
    thumbnail = File(file)
    thumbnail.write(thumb_data)
    thumbnail.close()
    imgfield.file.close()

def extract_filename(path):
    filename = basename(path)
    return filename[:filename.rfind(".")]

def remove_thumb(imgfield, preset):
    imgfield.file.open()
    suffix = preset['suffix']
    image_filename = basename(imgfield.file.name)
    thumb_name = image_filename[:image_filename.rfind(".")]+suffix+".jpg"
    remove(dirname(imgfield.path)+'/'+thumb_name)
    imgfield.file.close()
