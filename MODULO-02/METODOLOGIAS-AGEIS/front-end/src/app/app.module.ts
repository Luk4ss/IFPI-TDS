import { NgModule, LOCALE_ID } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HeaderComponent } from './components/template/header/header.component';

import {MatToolbarModule} from '@angular/material/toolbar';
import { FooterComponent } from './components/template/footer/footer.component';
import { NavComponent } from './components/template/nav/nav.component';

import{ HttpClientModule} from '@angular/common/http';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { MatSidenavModule} from '@angular/material/sidenav';
import { MatCardModule} from '@angular/material/card';
import { MatButtonModule} from '@angular/material/button';
import { MatListModule} from '@angular/material/list';
import { HomeComponent } from './views/home/home.component';
import { ProductCrudComponent } from './views/product-crud/product-crud.component';
import { ProductCreateComponent } from './components/product/product-create/product-create.component';
import { FormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { ProductListComponent } from './components/product/product-list/product-list.component';
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatSortModule } from '@angular/material/sort';
import localePt from '@angular/common/locales/pt';
import { registerLocaleData } from '@angular/common';
import { ProductUpdateComponent } from './components/product/product-update/product-update.component';
import { ProductDeleteComponent } from './components/product/product-delete/product-delete.component';
import { PetListComponent } from './components/pet/pet-list/pet-list.component';
import { PetCrudComponent } from './views/pet-crud/pet-crud.component';
import { PetCreateComponent } from './components/pet/pet-create/pet-create.component';
import { PetUpdateComponent } from './components/pet/pet-update/pet-update.component';
import { PetDeleteComponent } from './components/pet/pet-delete/pet-delete.component';
import { LoginComponent } from './components/login/login.component';
import { AcaoListComponent } from './components/acao/acao-list/acao-list.component';
import { AcaoCrudComponent } from './views/acao-crud/acao-crud.component';
import { AcaoCreateComponent } from './components/acao/acao-create/acao-create.component';
import {MatRadioModule} from '@angular/material/radio';

registerLocaleData(localePt);


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    NavComponent,
    HomeComponent,
    ProductCrudComponent,
    ProductCreateComponent,
    ProductListComponent,
    ProductUpdateComponent,
    ProductDeleteComponent,
    PetListComponent,
    PetCrudComponent,
    PetCreateComponent,
    PetUpdateComponent,
    PetDeleteComponent,
    LoginComponent,
    AcaoListComponent,
    AcaoCrudComponent,
    AcaoCreateComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    MatSidenavModule,
    MatListModule,
    MatCardModule,
    MatButtonModule,
    MatSnackBarModule,
    HttpClientModule,
    FormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatTableModule,
    MatPaginatorModule,
    MatSortModule,
    MatRadioModule
  ],
  providers: [{
    provide: LOCALE_ID,
    useValue: 'pt-BR'
  }],
  bootstrap: [AppComponent]
})
export class AppModule { }
