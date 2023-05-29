from PIL import Image, ImageDraw

def add_grid(image, grid_size, color=(255, 255, 255), thickness=1):
    draw = ImageDraw.Draw(image)
    width, height = image.size
    grid_width, grid_height = grid_size

    # Draw vertical grid lines
    for x in range(0, width, grid_width):
        draw.line([(x, 0), (x, height)], fill=color, width=thickness)

    # Draw horizontal grid lines
    for y in range(0, height, grid_height):
        draw.line([(0, y), (width, y)], fill=color, width=thickness)

    return image

# Load the image
image_path = 'peta.png'
image = Image.open(image_path)

# Define grid size (e.g., 10x10 pixels for smaller grids)
grid_size = (50, 50)

# Add grid to the image
image_with_grid = add_grid(image, grid_size)

# Display the image with the grid
image_with_grid.show()

