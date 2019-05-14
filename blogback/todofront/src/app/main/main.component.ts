import { Component, OnInit } from '@angular/core';
import { ITaskList, ITask, IPost } from '../models/models';
import { ProviderService } from '../services/provider.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public tasks: IPost[] = [];
  public task: IPost;
  public isTaskListUpdate: boolean = false;
  public isTaskUpdate: boolean = false;
  public taskListId: number = 0;
  public taskId: number = 0;

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getPost().then(res => {
      this.taskLists = res;
    })
  }

  // TaskList
  setTaskListUpdate(id: number) {
    this.taskListId = id;
    this.isTaskListUpdate = true;
  }
  setTaskListCreate() {
    this.isTaskListUpdate = false;
  }
  
  performTaskListRequest(name: string) {
    if(this.isTaskListUpdate) {
      this.updateTaskList(name);
    } else {
      this.createTaskList(name);
    }
  }

  createTaskList(name: string) {
    this.provider.createTaskList(name).then(res => {
      this.taskLists.push(res);
      console.log(res);
    })
  }
  updateTaskList(name: string) {
    this.provider.updateTaskList(this.taskListId, name).then(res => {
      console.log(res);
    })
  }
  deleteTaskList(id: number) {
    this.provider.deleteTaskList(id).then(res => {
      console.log(res);
    })
  }

  // Task
  setTaskCreate(id: number) {
    this.taskListId = id;
    this.isTaskUpdate = false;
  }
  setTaskUpdate(id: number, task_list: number) {
    this.taskId = id;
    this.taskListId = task_list;
    this.isTaskUpdate = true;
  }
  performTaskRequest(name: string, created_at: string, due_on: string, status: string) {
    if(this.isTaskUpdate) {
      this.updateTask(name, created_at, due_on, status);
    } else {
      this.createTask(name, created_at, due_on, status);
    }
  }
  getTask(task: ITask) {
    this.provider.getTaskDetails(task).then(res => {
      this.task = res;
      console.log(this.task);
    })
  }
  getTasks(taskId: number) {
    this.provider.getTaskListTasks(taskId).then(res => {
      this.tasks = res;
    })
  }
  createTask(name: string, created_at: string, due_on: string, status: string) {
    this.provider.createTask(this.taskListId, name, created_at, due_on, status).then(res => {
      this.tasks.push(res);
      console.log(res);
    })
  }
  updateTask(name: string, created_at: string, due_on: string, status: string) {
    this.provider.updateTask(this.taskId, name, created_at, due_on, status, this.taskListId).then(res => {
      console.log(res);
    })
  }
  deleteTask(id: number) {
    this.provider.deleteTask(id).then(res => {
      console.log(res);
    })
  }
}
