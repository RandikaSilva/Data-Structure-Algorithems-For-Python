import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SearchPageComponent } from './search-page/search-page.component';
import { InsertPageComponent } from './insert-page/insert-page.component';
import { UpdatePageComponent } from './update-page/update-page.component';
import { DeletePageComponent } from './delete-page/delete-page.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { ViewPageComponent } from './view-page/view-page.component';
import { CommonModule } from '@angular/common';
import { MinimumConnectorsComponent } from './minimum-connectors/minimum-connectors.component';

@NgModule({
  declarations: [
    AppComponent,
    SearchPageComponent,
    InsertPageComponent,
    UpdatePageComponent,
    DeletePageComponent,
    ViewPageComponent,
    MinimumConnectorsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    CommonModule
  ],
  providers: [
    HttpClient
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
