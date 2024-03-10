import kivy
from kivy.logger import Logger
from kivy.utils import platform
from collections import OrderedDict
try:
    import numpy
    import cv2
    opencv = True
except:
    opencv = False

if platform in ['win', 'linux', 'macosx', 'unknown']:
    desktop = True
else:
    desktop = False

import os
app_directory = os.path.dirname(os.path.realpath(__file__))
ffmpeg_command = os.path.join(app_directory, 'ffmpeg')
if not os.path.isfile(ffmpeg_command):
    ffmpeg_command = ffmpeg_command + '.exe'
if not os.path.isfile(ffmpeg_command):
    import distutils.spawn
    ffmpeg_command = distutils.spawn.find_executable("ffmpeg")
if ffmpeg_command is None:
    Logger.warning('FFMPEG not found, please install it for video conversion features.')
    ffmpeg = False
else:
    Logger.info('Using FFMPEG from '+str(ffmpeg_command))
    ffmpeg = True

kivy_version = kivy.__version__.split('.')
kivy_version_primary = int(kivy_version[0])
kivy_version_secondary = int(kivy_version[1])

scale_size_to_options = OrderedDict([('long', 'Long Side'), ('short', 'Short Side'), ('height', 'Height'), ('width', 'Width')])
naming_method_default = '%Y-%M-%D< - %T>'
avoidfolders = ['.picasaoriginals', '.thumbnails', '.originals']
negative_kelvin = [(255, 115, 0), (255, 124, 0), (255, 121, 0), (255, 130, 0), (255, 126, 0), (255, 135, 0), (255, 131, 0), (255, 141, 11), (255, 137, 18), (255, 146, 29), (255, 142, 33), (255, 152, 41), (255, 147, 44), (255, 157, 51), (255, 152, 54), (255, 162, 60), (255, 157, 63), (255, 166, 69), (255, 161, 72), (255, 170, 77), (255, 165, 79), (255, 174, 84), (255, 169, 87), (255, 178, 91), (255, 173, 94), (255, 182, 98), (255, 177, 101), (255, 185, 105), (255, 180, 107), (255, 189, 111), (255, 184, 114), (255, 192, 118), (255, 187, 120), (255, 195, 124), (255, 190, 126), (255, 198, 130), (255, 193, 132), (255, 201, 135), (255, 196, 137), (255, 203, 141), (255, 199, 143), (255, 206, 146), (255, 201, 148), (255, 208, 151), (255, 204, 153), (255, 211, 156), (255, 206, 159), (255, 213, 161), (255, 209, 163), (255, 215, 166), (255, 211, 168), (255, 217, 171), (255, 213, 173), (255, 219, 175), (255, 215, 177), (255, 221, 180), (255, 217, 182), (255, 223, 184), (255, 219, 186), (255, 225, 188), (255, 221, 190), (255, 226, 192), (255, 223, 194), (255, 228, 196), (255, 225, 198), (255, 229, 200), (255, 227, 202), (255, 231, 204), (255, 228, 206), (255, 232, 208), (255, 230, 210), (255, 234, 211), (255, 232, 213), (255, 235, 215), (255, 233, 217), (255, 237, 218), (255, 235, 220), (255, 238, 222), (255, 236, 224), (255, 239, 225), (255, 238, 227), (255, 240, 228), (255, 239, 230), (255, 241, 231), (255, 240, 233), (255, 243, 234), (255, 242, 236), (255, 244, 237), (255, 243, 239), (255, 245, 240), (255, 244, 242), (255, 246, 243), (255, 245, 245), (255, 247, 245), (255, 246, 248), (255, 248, 248), (255, 248, 251), (255, 249, 251), (255, 249, 253), (255, 249, 253)]
positive_kelvin = [(254, 249, 255), (254, 250, 255), (252, 247, 255), (252, 248, 255), (249, 246, 255), (250, 247, 255), (247, 245, 255), (247, 245, 255), (245, 243, 255), (245, 244, 255), (243, 242, 255), (243, 243, 255), (240, 241, 255), (241, 241, 255), (239, 240, 255), (239, 240, 255), (237, 239, 255), (238, 239, 255), (235, 238, 255), (236, 238, 255), (233, 237, 255), (234, 237, 255), (231, 236, 255), (233, 236, 255), (230, 235, 255), (231, 234, 255), (228, 234, 255), (229, 233, 255), (227, 233, 255), (228, 233, 255), (225, 232, 255), (227, 232, 255), (224, 231, 255), (225, 231, 255), (222, 230, 255), (224, 230, 255), (221, 230, 255), (223, 229, 255), (220, 229, 255), (221, 228, 255), (218, 228, 255), (220, 227, 255), (217, 227, 255), (219, 226, 255), (216, 227, 255), (218, 226, 255), (215, 226, 255), (217, 225, 255), (214, 225, 255), (216, 224, 255), (212, 225, 255), (215, 223, 255), (211, 224, 255), (214, 223, 255), (210, 223, 255), (213, 222, 255), (209, 223, 255), (212, 221, 255), (208, 222, 255), (211, 221, 255), (207, 221, 255), (210, 220, 255), (207, 221, 255), (209, 220, 255), (206, 220, 255), (208, 219, 255), (205, 220, 255), (207, 218, 255), (204, 219, 255), (207, 218, 255), (203, 219, 255), (206, 217, 255), (202, 218, 255), (205, 217, 255), (201, 218, 255), (204, 216, 255), (201, 217, 255), (204, 216, 255), (200, 217, 255), (203, 215, 255), (199, 216, 255), (202, 215, 255), (199, 216, 255), (202, 214, 255), (198, 216, 255), (201, 214, 255), (197, 215, 255), (200, 213, 255), (196, 215, 255), (200, 213, 255), (196, 214, 255), (199, 212, 255), (195, 214, 255), (198, 212, 255), (195, 214, 255), (198, 212, 255), (194, 213, 255), (197, 211, 255), (193, 213, 255), (197, 211, 255)]

audio_encode_values = [320, 256, 192, 160, 128, 96, 80, 64]

encoding_quality_friendly = ['Very High', 'High', 'Medium', 'Low', 'Very Low']
encoding_quality = [1.3, 1, 0.8, 0.7, 0.5]
encoding_speeds_friendly = ['Very Fast', 'Fast', 'Medium', 'Slow', 'Very Slow']
encoding_speeds = ['veryfast', 'fast', 'medium', 'slow', 'veryslow']
encoding_colors_friendly = ['Copy', 'YUV 420', 'YUV 422', 'YUV 444', 'RGB 24']
encoding_colors = ['copy', 'yuv420p', 'yuv422p', 'yuv444p', 'rgb24']
framerate_presets = ['Auto', '30', '29.97', '24', '25', '60']
resolution_presets = ['1920x1080', '1280x720', '3840x2160', '720x480']

interface_multiplier = 22
drag_delay = .5

themes = [
    {
        "name": "Default",
        "button_down": [0.48, 0.59, 0.62, 1.0],
        "button_up": [0.3, 0.44, 0.48, 1.0],
        "button_text": [1.0, 1.0, 1.0, 0.9],
        "button_warn_down": [0.78, 0.33, 0.33, 1.0],
        "button_warn_up": [0.8, 0.08, 0.08, 1.0],
        "button_toggle_true": [0.31, 0.68, 0.46, 1.0],
        "button_toggle_false": [0.38, 0.38, 0.38, 1.0],
        "button_menu_up": [0.14, 0.42, 0.35, 1.0],
        "button_menu_down": [0.15, 0.84, 0.67, 1.0],
        "button_disabled": [0.28, 0.28, 0.28, 1.0],
        "button_disabled_text": [1.0, 1.0, 1.0, 0.5],
        "header_background": [0.502, 0.467, 0.572, 1.0],
        "header_main_background": [0.739, 0.739, 0.8, 1.0],
        "header_text": [1.0, 1.0, 1.0, 1.0],
        "info_text": [0.0, 0.0, 0.0, 1.0],
        "info_background": [1.0, 1.0, 0.0, 0.75],
        "input_background": [0.18, 0.18, 0.27, 1.0],
        "scroller": [0.7, 0.7, 0.7, 0.4],
        "scroller_selected": [0.7, 0.7, 0.7, 0.9],
        "sidebar_background": [0.555, 0.625, 0.678, 1.0],
        "sidebar_resizer": [0.406, 0.607, 0.406, 1.0],
        "slider_grabber": [0.5098, 0.8745, 0.6588, 1.0],
        "slider_background": [0.546, 0.59, 0.616, 1.0],
        "main_background": [0.5, 0.5, 0.634, 0.292],
        "menu_background": [0.26, 0.29, 0.31, 1.0],
        "area_background": [0.26, 0.29, 0.31, 0.33],
        "background": [0.0, 0.0, 0.0, 1.0],
        "text": [1.0, 1.0, 1.0, 0.9],
        "disabled_text": [1.0, 1.0, 1.0, 0.5],
        "selected": [0.5098, 0.8745, 0.6588, 0.5],
        "missing": [1.0, 0.0, 0.0, 0.33],
        "favorite": [0.8, 0.8, 0.0, 0.6]
    },
    {
        "name": "Clean And Bright",
        "button_down": [0.651, 0.651, 0.678, 1.0],
        "button_up": [0.8, 0.8, 0.8, 1.0],
        "button_text": [0.0, 0.0, 0.0, 1.0],
        "button_warn_down": [0.78, 0.33, 0.33, 1.0],
        "button_warn_up": [1.0, 0.493, 0.502, 1.0],
        "button_toggle_true": [0.31, 0.68, 0.46, 1.0],
        "button_toggle_false": [0.678, 0.651, 0.678, 1.0],
        "button_menu_up": [0.686, 0.686, 0.686, 1.0],
        "button_menu_down": [0.511, 0.52, 0.52, 1.0],
        "button_disabled": [0.686, 0.695, 0.721, 0.669],
        "button_disabled_text": [1.0, 1.0, 1.0, 0.748],
        "header_background": [0.941, 0.95, 0.941, 0.16],
        "header_main_background": [1.0, 1.0, 1.0, 0.397],
        "header_text": [0.107, 0.099, 0.099, 1.0],
        "info_text": [0.0, 0.0, 0.0, 1.0],
        "info_background": [1.0, 1.0, 0.0, 0.75],
        "input_background": [1.0, 1.0, 1.0, 0.651],
        "scroller": [0.7, 0.7, 0.7, 0.388],
        "scroller_selected": [0.7, 0.7, 0.7, 0.9],
        "sidebar_background": [1.0, 1.0, 1.0, 0.792],
        "sidebar_resizer": [0.862, 1.0, 0.897, 1.0],
        "slider_grabber": [0.45, 0.45, 0.458, 1.0],
        "slider_background": [1.0, 1.0, 1.0, 1.0],
        "main_background": [0.616, 0.616, 0.616, 0.283],
        "menu_background": [0.529, 0.537, 0.537, 1.0],
        "area_background": [0.0, 0.0, 0.0, 0.046],
        "background": [1.0, 1.0, 1.0, 1.0],
        "text": [0.0, 0.011, 0.0, 1.0],
        "disabled_text": [0.0, 0.0, 0.0, 0.572],
        "selected": [0.239, 1.0, 0.344, 0.634],
        "missing": [1.0, 0.0, 0.0, 0.45],
        "favorite": [0.8, 0.8, 0.002, 0.6]
    },
    {
        "name": "Bright And Warm",
        "button_down": [0.763, 0.624, 0.494, 1.0],
        "button_up": [0.808, 0.714, 0.632, 1.0],
        "button_text": [0.0, 0.0, 0.0, 1.0],
        "button_warn_down": [0.821, 0.333, 0.329, 1.0],
        "button_warn_up": [1.0, 0.384, 0.408, 1.0],
        "button_toggle_true": [0.444, 0.776, 0.494, 1.0],
        "button_toggle_false": [0.467, 0.494, 0.427, 0.842],
        "button_menu_up": [0.733, 0.62, 0.538, 1.0],
        "button_menu_down": [0.553, 0.525, 0.459, 1.0],
        "button_disabled": [0.776, 0.69, 0.612, 0.444],
        "button_disabled_text": [0.0, 0.0, 0.0, 0.466],
        "header_background": [0.941, 0.871, 0.792, 0.719],
        "header_main_background": [0.98, 0.945, 0.763, 0.459],
        "header_text": [0.107, 0.099, 0.099, 1.0],
        "info_text": [0.0, 0.0, 0.0, 1.0],
        "info_background": [1.0, 0.965, 0.4, 1.0],
        "input_background": [0.915, 0.827, 0.765, 0.945],
        "scroller": [0.58, 0.62, 0.502, 0.733],
        "scroller_selected": [0.698, 0.792, 0.698, 0.902],
        "sidebar_background": [0.957, 0.91, 0.85, 0.835],
        "sidebar_resizer": [0.922, 0.987, 0.784, 1.0],
        "slider_grabber": [0.422, 0.827, 0.62, 1.0],
        "slider_background": [0.894, 0.859, 0.792, 1.0],
        "main_background": [1.0, 0.827, 0.618, 0.341],
        "menu_background": [0.835, 0.734, 0.62, 1.0],
        "area_background": [0.0, 0.0, 0.0, 0.089],
        "background": [1.0, 1.0, 1.0, 1.0],
        "text": [0.0, 0.011, 0.0, 1.0],
        "disabled_text": [0.0, 0.0, 0.0, 0.531],
        "selected": [0.705, 1.0, 0.537, 0.631],
        "missing": [1.0, 0.0, 0.0, 0.45],
        "favorite": [1.0, 0.957, 0.234, 0.6]
    },
    {
        "name": "Dark Blue",
        "button_down": [0.248, 0.336, 0.397, 1.0],
        "button_up": [0.204, 0.248, 0.309, 1.0],
        "button_text": [1.0, 1.0, 1.0, 0.774],
        "button_warn_down": [0.555, 0.204, 0.221, 1.0],
        "button_warn_up": [0.52, 0.08, 0.08, 1.0],
        "button_toggle_true": [0.195, 0.388, 0.221, 1.0],
        "button_toggle_false": [0.195, 0.239, 0.204, 1.0],
        "button_menu_up": [0.169, 0.204, 0.274, 1.0],
        "button_menu_down": [0.204, 0.283, 0.406, 1.0],
        "button_disabled": [0.134, 0.134, 0.143, 1.0],
        "button_disabled_text": [1.0, 1.0, 1.0, 0.248],
        "header_background": [0.353, 0.371, 0.493, 1.0],
        "header_main_background": [0.143, 0.151, 0.186, 1.0],
        "header_text": [1.0, 1.0, 1.0, 0.599],
        "info_text": [1.0, 1.0, 1.0, 1.0],
        "info_background": [0.318, 0.704, 0.572, 0.432],
        "input_background": [0.143, 0.107, 0.178, 1.0],
        "scroller": [0.7, 0.7, 0.7, 0.186],
        "scroller_selected": [0.7, 0.7, 0.7, 0.704],
        "sidebar_background": [0.029, 0.239, 0.3, 1.0],
        "sidebar_resizer": [0.195, 0.388, 0.292, 1.0],
        "slider_grabber": [0.23, 0.406, 0.274, 1.0],
        "slider_background": [0.204, 0.432, 0.485, 1.0],
        "main_background": [0.143, 0.195, 0.257, 0.309],
        "menu_background": [0.213, 0.23, 0.309, 1.0],
        "area_background": [0.26, 0.29, 0.31, 0.33],
        "background": [0.0, 0.0, 0.0, 1.0],
        "text": [1.0, 1.0, 1.0, 0.695],
        "disabled_text": [1.0, 1.0, 1.0, 0.5],
        "selected": [0.51, 0.875, 0.659, 0.327],
        "missing": [1.0, 0.0, 0.0, 0.33],
        "favorite": [0.8, 0.8, 0.0, 0.371]
    }
]
