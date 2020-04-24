import { Component, OnInit, AfterViewInit } from '@angular/core';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-view-page',
  templateUrl: './view-page.component.html',
  styleUrls: ['./view-page.component.css']
})
export class ViewPageComponent implements AfterViewInit {

  stationConnections=[]
  stations=[]
  station=true

  constructor(private api:ApiService) { }

  ngAfterViewInit() {
    this.getAllStationNames()
    this.getAllConnections()
  }

  toggleMode() {
    this.station = !this.station
    this.getAllStationNames()
    this.getAllConnections()
  }

  reload(){
    if(this.station==true){
      this.api.getAllStationNames().subscribe((result) => {
        if (result['status'] != false) {
          this.stations=[]
          this.stations = result['data']
          alert("Reloaded")
        }else{
          alert("Unable to reload")
        }
      })
    }else if(this.station==false){
      this.api.getAllConnections().subscribe((result)=>{
        if (result['status'] != false) {
          this.stationConnections=[]
          this.stationConnections=result['data']
          alert("Reloaded")
        }else{
          alert("Unable to reload")
        }
      })
    }
  }
  getAllConnections(){
    this.api.getAllConnections().subscribe((result)=>{
      if (result['status'] != false) {
        this.stationConnections=[]
        this.stationConnections=result['data']
      }else{
        alert("Unable to load data")
      }
    })
  }
  getAllStationNames(){
    this.api.getAllStationNames().subscribe((result) => {
      if (result['status'] != false) {
        this.stations=[]
        this.stations = result['data']
      }else{
        alert("Unable to load data")
      }
    })
  }
}
