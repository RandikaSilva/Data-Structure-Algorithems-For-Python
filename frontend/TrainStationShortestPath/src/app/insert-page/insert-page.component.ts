import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-insert-page',
  templateUrl: './insert-page.component.html',
  styleUrls: ['./insert-page.component.css']
})
export class InsertPageComponent implements OnInit {

  station = true
  stationList: any = []

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

  insertStationConnection(stationName, nextStation, distance) {
    if (this.stationList.includes(stationName) && this.stationList.includes(nextStation)) {
      if (distance != undefined && distance != null) {
        this.api.addStationConnection(stationName, nextStation, distance).subscribe((result) => {
          if (result['status'] != false) {
            alert("Station connection inserted")
            this.fillStationList()
          } else {
            alert(result['message'])
          }
        })
      }else{
        alert("Invalid data")
      }
    } else {
      alert("Invalid station selected.\n Please try again")
    }
  }

  insertStation(stationName) {
    this.api.addStation(stationName).subscribe((result) => {
      if (result['status'] != false) {
        alert("Station inserted")
        this.fillStationList()
      } else {
        alert(result['message'])
      }
    })
  }

  toggleMode() {
    this.station = !this.station
  }

}
