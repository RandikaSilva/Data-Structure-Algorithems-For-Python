import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-delete-page',
  templateUrl: './delete-page.component.html',
  styleUrls: ['./delete-page.component.css']
})
export class DeletePageComponent implements OnInit {

  station = true
  stationList:any = []

  constructor(private api: ApiService) {
  }

  ngOnInit() {
    this.fillStationList()
  }

  fillStationList() {
    this.api.getAllStationNames().subscribe((result) => {
      if (result['status'] != false) {
        this.stationList = result['data']
      }
    })
  }

  deleteStationConnection(stationName, nextStation) {
    if (this.stationList.includes(stationName) && this.stationList.includes(nextStation)) {
      this.api.deleteStationConnection(stationName, nextStation).subscribe((result) => {
        if(result['status']!=false){
          alert("Station deleted")
          this.fillStationList()
        }else{
          alert(result['message'])
        }
      })
    } else {
      alert("Invalid station selected.\n Please try again")
    }
  }

  deleteStation(stationName) {
    if (this.stationList.includes(stationName)) {
      this.api.deleteStation(stationName).subscribe((result) => {
        if(result['status']!=false){
          alert("Station connection deleted")
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
