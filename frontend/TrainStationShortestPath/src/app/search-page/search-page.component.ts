import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-search-page',
  templateUrl: './search-page.component.html',
  styleUrls: ['./search-page.component.css']
})
export class SearchPageComponent implements OnInit {

  stationList:any = []
  distance =0;
  connection: any=[];

  constructor(private api:ApiService) {
    this.fillStationList()
  }

  ngOnInit() {
  }

  fillStationList(){
    this.api.getAllStationNames().subscribe((result)=>{
      console.log(result)
      if(result['status']!=false){
        this.stationList=result['data']
      }
    })
  }

  seachPath(start,destination){
    if(this.stationList.includes(start)==true&&this.stationList.includes(destination)==true){
      this.api.searchShortestPath(start,destination).subscribe((result)=>{
        console.log(result)
        if(result['status']!=false){
          this.connection = result['data']['shortest_path'];
          this.distance = result['data']['distance'];
          console.log(this.distance)
        }else{
          alert(result['message'])
        }
      })
    }else{
      alert("Invalid station selected.\n Please try again")
    }
  }

}
