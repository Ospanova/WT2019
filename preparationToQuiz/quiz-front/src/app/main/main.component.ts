import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import { IContact } from '../shared/models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {

  public contacts: IContact[] = [];
  public name : any = '';
  public phone: any = '';
  public loading = false;
  public isLogged = false;
  public login = '';
  public password = '';
  public currentId = -1;

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.isLogged = true;
    }

    if (this.isLogged) {
      this.provider.getContacts().then(res => {
        this.contacts = res;
        setTimeout(() => {
          this.loading = true;
        }, 2000);
      });
    }
  }

  showContactDetails(contact: IContact) {
    this.currentId = contact.id;
  }

  createContact() {
    if (this.name !== '' && this.phone !== '') {
      this.provider.createContact(this.name , this.phone).then(res => {
        this.name = '';
        this.phone = '';
        this.contacts.push(res);
      });
    }
  }
  deleteContact(post: IContact) {
    this.provider.deleteContact(post.id).then(res => {
      this.provider.getContacts().then(r => {
        this.contacts = r;
      });
    });
  }

  auth() {
    if (this.login !== '' && this.password !== '') {
      this.provider.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);
        this.isLogged = true;
        // this.getCategories();
        this.provider.getContacts().then(r => {
          this.contacts = r;
          setTimeout(() => {
            this.loading = true;
          }, 2000);
        });
      });
    }
  }

  logout() {
    this.provider.logout().then(res => {
      localStorage.clear();
      this.isLogged = false;
    });
  }

}
