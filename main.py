import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import PRIMARY, SECONDARY, SUCCESS, INFO, WARNING, DANGER
from tkinter.constants import LEFT, RIGHT, TOP, BOTTOM, BOTH, X, Y, YES, HORIZONTAL, VERTICAL
from PIL import Image, ImageTk
import pandas as pd
import numpy as np


class ImageToRGBMatrix:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to RGB Matrix Converter")
        self.root.geometry("1400x900")
        
        # Variables
        self.image = None
        self.photo = None
        self.image_array = None
        self.original_image = None
        self.zoom_scale = 1.0
        
        # Create main container with better styling
        main_container = ttk.PanedWindow(root, orient=HORIZONTAL, bootstyle=INFO)
        main_container.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        # Left panel - Image display
        left_frame = ttk.Frame(main_container, padding=10)
        main_container.add(left_frame, weight=1)
        
        # Right panel - Controls and data
        right_frame = ttk.Frame(main_container, padding=10)
        main_container.add(right_frame, weight=1)
        
        self.setup_left_panel(left_frame)
        self.setup_right_panel(right_frame)
    
    def setup_left_panel(self, parent):
        # Title with modern styling
        title_label = ttk.Label(parent, text="📷 Image Display", 
                               font=("Segoe UI", 16, "bold"), 
                               bootstyle=PRIMARY)
        title_label.pack(pady=(0, 15))
        
        # Upload button with modern styling
        upload_btn = ttk.Button(parent, text="📁 Upload Image", 
                               command=self.upload_image, 
                               bootstyle=SUCCESS,
                               width=20)
        upload_btn.pack(pady=10)
        
        # Image info label with better styling
        self.info_label = ttk.Label(parent, text="No image loaded", 
                                   font=("Segoe UI", 10), 
                                   bootstyle=SECONDARY)
        self.info_label.pack(pady=5)
        
        # Canvas frame with modern styling
        canvas_frame = ttk.Frame(parent, relief="solid", borderwidth=1)
        canvas_frame.pack(fill=BOTH, expand=YES, padx=5, pady=10)
        
        # Scrollbars with modern styling
        h_scrollbar = ttk.Scrollbar(canvas_frame, orient=HORIZONTAL, bootstyle=INFO)
        h_scrollbar.pack(side=BOTTOM, fill=X)
        
        v_scrollbar = ttk.Scrollbar(canvas_frame, orient=VERTICAL, bootstyle=INFO)
        v_scrollbar.pack(side=RIGHT, fill=Y)
        
        # Canvas
        self.canvas = tk.Canvas(canvas_frame, bg='#f8f9fa', 
                                xscrollcommand=h_scrollbar.set,
                                yscrollcommand=v_scrollbar.set,
                                highlightthickness=0)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=YES)
        
        h_scrollbar.config(command=self.canvas.xview)
        v_scrollbar.config(command=self.canvas.yview)
        
        # Bind mouse events
        self.canvas.bind("<Motion>", self.on_mouse_move)
        self.canvas.bind("<Leave>", self.on_mouse_leave)
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        
        # RGB info label under canvas with modern styling
        self.rgb_info_label = ttk.Label(parent, 
                                       text="Hover over image to see RGB values", 
                                       font=("Segoe UI", 10, "bold"), 
                                       bootstyle=INFO)
        self.rgb_info_label.pack(pady=10)
    
    def setup_right_panel(self, parent):
        # Title with modern styling
        title_label = ttk.Label(parent, text="📊 RGB Matrix Data", 
                               font=("Segoe UI", 16, "bold"), 
                               bootstyle=PRIMARY)
        title_label.pack(pady=(0, 15))
        
        # Search frame with modern styling
        search_frame = ttk.Labelframe(parent, text="🔍 Search Coordinate", 
                                     padding=15, bootstyle=INFO)
        search_frame.pack(fill=X, padx=5, pady=(0, 10))
        
        # Coordinate input frame
        coord_frame = ttk.Frame(search_frame)
        coord_frame.pack(fill=X, pady=5)
        
        # X coordinate
        x_frame = ttk.Frame(coord_frame)
        x_frame.pack(side=LEFT, padx=5, expand=YES, fill=X)
        ttk.Label(x_frame, text="X:", font=("Segoe UI", 10), width=3).pack(side=LEFT, padx=(0, 5))
        self.x_entry = ttk.Entry(x_frame, font=("Segoe UI", 10), width=12)
        self.x_entry.pack(side=LEFT, fill=X, expand=YES)
        
        # Y coordinate
        y_frame = ttk.Frame(coord_frame)
        y_frame.pack(side=LEFT, padx=5, expand=YES, fill=X)
        ttk.Label(y_frame, text="Y:", font=("Segoe UI", 10), width=3).pack(side=LEFT, padx=(0, 5))
        self.y_entry = ttk.Entry(y_frame, font=("Segoe UI", 10), width=12)
        self.y_entry.pack(side=LEFT, fill=X, expand=YES)
        
        # Search button with modern styling
        search_btn = ttk.Button(search_frame, text="🔍 Search", 
                               command=self.search_coordinate,
                               bootstyle=INFO,
                               width=15)
        search_btn.pack(pady=10)
        
        # Result label with modern styling
        self.search_result_label = ttk.Label(search_frame, text="", 
                                            font=("Segoe UI", 10, "bold"), 
                                            bootstyle=SUCCESS)
        self.search_result_label.pack(pady=5)
        
        # Separator with modern styling
        ttk.Separator(parent, orient=HORIZONTAL, bootstyle=INFO).pack(fill=X, padx=5, pady=15)
        
        # Matrix table frame with modern styling
        table_frame = ttk.Labelframe(parent, text="📋 RGB Matrix Table", 
                                    padding=10, bootstyle=PRIMARY)
        table_frame.pack(fill=BOTH, expand=YES, padx=5, pady=(0, 10))
        
        # Table with modern scrollbars
        table_scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL, bootstyle=INFO)
        table_scroll_y.pack(side=RIGHT, fill=Y)
        
        table_scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL, bootstyle=INFO)
        table_scroll_x.pack(side=BOTTOM, fill=X)
        
        # Treeview for table with modern styling
        self.tree = ttk.Treeview(table_frame, 
                                 show='tree headings',
                                 yscrollcommand=table_scroll_y.set,
                                 xscrollcommand=table_scroll_x.set,
                                 height=20,
                                 bootstyle=INFO)
        
        table_scroll_y.config(command=self.tree.yview)
        table_scroll_x.config(command=self.tree.xview)
        
        self.tree.pack(fill=BOTH, expand=YES)
        
        # Export buttons with modern styling
        export_label = ttk.Label(parent, text="Export Options:", 
                                font=("Segoe UI", 11, "bold"), 
                                bootstyle=SECONDARY)
        export_label.pack(pady=(5, 10))
        
        export_frame = ttk.Frame(parent)
        export_frame.pack(fill=X, padx=5, pady=(0, 10))
        
        export_csv_list_btn = ttk.Button(export_frame, text="💾 CSV (List)", 
                                        command=self.export_to_csv_list,
                                        bootstyle=WARNING,
                                        width=15)
        export_csv_list_btn.pack(side=LEFT, padx=5, expand=YES, fill=X)
        
        export_csv_matrix_btn = ttk.Button(export_frame, text="📋 CSV (Matrix)", 
                                          command=self.export_to_csv_matrix,
                                          bootstyle=DANGER,
                                          width=15)
        export_csv_matrix_btn.pack(side=LEFT, padx=5, expand=YES, fill=X)
        
        export_excel_btn = ttk.Button(export_frame, text="📊 Excel", 
                                     command=self.export_to_excel,
                                     bootstyle=SUCCESS,
                                     width=15)
        export_excel_btn.pack(side=LEFT, padx=5, expand=YES, fill=X)
    
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
                text=f"📍 Position: ({img_x}, {img_y}) | RGB: ({r}, {g}, {b}) | Hex: {rgb_hex}",
                bootstyle=INFO
            )
        else:
            self.rgb_info_label.config(
                text="Hover over image to see RGB values", 
                bootstyle=SECONDARY
            )
    
    def on_mouse_leave(self, event):
        """Reset info label when mouse leaves canvas"""
        self.rgb_info_label.config(
            text="Hover over image to see RGB values", 
            bootstyle=SECONDARY
        )
    
    def on_canvas_click(self, event):
        """Show RGB Matrix Table when image is clicked"""
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
            self.show_rgb_matrix_window(img_x, img_y)
    
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
                    text=f"✓ Found: RGB({r}, {g}, {b})\nHex: {rgb_hex}",
                    bootstyle=SUCCESS
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
                    text=f"⚠ Coordinate out of bounds!\nImage size: {width}x{height}",
                    bootstyle=DANGER
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
    
    def show_rgb_matrix_window(self, center_x, center_y):
        """Show popup window with RGB matrix table around clicked position"""
        # Create popup window with modern styling
        popup = ttk.Toplevel(self.root)
        popup.title(f"📊 RGB Matrix Table at ({center_x}, {center_y})")
        popup.geometry("900x650")
        
        # Info label with modern styling
        height, width, _ = self.image_array.shape
        r, g, b = self.image_array[center_y, center_x]
        rgb_hex = f"#{r:02X}{g:02X}{b:02X}"
        
        info_frame = ttk.Frame(popup, padding=15, bootstyle=INFO)
        info_frame.pack(fill=X, padx=10, pady=10)
        
        info_text = (f"📍 Clicked Position: ({center_x}, {center_y})\n"
                    f"🎨 RGB: ({r}, {g}, {b}) | Hex: {rgb_hex}\n"
                    f"🔍 Showing surrounding pixels (7x7 grid)")
        
        ttk.Label(info_frame, text=info_text, font=("Segoe UI", 11, "bold"), 
                 bootstyle=PRIMARY, justify=LEFT).pack()
        
        # Define matrix range (show 7x7 grid centered on clicked position)
        matrix_size = 7
        half_size = matrix_size // 2
        
        start_x = max(0, center_x - half_size)
        end_x = min(width, center_x + half_size + 1)
        start_y = max(0, center_y - half_size)
        end_y = min(height, center_y + half_size + 1)
        
        # Create frame for table with modern styling
        table_frame = ttk.Frame(popup)
        table_frame.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        
        # Scrollbars with modern styling
        table_scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL, bootstyle=INFO)
        table_scroll_y.pack(side=RIGHT, fill=Y)
        
        table_scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL, bootstyle=INFO)
        table_scroll_x.pack(side=BOTTOM, fill=X)
        
        # Create Treeview with modern styling
        columns = ["X/Y"] + [str(x) for x in range(start_x, end_x)]
        
        tree = ttk.Treeview(table_frame, 
                           show='tree headings',
                           yscrollcommand=table_scroll_y.set,
                           xscrollcommand=table_scroll_x.set,
                           height=15,
                           bootstyle=INFO)
        
        table_scroll_y.config(command=tree.yview)
        table_scroll_x.config(command=tree.xview)
        
        tree.pack(fill=BOTH, expand=YES)
        
        tree["columns"] = columns
        tree.column("#0", width=0, stretch=tk.NO)
        
        # Configure headers
        tree.heading("X/Y", text="X/Y")
        tree.column("X/Y", width=60, anchor='center')
        
        for col in columns[1:]:
            tree.heading(col, text=col)
            tree.column(col, width=120, anchor='center')
        
        # Populate table
        for y in range(start_y, end_y):
            row_values = [str(y)]
            
            for x in range(start_x, end_x):
                r, g, b = self.image_array[y, x]
                rgb_str = f"({r},{g},{b})"
                
                # Highlight the clicked pixel
                if x == center_x and y == center_y:
                    rgb_str = f"★ {rgb_str} ★"
                
                row_values.append(rgb_str)
            
            # Insert row with tag for clicked position
            if y == center_y:
                tree.insert("", tk.END, values=row_values, tags=('clicked',))
            else:
                tree.insert("", tk.END, values=row_values)
        
        # Configure tag for clicked row
        tree.tag_configure('clicked', background='yellow')
        
        # Export button for this matrix with modern styling
        export_btn_frame = ttk.Frame(popup, padding=10)
        export_btn_frame.pack(fill=X, padx=10, pady=10)
        
        def export_this_matrix():
            """Export this specific matrix region to CSV"""
            file_path = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                title=f"Export Matrix at ({center_x}, {center_y})"
            )
            
            if file_path:
                try:
                    # Create matrix data
                    headers = ["X/Y"] + [str(x) for x in range(start_x, end_x)]
                    data = []
                    
                    for y in range(start_y, end_y):
                        row = [str(y)]
                        for x in range(start_x, end_x):
                            r, g, b = self.image_array[y, x]
                            rgb_str = f"({r},{g},{b})"
                            if x == center_x and y == center_y:
                                rgb_str = f"[CLICKED] {rgb_str}"
                            row.append(rgb_str)
                        data.append(row)
                    
                    df = pd.DataFrame(data, columns=headers)
                    df.to_csv(file_path, index=False)
                    
                    messagebox.showinfo("Success", f"✓ Matrix exported to {file_path}")
                except Exception as e:
                    messagebox.showerror("Error", f"✗ Failed to export: {str(e)}")
        
        ttk.Button(export_btn_frame, text="💾 Export This Matrix to CSV", 
                 command=export_this_matrix,
                 bootstyle=SUCCESS,
                 width=25).pack(side=LEFT, padx=5)
        
        ttk.Button(export_btn_frame, text="❌ Close", 
                 command=popup.destroy,
                 bootstyle=DANGER,
                 width=12).pack(side=RIGHT, padx=5)


def main():
    # Create modern themed window with ttkbootstrap
    root = ttk.Window(themename="cosmo")  # Modern, clean theme
    app = ImageToRGBMatrix(root)
    root.mainloop()


if __name__ == "__main__":
    main()
