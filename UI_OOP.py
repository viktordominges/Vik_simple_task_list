# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 11:10:51 2023

@author: vikto
"""

import flet as ft
import tkinter as tk

class TaskApp(ft.UserControl):
    
    def build(self):
        self.textField = ft.TextField(width=380, )
        self.addBtn = ft.FloatingActionButton(icon = ft.icons.ADD, on_click=self.addClick)
        self.tasks = ft.Column()
        taskRow = ft.Column(controls=[ft.Row(alignment = ft.MainAxisAlignment.SPACE_BETWEEN, 
                                                 controls=[self.textField, self.addBtn]), self.tasks])
        return taskRow
        
    def addClick(self, e):
        task = Task(self.textField.value, self.taskDelete)
        self.tasks.controls.append(task)
        self.textField.value = ''
        self.update()
        
    def taskDelete(self, task):
        self.tasks.controls.remove(task)
        self.update()
    
class Task(ft.UserControl):
    
    def __init__(self, taskName, taskDelete):
        super().__init__()
        self.taskName = taskName
        self.taskDelete = taskDelete
        
    def build(self):
        self.displayTask = ft.Checkbox(label=self.taskName, value=False)
        self.editName = ft.TextField()
        
        self.displayView = ft.Row(alignment = ft.MainAxisAlignment.SPACE_BETWEEN, controls=[self.displayTask, 
                                            ft.Row(controls=[ft.IconButton(ft.icons.CREATE_OUTLINED, on_click=self.editClick),
                                                             ft.IconButton(ft.icons.DELETE_OUTLINED, on_click=self.deleteClick)])])
        
        self.editView = ft.Row(alignment = ft.MainAxisAlignment.SPACE_BETWEEN, visible=False, controls = [self.editName, 
                                                          ft.IconButton(ft.icons.DONE_OUTLINED, on_click=self.saveClick)])

        
        return ft.Column(controls=[self.displayView, self.editView])
                               
    def editClick(self, e):
        self.displayView.visible = False
        self.editView.visible = True
        self.editName.value = self.displayTask.label
        self.update()
    
    def saveClick(self, e):
        self.displayView.visible = True
        self.editView.visible = False
        self.displayTask.label = self.editName.value
        self.update()
    
    def deleteClick(self, e):
        self.taskDelete(self)
    

def main(page: ft.page):
    
    page.title = 'Tasking App by Vik'
    page.window_width = 500
    page.window_hight = 800
    page.bgcolor = '#5D534A'
    
    taskingApp = TaskApp()
    page.add(taskingApp)
    
ft.app(target=main)