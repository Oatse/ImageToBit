import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import pandas as pd
import numpy as np
from pathlib import Path


class ImageColorBitConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to Color Bit Converter")
        self.root.geometry("1200x800")
        
        # Variables
        self.image = None
        self.photo = None
        self.image_path = None
        self.color_data = []
        self.canvas_image = None
        self.markers = []
        
        # Setup UI
        self.setup_ui()
        
    def setup_ui(self):
        """Setup main UI layout"""
        # Main container
        main_container = ttk.Frame(self.root, padding="10")
        main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_container.columnconfigure(0, weight=1)
        main_container.rowconfigure(1, weight=1)
        
        # Top frame for controls
        top_frame = ttk.Frame(main_container)
        top_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Upload button
        self.upload_btn = ttk.Button(top_frame, text="📁 Upload Image", command=self.upload_image)
        self.upload_btn.grid(row=0, column=0, padx=5)
        
        # Export button
        self.export_btn = ttk.Button(top_frame, text="💾 Export to CSV", command=self.export_to_csv, state=tk.DISABLED)
        self.export_btn.grid(row=0, column=1, padx=5)
        
        # Clear button
        self.clear_btn = ttk.Button(top_frame, text="🗑️ Clear Table", command=self.clear_table, state=tk.DISABLED)
        self.clear_btn.grid(row=0, column=2, padx=5)
        
        # Color info label
        self.color_info_label = ttk.Label(top_frame, text="Hover over image to see color info", relief=tk.SUNKEN, width=60)
        self.color_info_label.grid(row=0, column=3, padx=20)
        
        # Color preview box
        self.color_preview = tk.Canvas(top_frame, width=50, height=30, bg="white", relief=tk.SUNKEN, borderwidth=2)
        self.color_preview.grid(row=0, column=4, padx=5)
        
        # Middle frame - split between image and table
        middle_frame = ttk.Frame(main_container)
        middle_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        middle_frame.columnconfigure(0, weight=1)
        middle_frame.columnconfigure(1, weight=1)
        middle_frame.rowconfigure(0, weight=1)
        
        # Left side - Image canvas
        left_frame = ttk.LabelFrame(middle_frame, text="Image Preview", padding="5")
        left_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 5))
        left_frame.columnconfigure(0, weight=1)
        left_frame.rowconfigure(0, weight=1)
        
        # Canvas for image
        self.canvas = tk.Canvas(left_frame, bg="gray90", cursor="crosshair")
        self.canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbars for canvas
        canvas_scrollbar_y = ttk.Scrollbar(left_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        canvas_scrollbar_y.grid(row=0, column=1, sticky=(tk.N, tk.S))
        canvas_scrollbar_x = ttk.Scrollbar(left_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        canvas_scrollbar_x.grid(row=1, column=0, sticky=(tk.W, tk.E))
        self.canvas.configure(yscrollcommand=canvas_scrollbar_y.set, xscrollcommand=canvas_scrollbar_x.set)
        
        # Right side - Table
        right_frame = ttk.LabelFrame(middle_frame, text="Color Bit Data", padding="5")
        right_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(5, 0))
        right_frame.columnconfigure(0, weight=1)
        right_frame.rowconfigure(0, weight=1)
        
        # Table
        table_columns = ("No", "X", "Y", "Red", "Green", "Blue", "Red_Bin", "Green_Bin", "Blue_Bin", "Hex")
        self.table = ttk.Treeview(right_frame, columns=table_columns, show="headings", height=20)
        
        # Define column headings
        self.table.heading("No", text="No")
        self.table.heading("X", text="X")
        self.table.heading("Y", text="Y")
        self.table.heading("Red", text="Red (Dec)")
        self.table.heading("Green", text="Green (Dec)")
        self.table.heading("Blue", text="Blue (Dec)")
        self.table.heading("Red_Bin", text="Red (Bin)")
        self.table.heading("Green_Bin", text="Green (Bin)")
        self.table.heading("Blue_Bin", text="Blue (Bin)")
        self.table.heading("Hex", text="Hex Color")
        
        # Define column widths
        self.table.column("No", width=40)
        self.table.column("X", width=50)
        self.table.column("Y", width=50)
        self.table.column("Red", width=70)
        self.table.column("Green", width=70)
        self.table.column("Blue", width=70)
        self.table.column("Red_Bin", width=90)
        self.table.column("Green_Bin", width=90)
        self.table.column("Blue_Bin", width=90)
        self.table.column("Hex", width=80)
        
        self.table.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Table scrollbar
        table_scrollbar = ttk.Scrollbar(right_frame, orient=tk.VERTICAL, command=self.table.yview)
        table_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.table.configure(yscrollcommand=table_scrollbar.set)
        
        # Status bar
        self.status_bar = ttk.Label(main_container, text="Ready", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        
        # Bind events
        self.canvas.bind("<Motion>", self.on_mouse_move)
        self.canvas.bind("<Button-1>", self.on_mouse_click)
        
    def upload_image(self):
        """Upload and display image"""
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                # Load image
                self.image = Image.open(file_path)
                self.image_path = file_path
                
                # Display image
                self.display_image()
                
                # Auto-read all pixels from image
                self.auto_read_all_pixels()
                
                # Update status
                self.status_bar.config(text=f"Loaded: {Path(file_path).name} - Size: {self.image.size} - Total Pixels: {len(self.color_data)}")
                
                # Enable buttons
                self.export_btn.config(state=tk.NORMAL)
                self.clear_btn.config(state=tk.NORMAL)
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image:\n{str(e)}")
    
    def display_image(self):
        """Display image on canvas"""
        if self.image:
            # Convert to PhotoImage
            self.photo = ImageTk.PhotoImage(self.image)
            
            # Clear canvas
            self.canvas.delete("all")
            self.markers = []
            
            # Display image
            self.canvas_image = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            
            # Configure canvas scroll region
            self.canvas.configure(scrollregion=self.canvas.bbox(tk.ALL))
    
    def auto_read_all_pixels(self):
        """Automatically read all pixels from the image and save to table"""
        if not self.image:
            return
        
        # Clear existing data
        self.color_data = []
        
        # Show progress dialog
        self.status_bar.config(text="Reading all pixels... Please wait...")
        self.root.update()
        
        width, height = self.image.size
        total_pixels = width * height
        
        # Warning for very large images
        if total_pixels > 1000000:  # More than 1 million pixels
            result = messagebox.askyesno(
                "Large Image Warning",
                f"This image has {total_pixels:,} pixels.\n"
                f"Reading all pixels may take some time and use significant memory.\n\n"
                f"Do you want to continue?"
            )
            if not result:
                self.status_bar.config(text="Operation cancelled by user")
                return
        
        # Read all pixels
        try:
            for y in range(height):
                for x in range(width):
                    # Get pixel color
                    pixel = self.image.getpixel((x, y))
                    
                    # Handle different image modes
                    if self.image.mode == 'RGB':
                        r, g, b = pixel
                    elif self.image.mode == 'RGBA':
                        r, g, b, a = pixel
                    elif self.image.mode == 'L':  # Grayscale
                        r = g = b = pixel
                    else:
                        continue
                    
                    # Convert to binary
                    r_bin = format(r, '08b')
                    g_bin = format(g, '08b')
                    b_bin = format(b, '08b')
                    hex_color = f"#{r:02X}{g:02X}{b:02X}"
                    
                    # Add to data
                    self.color_data.append({
                        'X': x,
                        'Y': y,
                        'Red_Dec': r,
                        'Green_Dec': g,
                        'Blue_Dec': b,
                        'Red_Bin': r_bin,
                        'Green_Bin': g_bin,
                        'Blue_Bin': b_bin,
                        'Hex_Color': hex_color
                    })
                
                # Update progress every 10 rows
                if y % 10 == 0:
                    progress = (y / height) * 100
                    self.status_bar.config(text=f"Reading pixels... {progress:.1f}% ({y}/{height} rows)")
                    self.root.update()
            
            # Update table
            self.update_table()
            
            # Update status
            self.status_bar.config(text=f"Successfully read {len(self.color_data):,} pixels from image")
            messagebox.showinfo("Success", f"Successfully read {len(self.color_data):,} pixels!\n\nData is ready to export.")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read pixels:\n{str(e)}")
            self.status_bar.config(text="Error reading pixels")
    
    def on_mouse_move(self, event):
        """Handle mouse movement over canvas"""
        if self.image and self.canvas_image:
            # Get canvas coordinates
            canvas_x = self.canvas.canvasx(event.x)
            canvas_y = self.canvas.canvasy(event.y)
            
            # Convert to image coordinates
            x = int(canvas_x)
            y = int(canvas_y)
            
            # Check if coordinates are within image bounds
            if 0 <= x < self.image.width and 0 <= y < self.image.height:
                # Get pixel color
                pixel = self.image.getpixel((x, y))
                
                # Handle different image modes
                if self.image.mode == 'RGB':
                    r, g, b = pixel
                elif self.image.mode == 'RGBA':
                    r, g, b, a = pixel
                elif self.image.mode == 'L':  # Grayscale
                    r = g = b = pixel
                else:
                    return
                
                # Convert to binary
                r_bin = format(r, '08b')
                g_bin = format(g, '08b')
                b_bin = format(b, '08b')
                hex_color = f"#{r:02X}{g:02X}{b:02X}"
                
                # Update color info label
                info_text = f"X:{x} Y:{y} | RGB:({r},{g},{b}) | Bin: R:{r_bin} G:{g_bin} B:{b_bin} | {hex_color}"
                self.color_info_label.config(text=info_text)
                
                # Update color preview
                self.color_preview.config(bg=hex_color)
    
    def on_mouse_click(self, event):
        """Handle mouse click to save color data"""
        if self.image and self.canvas_image:
            # Get canvas coordinates
            canvas_x = self.canvas.canvasx(event.x)
            canvas_y = self.canvas.canvasy(event.y)
            
            # Convert to image coordinates
            x = int(canvas_x)
            y = int(canvas_y)
            
            # Check if coordinates are within image bounds
            if 0 <= x < self.image.width and 0 <= y < self.image.height:
                # Get pixel color
                pixel = self.image.getpixel((x, y))
                
                # Handle different image modes
                if self.image.mode == 'RGB':
                    r, g, b = pixel
                elif self.image.mode == 'RGBA':
                    r, g, b, a = pixel
                elif self.image.mode == 'L':  # Grayscale
                    r = g = b = pixel
                else:
                    return
                
                # Convert to binary
                r_bin = format(r, '08b')
                g_bin = format(g, '08b')
                b_bin = format(b, '08b')
                hex_color = f"#{r:02X}{g:02X}{b:02X}"
                
                # Add to data
                self.color_data.append({
                    'X': x,
                    'Y': y,
                    'Red_Dec': r,
                    'Green_Dec': g,
                    'Blue_Dec': b,
                    'Red_Bin': r_bin,
                    'Green_Bin': g_bin,
                    'Blue_Bin': b_bin,
                    'Hex_Color': hex_color
                })
                
                # Update table
                self.update_table()
                
                # Draw marker on canvas
                marker = self.canvas.create_oval(
                    canvas_x - 3, canvas_y - 3,
                    canvas_x + 3, canvas_y + 3,
                    fill=hex_color, outline="black", width=2
                )
                self.markers.append(marker)
                
                # Update status
                self.status_bar.config(text=f"Saved color at ({x}, {y}) - Total: {len(self.color_data)} points")
    
    def update_table(self):
        """Update table with color data"""
        # Clear table
        for item in self.table.get_children():
            self.table.delete(item)
        
        # Add data to table
        for idx, data in enumerate(self.color_data, 1):
            self.table.insert("", tk.END, values=(
                idx,
                data['X'],
                data['Y'],
                data['Red_Dec'],
                data['Green_Dec'],
                data['Blue_Dec'],
                data['Red_Bin'],
                data['Green_Bin'],
                data['Blue_Bin'],
                data['Hex_Color']
            ))
    
    def export_to_csv(self):
        """Export table data to CSV"""
        if not self.color_data:
            messagebox.showwarning("Warning", "No data to export!")
            return
        
        # Ask for save location
        file_path = filedialog.asksaveasfilename(
            title="Save CSV File",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                # Create DataFrame
                df = pd.DataFrame(self.color_data)
                
                # Reorder columns
                df = df[['X', 'Y', 'Red_Dec', 'Green_Dec', 'Blue_Dec', 
                        'Red_Bin', 'Green_Bin', 'Blue_Bin', 'Hex_Color']]
                
                # Export to CSV
                df.to_csv(file_path, index=False)
                
                messagebox.showinfo("Success", f"Data exported successfully to:\n{file_path}")
                self.status_bar.config(text=f"Exported {len(self.color_data)} rows to CSV")
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export CSV:\n{str(e)}")
    
    def clear_table(self):
        """Clear all data from table"""
        if self.color_data:
            result = messagebox.askyesno("Confirm", "Are you sure you want to clear all data?")
            if result:
                # Clear data
                self.color_data = []
                
                # Clear table
                for item in self.table.get_children():
                    self.table.delete(item)
                
                # Clear markers
                for marker in self.markers:
                    self.canvas.delete(marker)
                self.markers = []
                
                # Update status
                self.status_bar.config(text="Table cleared")
                messagebox.showinfo("Success", "Table cleared successfully")


def main():
    root = tk.Tk()
    app = ImageColorBitConverter(root)
    root.mainloop()


if __name__ == "__main__":
    main()
