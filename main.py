import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import pandas as pd
import numpy as np


class ImageToRGBMatrix:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to RGB Matrix Converter")
        self.root.geometry("1400x800")
        
        # Variables
        self.image = None
        self.photo = None
        self.image_array = None
        self.original_image = None
        self.zoom_scale = 1.0
        
        # Create main container
        main_container = tk.PanedWindow(root, orient=tk.HORIZONTAL)
        main_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Left panel - Image display
        left_frame = tk.Frame(main_container, bg='white')
        main_container.add(left_frame, width=700)
        
        # Right panel - Controls and data
        right_frame = tk.Frame(main_container, bg='lightgray')
        main_container.add(right_frame, width=700)
        
        self.setup_left_panel(left_frame)
        self.setup_right_panel(right_frame)
    
    def setup_left_panel(self, parent):
        # Title
        title_label = tk.Label(parent, text="Image Display", font=("Arial", 14, "bold"), bg='white')
        title_label.pack(pady=10)
        
        # Upload button
        upload_btn = tk.Button(parent, text="📁 Upload Image", command=self.upload_image, 
                               font=("Arial", 12), bg='#4CAF50', fg='white', 
                               padx=20, pady=10, cursor='hand2')
        upload_btn.pack(pady=5)
        
        # Image info label
        self.info_label = tk.Label(parent, text="No image loaded", 
                                   font=("Arial", 10), bg='white', fg='gray')
        self.info_label.pack(pady=5)
        
        # Canvas frame with scrollbars
        canvas_frame = tk.Frame(parent, bg='white')
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Scrollbars
        h_scrollbar = tk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        v_scrollbar = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL)
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Canvas
        self.canvas = tk.Canvas(canvas_frame, bg='white', 
                                xscrollcommand=h_scrollbar.set,
                                yscrollcommand=v_scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        h_scrollbar.config(command=self.canvas.xview)
        v_scrollbar.config(command=self.canvas.yview)
        
        # Bind mouse events
        self.canvas.bind("<Motion>", self.on_mouse_move)
        self.canvas.bind("<Leave>", self.on_mouse_leave)
        
        # RGB info label under canvas
        self.rgb_info_label = tk.Label(parent, text="Hover over image to see RGB values", 
                                       font=("Arial", 11, "bold"), bg='white', fg='blue')
        self.rgb_info_label.pack(pady=5)
    
    def setup_right_panel(self, parent):
        # Title
        title_label = tk.Label(parent, text="RGB Matrix Data", font=("Arial", 14, "bold"), 
                               bg='lightgray')
        title_label.pack(pady=10)
        
        # Search frame
        search_frame = tk.LabelFrame(parent, text="Search Coordinate", 
                                     font=("Arial", 11, "bold"), bg='lightgray', padx=10, pady=10)
        search_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # X coordinate
        x_frame = tk.Frame(search_frame, bg='lightgray')
        x_frame.pack(fill=tk.X, pady=5)
        tk.Label(x_frame, text="X:", font=("Arial", 10), bg='lightgray', width=5).pack(side=tk.LEFT)
        self.x_entry = tk.Entry(x_frame, font=("Arial", 10), width=10)
        self.x_entry.pack(side=tk.LEFT, padx=5)
        
        # Y coordinate
        y_frame = tk.Frame(search_frame, bg='lightgray')
        y_frame.pack(fill=tk.X, pady=5)
        tk.Label(y_frame, text="Y:", font=("Arial", 10), bg='lightgray', width=5).pack(side=tk.LEFT)
        self.y_entry = tk.Entry(y_frame, font=("Arial", 10), width=10)
        self.y_entry.pack(side=tk.LEFT, padx=5)
        
        # Search button
        search_btn = tk.Button(search_frame, text="🔍 Search", command=self.search_coordinate,
                              font=("Arial", 10), bg='#2196F3', fg='white', cursor='hand2')
        search_btn.pack(pady=10)
        
        # Result label
        self.search_result_label = tk.Label(search_frame, text="", 
                                            font=("Arial", 10, "bold"), bg='lightgray', fg='green')
        self.search_result_label.pack(pady=5)
        
        # Separator
        ttk.Separator(parent, orient='horizontal').pack(fill=tk.X, padx=10, pady=10)
        
        # Matrix table frame
        table_frame = tk.LabelFrame(parent, text="RGB Matrix Table", 
                                    font=("Arial", 11, "bold"), bg='lightgray', padx=5, pady=5)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Table with scrollbars
        table_scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)
        table_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        
        table_scroll_x = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        table_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Treeview for table - dynamic columns will be created later
        self.tree = ttk.Treeview(table_frame, 
                                 show='tree headings',
                                 yscrollcommand=table_scroll_y.set,
                                 xscrollcommand=table_scroll_x.set,
                                 height=20)
        
        table_scroll_y.config(command=self.tree.yview)
        table_scroll_x.config(command=self.tree.xview)
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Export buttons
        export_frame = tk.Frame(parent, bg='lightgray')
        export_frame.pack(fill=tk.X, padx=10, pady=10)
        
        export_csv_list_btn = tk.Button(export_frame, text="💾 CSV (List)", 
                                        command=self.export_to_csv_list,
                                        font=("Arial", 9), bg='#FF9800', fg='white', cursor='hand2')
        export_csv_list_btn.pack(side=tk.LEFT, padx=3)
        
        export_csv_matrix_btn = tk.Button(export_frame, text="📋 CSV (Matrix)", 
                                          command=self.export_to_csv_matrix,
                                          font=("Arial", 9), bg='#FF5722', fg='white', cursor='hand2')
        export_csv_matrix_btn.pack(side=tk.LEFT, padx=3)
        
        export_excel_btn = tk.Button(export_frame, text="📊 Excel", 
                                     command=self.export_to_excel,
                                     font=("Arial", 9), bg='#4CAF50', fg='white', cursor='hand2')
        export_excel_btn.pack(side=tk.LEFT, padx=3)
    
    def upload_image(self):
        """Upload and display image"""
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff"), 
                      ("All files", "*.*")]
        )
        
        if file_path:
            try:
                # Load image
                self.original_image = Image.open(file_path)
                self.image = self.original_image.copy()
                
                # Convert to RGB if needed
                if self.image.mode != 'RGB':
                    self.image = self.image.convert('RGB')
                
                # Get image array
                self.image_array = np.array(self.image)
                
                # Update info
                width, height = self.image.size
                self.info_label.config(text=f"Size: {width}x{height} pixels")
                
                # Display image
                self.display_image()
                
                # Populate table
                self.populate_table()
                
                messagebox.showinfo("Success", "Image loaded successfully!")
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {str(e)}")
    
    def display_image(self):
        """Display image on canvas"""
        if self.image:
            # Resize for display if too large
            display_image = self.image.copy()
            width, height = display_image.size
            
            # Limit size for display
            max_size = 600
            if width > max_size or height > max_size:
                ratio = min(max_size/width, max_size/height)
                new_width = int(width * ratio)
                new_height = int(height * ratio)
                display_image = display_image.resize((new_width, new_height), Image.LANCZOS)
            
            self.photo = ImageTk.PhotoImage(display_image)
            self.canvas.config(scrollregion=(0, 0, display_image.width, display_image.height))
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
    
    def on_mouse_move(self, event):
        """Show RGB values on mouse hover"""
        if self.image_array is None:
            return
        
        # Get canvas coordinates
        canvas_x = self.canvas.canvasx(event.x)
        canvas_y = self.canvas.canvasy(event.y)
        
        # Convert to image coordinates
        width, height = self.image.size
        display_width = self.photo.width() if self.photo else width
        display_height = self.photo.height() if self.photo else height
        
        scale_x = width / display_width
        scale_y = height / display_height
        
        img_x = int(canvas_x * scale_x)
        img_y = int(canvas_y * scale_y)
        
        # Check bounds
        if 0 <= img_x < width and 0 <= img_y < height:
            r, g, b = self.image_array[img_y, img_x]
            rgb_hex = f"#{r:02X}{g:02X}{b:02X}"
            self.rgb_info_label.config(
                text=f"Position: ({img_x}, {img_y}) | RGB: ({r}, {g}, {b}) | Hex: {rgb_hex}",
                fg='blue'
            )
        else:
            self.rgb_info_label.config(text="Hover over image to see RGB values", fg='gray')
    
    def on_mouse_leave(self, event):
        """Reset info label when mouse leaves canvas"""
        self.rgb_info_label.config(text="Hover over image to see RGB values", fg='gray')
    
    def populate_table(self):
        """Populate table with RGB matrix data in X/Y format"""
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        if self.image_array is None:
            return
        
        height, width, _ = self.image_array.shape
        
        # No limit - display all coordinates
        # Create columns: X/Y header + X coordinates
        columns = ["X/Y"] + [str(x) for x in range(width)]
        
        self.tree["columns"] = columns
        self.tree.column("#0", width=0, stretch=tk.NO)  # Hide tree column
        
        # Configure column headers
        self.tree.heading("X/Y", text="X/Y")
        self.tree.column("X/Y", width=60, anchor='center')
        
        for col in columns[1:]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor='center')
        
        # Show loading message for large images
        if width * height > 10000:
            self.info_label.config(text=f"Loading table: {width}x{height} pixels... Please wait...")
            self.root.update()
        
        # Populate rows (Y coordinates)
        for y in range(height):
            row_values = [str(y)]  # Y coordinate as first column
            
            for x in range(width):
                r, g, b = self.image_array[y, x]
                rgb_str = f"({r},{g},{b})"
                row_values.append(rgb_str)
            
            self.tree.insert("", tk.END, values=row_values)
        
        # Update info label
        self.info_label.config(text=f"Size: {width}x{height} pixels | Table: {width} cols x {height} rows")
    
    def search_coordinate(self):
        """Search for specific coordinate and show RGB values"""
        try:
            x = int(self.x_entry.get())
            y = int(self.y_entry.get())
            
            if self.image_array is None:
                messagebox.showwarning("Warning", "Please load an image first!")
                return
            
            height, width, _ = self.image_array.shape
            
            if 0 <= x < width and 0 <= y < height:
                r, g, b = self.image_array[y, x]
                rgb_hex = f"#{r:02X}{g:02X}{b:02X}"
                
                self.search_result_label.config(
                    text=f"Found: RGB({r}, {g}, {b})\nHex: {rgb_hex}",
                    fg='green'
                )
                
                # Highlight in table
                try:
                    # Find the row with this Y value
                    children = self.tree.get_children()
                    if y < len(children):
                        item = children[y]
                        self.tree.selection_set(item)
                        self.tree.see(item)
                        
                        # Scroll horizontally to show the X column
                        self.tree.xview_moveto(x / width if width > 0 else 0)
                except Exception as e:
                    pass  # Could not highlight in table
                
            else:
                self.search_result_label.config(
                    text=f"Coordinate out of bounds!\nImage size: {width}x{height}",
                    fg='red'
                )
                
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integer coordinates!")
    
    def export_to_csv_list(self):
        """Export RGB matrix to CSV in list format (X, Y, R, G, B, RGB_Hex)"""
        if self.image_array is None:
            messagebox.showwarning("Warning", "Please load an image first!")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            title="Export to CSV (List Format)"
        )
        
        if file_path:
            try:
                height, width, _ = self.image_array.shape
                data = []
                
                for y in range(height):
                    for x in range(width):
                        r, g, b = self.image_array[y, x]
                        rgb_hex = f"#{r:02X}{g:02X}{b:02X}"
                        data.append([x, y, r, g, b, rgb_hex])
                
                df = pd.DataFrame(data, columns=["X", "Y", "R", "G", "B", "RGB_Hex"])
                df.to_csv(file_path, index=False)
                
                messagebox.showinfo("Success", f"Data exported to {file_path}\nFormat: List (X, Y, R, G, B, RGB_Hex)")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export: {str(e)}")
    
    def export_to_csv_matrix(self):
        """Export RGB matrix to CSV in matrix format (X/Y grid with RGB tuples)"""
        if self.image_array is None:
            messagebox.showwarning("Warning", "Please load an image first!")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            title="Export to CSV (Matrix Format)"
        )
        
        if file_path:
            try:
                height, width, _ = self.image_array.shape
                
                # Create matrix data
                # First row: headers (X/Y, 0, 1, 2, ...)
                headers = ["X/Y"] + [str(x) for x in range(width)]
                
                # Data rows: Y coordinate + RGB tuples for each X
                data = []
                for y in range(height):
                    row = [str(y)]  # Y coordinate as first column
                    for x in range(width):
                        r, g, b = self.image_array[y, x]
                        rgb_str = f"({r},{g},{b})"
                        row.append(rgb_str)
                    data.append(row)
                
                # Create DataFrame and export
                df = pd.DataFrame(data, columns=headers)
                df.to_csv(file_path, index=False)
                
                messagebox.showinfo("Success", 
                                  f"Data exported to {file_path}\n"
                                  f"Format: Matrix ({width} columns x {height} rows)\n"
                                  f"Cell format: (R,G,B)")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export: {str(e)}")
    
    def export_to_excel(self):
        """Export RGB matrix to Excel"""
        if self.image_array is None:
            messagebox.showwarning("Warning", "Please load an image first!")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                height, width, _ = self.image_array.shape
                data = []
                
                for y in range(height):
                    for x in range(width):
                        r, g, b = self.image_array[y, x]
                        rgb_hex = f"#{r:02X}{g:02X}{b:02X}"
                        data.append([x, y, r, g, b, rgb_hex])
                
                df = pd.DataFrame(data, columns=["X", "Y", "R", "G", "B", "RGB_Hex"])
                df.to_excel(file_path, index=False, engine='openpyxl')
                
                messagebox.showinfo("Success", f"Data exported to {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export: {str(e)}")


def main():
    root = tk.Tk()
    app = ImageToRGBMatrix(root)
    root.mainloop()


if __name__ == "__main__":
    main()
