import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SearchPageComponent } from './search-page/search-page.component';
import { InsertPageComponent } from './insert-page/insert-page.component';
import { DeletePageComponent } from './delete-page/delete-page.component';
import { UpdatePageComponent } from './update-page/update-page.component';
import { ViewPageComponent } from './view-page/view-page.component';
import { format } from 'url';
import { MinimumConnectorsComponent } from './minimum-connectors/minimum-connectors.component';


const routes: Routes = [
  {
    path: 'search',
    component: SearchPageComponent
  },
  {
    path: 'insert',
    component: InsertPageComponent
  },
  {
    path: 'delete',
    component: DeletePageComponent
  },
  {
    path: 'update',
    component: UpdatePageComponent
  },
  {
    path: 'view',
    component: ViewPageComponent
  },
  {
    path: 'Minimun',
    component: MinimumConnectorsComponent
  },
  {
    path: '',
    component: SearchPageComponent
  },

];

@NgModule({
  imports: [RouterModule.forRoot(routes, { useHash: true })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
