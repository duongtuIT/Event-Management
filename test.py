import tkinter as tk

def draw_horizontal_line(event):
    canvas.delete("all")  # Xóa đường cũ
    canvas.create_line(0, event.height // 2, event.width, event.height // 2, fill="blue", width=2)

root = tk.Tk()
root.title("Đường kẻ ngang động")
root.geometry("400x300")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

# Vẽ đường khi kích thước cửa sổ thay đổi
canvas.bind("<Configure>", draw_horizontal_line)

root.mainloop()
