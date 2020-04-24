import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-update-page',
  templateUrl: './update-page.component.html',
  styleUrls: ['./update-page.component.css']
})
export class UpdatePageComponent implements OnInit {

  station = true
  stationList:any = []

  constructor(private api: ApiService) {
  }

  ngOnInit() {
    this.fillStationList()
  }

  fillStationList() {
    this.api.getAllStationNames().subscribe((result) => {
      console.log(result)
      if (result['status'] != false) {
        this.stationList = result['data']
      }
    })
  }

  updateStationConnection(stationName, nextStation, distance) {
    if (this.stationList.includes(stationName) && this.stationList.includes(nextStation)) {
      if (distance != undefined && distance != null) {
        this.api.updateStationConnection(stationName, nextStation, distance).subscribe((result) => {
          if(result['status']!=false){
            alert("Station connection updated")
            this.fillStationList()
          }else{
            alert(result['message'])
          }
        })
      }
    } else {
      alert("Invalid station selected.\n Please try again")
    }
  }

  updateStation(oldStationName,stationName) {
    if (this.stationList.includes(oldStationName)) {
      this.api.updateStation(oldStationName,stationName).subscribe((result) => {
        if(result['status']!=false){
          alert("Station updated")
          this.fillStationList()
        }else{
          alert(result['message'])
        }
      })
    } else {
      alert("Invalid station selected.\n Please try again")
    }
  }

  toggleMode() {
    this.station = !this.station
  }
}
