import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-minimum-connectors',
  templateUrl: './minimum-connectors.component.html',
  styleUrls: ['./minimum-connectors.component.css']
})
export class MinimumConnectorsComponent implements OnInit {
  station = true;
  stationList:any = [];
  AddedList:any = [];
  final_path: any=[];
  total_distance;
  directed_connnections:any=[];
  constructor(private api: ApiService) {
  }

  ngOnInit() {
    this.fillStationList()
  }

  fillStationList() {
    this.api.getAllStationNames().subscribe((result) => {

      console.log(result)
      if (result['status'] !== false) {
        this.stationList = result['data']
      }
    })
  }

  AddStation(stationName){
    console.log(stationName);
    if(this.AddedList.includes(stationName)||stationName==""){
        alert("Already Added");
    }
    else{
      this.AddedList.push(stationName);
      console.log(this.AddedList);
    }
  }
  toggleMode() {
    this.station = !this.station
  }
  View(){
    console.log("No");
    this.api.getMinimumConnectors(this.AddedList).subscribe((result) => {
      console.log(result)
      if (result['status'] == true && result['code'] == 101) {
        if (confirm(result['message'])) {
           this.final_path = result['data']['final_path'];
           this.total_distance = result['data']['total_distance'];
           console.log(result['data']['final_path']);
           console.log(result['data']['total_distance']);
        }
      }
      else if (result['status'] == true && result['code'] == 100){
        if (confirm(result['message'])) {
          this.directed_connnections = result['data']['directed_connections'];
          this.final_path = result['data']['final_path'];
          this.total_distance = result['data']['total_distance'];
          console.log("Data");
          console.log(result['data']['total_distance']);
           console.log(result['data']['final_path']);
       }else{
        this.final_path = result['data']['total_distance'];
       }
      }
      console.log("ok");
    })
  }
}
