import { Injectable } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';
import {IPost} from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  private baseUrl = 'http://127.0.0.1:8000/api';

  constructor(http: HttpClient) {
    super(http);
   }


   getPosts(): Promise<IPost[]> {
     return this.get(this.baseUrl + '/post/', {})
   } 
  getPost(taskId: number): Promise<IPost[]> {
    return this.get(this.baseUrl + '/post/' + taskId + '/', {})
  }
  
  // POST
  createPost(id: number, name: any, created_at: any, due_on: any, status: any): Promise<IPost> {
    return this.post(this.baseUrl + '/post/' + id + '/', {
      name: name,
      created_at: created_at,
      due_on: due_on,
      status: status,
      task_list: id
    })
  }
  // PUT
  updatePost(id: number, name: any, created_at: any, due_on: any, status: any, task_list: number): Promise<IPost> {
    return this.put(this.baseUrl + '/post/' + id + '/', {
      name: name,
      created_at: created_at,
      due_on: due_on,
      status: status,
      task_list: task_list
    })
  }
  
  // DELETE
  deleteTask(id: number): Promise<any> {
    return this.delete(this.baseUrl + '/post/' + id + '/', {});
  }
 
}
