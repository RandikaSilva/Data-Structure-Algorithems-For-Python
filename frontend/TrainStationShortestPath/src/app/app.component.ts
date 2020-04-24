import { Component, OnInit } from '@angular/core';
import { ApiService } from './services/api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'TrainStationShortestPath';
  mode = "Loading"

  constructor(private api: ApiService) {
  }
  ngOnInit(): void {
    this.getMode()
    // setInterval(()=>{
    //   this.getMode()
    // },2000)
  }

  getMode() {
    this.api.getMode().subscribe((result) => {
      console.log(result)
      if (result['status'] == true) {
        let data = result['data']
        if (data == "0" || data == 0) {
          this.mode = "Dictionary"
        } else if (data == "1" || data == 1) {
          this.mode = "Linked List"
        } else if (data == "2" || data == 2) {
          this.mode = "Adjacency Matrix"
        }
      }
    })
  }

  changeMode(value) {
    if (value == "0") {
      this.api.changeMode(value).subscribe((result) => {
        if (result['status'] == true) {
          this.getMode()
        } else {
          alert("Unable to change mode")
        }
      })
    } else if (value == "1") {
      this.api.changeMode(value).subscribe((result) => {
        if (result['status'] == true) {
          this.getMode()
        } else {
          alert("Unable to change mode")
        }
      })
    } else if (value == "2") {
      this.api.changeMode(value).subscribe((result) => {
        if (result['status'] == true) {
          this.getMode()
        } else {
          alert("Unable to change mode")
        }
      })
    }
  }

  resetCache() {
    this.api.resetCache().subscribe((result) => {
      if (result["status"] == true) {
        alert("Cache reseted")
      } else {
        alert("Unabled to reset cache")
      }
    })
  }

  loadCache() {
    this.api.loadCache().subscribe((result) => {
      if (result["status"] == true) {
        alert("Cache loaded")
      } else if (result["status"] == false) {
        alert(result["message"])
      } else {
        alert("Unabled to load cache")
      }
    })
  }
}
