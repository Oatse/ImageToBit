# Technical Documentation - Image to Color Bit Converter

## Architecture Overview

### System Architecture
```
┌─────────────────────────────────────────────────┐
│              ImageColorBitConverter             │
│                 (Main Class)                    │
├─────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐            │
│  │  GUI Layer   │  │  Data Layer  │            │
│  │  (tkinter)   │  │  (pandas)    │            │
│  └──────────────┘  └──────────────┘            │
│         │                  │                    │
│  ┌──────────────┐  ┌──────────────┐            │
│  │ Image Layer  │  │  File I/O    │            │
│  │  (Pillow)    │  │  (CSV)       │            │
│  └──────────────┘  └──────────────┘            │
└─────────────────────────────────────────────────┘
```

## Components

### 1. GUI Components (tkinter)
- **Main Window**: Root window dengan grid layout
- **Top Frame**: Control buttons dan info labels
- **Middle Frame**: Split view (image canvas + data table)
- **Status Bar**: Bottom status information

### 2. Image Processing (Pillow)
```python
# Image loading
self.image = Image.open(file_path)

# Pixel access
pixel = self.image.getpixel((x, y))

# Color extraction
r, g, b = pixel  # for RGB mode
```

### 3. Data Management (pandas)
```python
# Data structure
{
    'X': x_coordinate,
    'Y': y_coordinate,
    'Red_Dec': red_value,
    'Green_Dec': green_value,
    'Blue_Dec': blue_value,
    'Red_Bin': binary_string,
    'Green_Bin': binary_string,
    'Blue_Bin': binary_string,
    'Hex_Color': hex_string
}

# Export
df = pd.DataFrame(self.color_data)
df.to_csv(file_path, index=False)
```

## Key Functions

### upload_image()
```python
def upload_image(self):
    """
    1. Open file dialog
    2. Load image with Pillow
    3. Display on canvas
    4. Enable buttons
    """
```

### on_mouse_move(event)
```python
def on_mouse_move(self, event):
    """
    Real-time color detection:
    1. Get canvas coordinates
    2. Convert to image coordinates
    3. Extract pixel color
    4. Convert to binary
    5. Update UI labels
    """
```

### on_mouse_click(event)
```python
def on_mouse_click(self, event):
    """
    Save color data:
    1. Get pixel color
    2. Convert to all formats
    3. Add to data list
    4. Update table
    5. Draw marker
    """
```

### export_to_csv()
```python
def export_to_csv(self):
    """
    Export process:
    1. Check data availability
    2. Create DataFrame
    3. Reorder columns
    4. Save to CSV
    5. Show notification
    """
```

## Data Flow

```
User Action
    │
    ├─→ Upload Image
    │       └─→ Pillow.Image.open()
    │              └─→ display_image()
    │                     └─→ Canvas.create_image()
    │
    ├─→ Hover Mouse
    │       └─→ on_mouse_move()
    │              └─→ getpixel()
    │                     └─→ RGB extraction
    │                            └─→ Binary conversion
    │                                   └─→ Update UI
    │
    ├─→ Click Pixel
    │       └─→ on_mouse_click()
    │              └─→ getpixel()
    │                     └─→ Save to list
    │                            └─→ Update table
    │                                   └─→ Draw marker
    │
    └─→ Export CSV
            └─→ export_to_csv()
                   └─→ DataFrame creation
                          └─→ to_csv()
                                 └─→ File save
```

## Color Conversion

### RGB to Binary (8-bit)
```python
# Decimal to Binary
r = 255  # Red channel
r_bin = format(r, '08b')  # '11111111'

# Example conversions:
# 0   -> '00000000'
# 128 -> '10000000'
# 255 -> '11111111'
```

### RGB to Hexadecimal
```python
# RGB to Hex
r, g, b = 255, 128, 64
hex_color = f"#{r:02X}{g:02X}{b:02X}"  # '#FF8040'
```

## Performance Considerations

### Memory Management
- Images are kept in memory as PIL Image objects
- Canvas uses PhotoImage for display
- Markers are stored as canvas objects

### Optimization
```python
# Efficient pixel access
pixel = self.image.getpixel((x, y))  # O(1) operation

# List append for data
self.color_data.append(data)  # O(1) amortized

# DataFrame creation only on export
df = pd.DataFrame(self.color_data)  # Created once
```

## Event Handling

### Mouse Events
```python
# Bind events
self.canvas.bind("<Motion>", self.on_mouse_move)
self.canvas.bind("<Button-1>", self.on_mouse_click)

# Canvas coordinates to image coordinates
canvas_x = self.canvas.canvasx(event.x)
canvas_y = self.canvas.canvasy(event.y)
```

### Button Events
```python
# Command binding
ttk.Button(text="Upload", command=self.upload_image)
ttk.Button(text="Export", command=self.export_to_csv)
ttk.Button(text="Clear", command=self.clear_table)
```

## Error Handling

### Image Loading
```python
try:
    self.image = Image.open(file_path)
except Exception as e:
    messagebox.showerror("Error", f"Failed to load: {str(e)}")
```

### Pixel Access
```python
# Bounds checking
if 0 <= x < self.image.width and 0 <= y < self.image.height:
    pixel = self.image.getpixel((x, y))
```

### Image Mode Handling
```python
if self.image.mode == 'RGB':
    r, g, b = pixel
elif self.image.mode == 'RGBA':
    r, g, b, a = pixel
elif self.image.mode == 'L':  # Grayscale
    r = g = b = pixel
```

## UI Layout Grid System

```python
# Root grid
main_container.grid(row=0, column=0, sticky=(W, E, N, S))

# Configure weights for responsive
self.root.columnconfigure(0, weight=1)
self.root.rowconfigure(0, weight=1)

# Layout structure
row 0: Top control frame
row 1: Middle split frame (image | table)
row 2: Status bar
```

## CSV Format Specification

### Headers
```
X, Y, Red_Dec, Green_Dec, Blue_Dec, Red_Bin, Green_Bin, Blue_Bin, Hex_Color
```

### Data Types
- X, Y: Integer (pixel coordinates)
- Red/Green/Blue_Dec: Integer (0-255)
- Red/Green/Blue_Bin: String (8-bit binary)
- Hex_Color: String (hex format #RRGGBB)

### Example Row
```
50,100,255,128,64,11111111,10000000,01000000,#FF8040
```

## Testing Strategy

### Unit Testing Areas
1. Color conversion (RGB to Binary)
2. Image loading (various formats)
3. Pixel access (boundary cases)
4. CSV export (data integrity)

### Integration Testing
1. Upload → Display workflow
2. Hover → Color detection workflow
3. Click → Save → Table update workflow
4. Export → CSV generation workflow

### Edge Cases
- Very large images
- Different image modes (RGB, RGBA, L)
- Empty table export
- Invalid file formats

## Future Enhancements

### Potential Features
1. **Zoom functionality** - Zoom in/out untuk detail
2. **Color history** - Track recent colors
3. **Color picker** - Select color from palette
4. **Batch processing** - Process multiple images
5. **Image filters** - Apply filters before analysis
6. **Statistics** - Color distribution analysis
7. **Export formats** - JSON, Excel, etc.
8. **Undo/Redo** - Action history
9. **Color comparison** - Side-by-side compare
10. **Annotations** - Add notes to saved colors

### Performance Improvements
1. Lazy loading for large images
2. Cache pixel data
3. Async export for large datasets
4. Image compression options

## Code Standards

### Naming Conventions
- Classes: PascalCase
- Functions: snake_case
- Constants: UPPER_CASE
- Private: _leading_underscore

### Documentation
- Docstrings for all public methods
- Inline comments for complex logic
- Type hints where applicable

## Dependencies Version

```
Python >= 3.8
tkinter: Built-in
Pillow >= 10.0.0
pandas >= 2.0.0
numpy >= 1.24.0
```

## License
This project is created for educational purposes.

---
**Last Updated**: October 2025
