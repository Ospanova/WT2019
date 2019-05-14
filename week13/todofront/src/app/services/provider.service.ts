import { Injectable } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';
import { ITaskList, ITask, IAuthResponse } from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  private baseUrl = 'http://127.0.0.1:8000/api';

  constructor(http: HttpClient) {
    super(http);
   }

  // GET
  getTaskLists(): Promise<ITaskList[]> {
    return this.get(this.baseUrl + '/task_lists/', {});
  }
  getTaskListTasks(taskId: number): Promise<ITask[]> {
    return this.get(this.baseUrl + '/task_lists/'+ taskId +'/tasks/', {})
  }
  getTaskDetails(task: ITask): Promise<ITask> {
    return this.get(this.baseUrl + '/tasks/'+ task.id +'/', {})
  }
  // POST
  auth(username: any, password: any): Promise<IAuthResponse> {
    return this.post(this.baseUrl + '/login/', {
      username: username,
      password: password
    })
  }
  logout(): Promise<any> {
    return this.post(this.baseUrl + '/logout/', {})
  }
  createTask(id: number, name: any, created_at: any, due_on: any, status: any): Promise<ITask> {
    return this.post(this.baseUrl + '/task_lists/' + id + '/tasks/', {
      name: name,
      created_at: created_at,
      due_on: due_on,
      status: status,
      task_list: id
    })
  }
  createTaskList(name: any): Promise<ITaskList> {
    return this.post(this.baseUrl + '/task_lists/', {
      name: name
    })
  }
  // PUT
  updateTask(id: number, name: any, created_at: any, due_on: any, status: any, task_list: number): Promise<ITask> {
    return this.put(this.baseUrl + '/tasks/' + id + '/', {
      name: name,
      created_at: created_at,
      due_on: due_on,
      status: status,
      task_list: task_list
    })
  }
  updateTaskList(id: number, name: any): Promise<ITaskList> {
    return this.put(this.baseUrl + '/task_lists/' + id + '/', {
      name: name
    })
  }
  // DELETE
  deleteTask(id: number): Promise<any> {
    return this.delete(this.baseUrl + '/tasks/' + id + '/', {});
  }
  deleteTaskList(id: number): Promise<any> {
    return this.delete(this.baseUrl + '/task_lists/' + id + '/', {});
  }
}
