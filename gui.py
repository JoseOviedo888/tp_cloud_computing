import tkinter as tk
from tkinter import messagebox
from tasks import add_task, remove_task, complete_task, get_tasks
from storage import save_tasks, load_tasks

tasks = load_tasks()

def update_task_list(listbox):
    listbox.delete(0, tk.END)
    for idx, task in enumerate(get_tasks(tasks)):
        status = "✅" if task['completed'] else "❌"
        listbox.insert(tk.END, f"{idx+1}. {task['title']} {status}")

def run_app():
    def on_add():
        title = entry.get()
        if not title:
            messagebox.showwarning("Campo vacío", "La tarea no puede estar vacía.")
            return
        add_task(tasks, title)
        save_tasks(tasks)
        update_task_list(listbox)
        entry.delete(0, tk.END)

    def on_remove():
        sel = listbox.curselection()
        if not sel:
            return
        index = sel[0]
        remove_task(tasks, index)
        save_tasks(tasks)
        update_task_list(listbox)

    def on_complete():
        sel = listbox.curselection()
        if not sel:
            return
        index = sel[0]
        complete_task(tasks, index)
        save_tasks(tasks)
        update_task_list(listbox)

    window = tk.Tk()
    window.title("Gestor de Tareas")

    entry = tk.Entry(window, width=40)
    entry.pack(pady=10)

    listbox = tk.Listbox(window, width=50)
    listbox.pack()

    update_task_list(listbox)

    tk.Button(window, text="Agregar Tarea", command=on_add).pack(pady=2)
    tk.Button(window, text="Marcar como Completada", command=on_complete).pack(pady=2)
    tk.Button(window, text="Eliminar Tarea", command=on_remove).pack(pady=2)

    window.mainloop()
