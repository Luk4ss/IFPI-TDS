import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AcaoCreateComponent } from './components/acao/acao-create/acao-create.component';
import { AcaoListComponent } from './components/acao/acao-list/acao-list.component';
import { LoginComponent } from './components/login/login.component';
import { PetCreateComponent } from './components/pet/pet-create/pet-create.component';
import { PetDeleteComponent } from './components/pet/pet-delete/pet-delete.component';
import { PetListComponent } from './components/pet/pet-list/pet-list.component';
import { PetUpdateComponent } from './components/pet/pet-update/pet-update.component';
import { ProductCreateComponent } from './components/product/product-create/product-create.component';
import { ProductDeleteComponent } from './components/product/product-delete/product-delete.component';
import { ProductListComponent } from './components/product/product-list/product-list.component';
import { ProductUpdateComponent } from './components/product/product-update/product-update.component';
import { AcaoCrudComponent } from './views/acao-crud/acao-crud.component';
import { HomeComponent } from './views/home/home.component';
import { PetCrudComponent } from './views/pet-crud/pet-crud.component';
import { ProductCrudComponent } from './views/product-crud/product-crud.component';

const routes: Routes = [
  {
    path: "", 
  component: HomeComponent
  },
  {
    path:"products",
    component: ProductCrudComponent,
    children:[
      {
        path: "",
        component: ProductListComponent
      },
      {
        path:"create",
        component: ProductCreateComponent
      },
      {
        path:"update/:id",
        component: ProductUpdateComponent
      },
      {
        path:"delete/:id",
        component: ProductDeleteComponent
      },

    ]
  },
  {
    path:"pets",
    component: PetCrudComponent,
    children:[
      {
        path:"",
        component: PetListComponent
      },
      {
        path: "create",
        component: PetCreateComponent
      },
      {
        path: "update/:id",
        component: PetUpdateComponent
      },
      {
        path: "delete/:id",
        component: PetDeleteComponent
      }
    ]
  },
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: 'acoes',
    component: AcaoCrudComponent,
    children:[
      {
        path: "",
        component: AcaoListComponent
      },
      {
        path: "create",
        component: AcaoCreateComponent
      }
    ]    
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
