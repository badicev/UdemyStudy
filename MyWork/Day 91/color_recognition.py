class ImageColorRecognizer:
    def __init__(self, image_path):
        self.image_path = image_path
        
    def get_colors(self, image, number_of_colors, show_chart):
        modified_image = image.resize((600, 400), Image.ANTIALIAS)
        modified_image = modified_image.convert('RGB')
        modified_image = modified_image.convert('P', palette=Image.ADAPTIVE, colors=number_of_colors)
        modified_image = modified_image.convert('RGB')
        
        color_list = modified_image.getcolors(600 * 400)
        
        # Sort colors by count number
        color_list.sort(reverse=True)
        
        # Return colors
        return color_list
    
    def get_image(self):
        image = Image.open(self.image_path)
        return image
    
    def get_colors_from_image(self, number_of_colors=10, show_chart=False):
        # Get colors from image
        image = self.get_image()
        color_list = self.get_colors(image, number_of_colors, show_chart)
        
        # Return colors
        return color_list
    
    def get_color_name(self, rgb_color):
        # Convert RGB to HEX
        hex_color = '#%02x%02x%02x' % rgb_color
        hex_color = hex_color.upper()
        
        # Get color name
        try:
            color_name = webcolors.hex_to_name(hex_color)
        except ValueError:
            color_name = hex_color
            
        # Return color name
        return color_name
    
    def get_colors_from_image_as_dict(self, number_of_colors=10, show_chart=False):
        # Get colors from image
        color_list = self.get_colors_from_image(number_of_colors, show_chart)
        
        # Create color dict
        color_dict = {}
        
        # Add colors to dict
        for color in color_list:
            color_dict[self.get_color_name(color[1])] = color[0]
            
        # Return color dict
        return color_dict

        #Create a chart
    def create_chart(color_dict):
        # Create color list
        color_list = []
            
        # Add colors to list
        for key, value in color_dict.items():
             color_list.append((key, value))
                
        # Create chart
        chart = pygal.Pie()
        chart.title = 'Color Recognition'
        chart.add('', color_list)
            
        # Return chart
        return chart

# Path: Day 91\color_recognition_app.py 
