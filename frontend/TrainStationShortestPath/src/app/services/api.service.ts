import { Injectable } from '@angular/core'
import { HttpClient, HttpHeaders } from "@angular/common/http"

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  apiBaseUrlLive = "https://pdsanibm.herokuapp.com/api/"
  //apiBaseUrlLive = "localhost:5000/api/"

  constructor(private http: HttpClient) {
  }

  searchShortestPath(start, end) {
    try {
      return this.http.post(
        this.apiBaseUrlLive + "navigate",
        {
          start: start,
          end: end
        }
      )
    } catch {
      throw "Error"
    }
  }
  updateStation(old_station_name, station_name) {
    try {
      return this.http.post(
        this.apiBaseUrlLive + "update/station",
        {
          old_station_name: old_station_name,
          station_name: station_name
        }
      )
    } catch {
      throw "Error"
    }
  }
  updateStationConnection(station_name, next_station, distance) {
    try {
      return this.http.post(
        this.apiBaseUrlLive + "update/station_connection",
        {
          station_name: station_name,
          next_station: next_station,
          distance: distance
        }
      )
    } catch {
      throw "Error"
    }
  }
  deleteStation(station_name) {
    try {
      return this.http.post(
        this.apiBaseUrlLive + "delete/station",
        {
          station_name: station_name
        }
      )
    } catch {
      throw "Error"
    }
  }
  deleteStationConnection(station_name, next_station) {
    try {
      return this.http.post(
        this.apiBaseUrlLive + "delete/station_connection",
        {
          station_name: station_name,
          next_station: next_station
        }
      )
    } catch {
      throw "Error"
    }
  }
  addStation(station_name) {
    try {
      return this.http.post(
        this.apiBaseUrlLive + "add/station",
        {
          station_name: station_name
        }
      )
    } catch {
      throw "Error"
    }
  }
  addStationConnection(station_name, next_station, distance) {
    try {
      return this.http.post(
        this.apiBaseUrlLive + "add/station_connector",
        {
          station_name: station_name,
          next_station: next_station,
          distance: distance
        }
      )
    } catch {
      throw "Error"
    }
  }
  getAllStationNames() {
    try {
      return this.http.get(
        this.apiBaseUrlLive + "get/all_stations"
      )
    } catch {
      throw "Error"
    }
  }
  resetCache() {
    try {
      return this.http.get(
        this.apiBaseUrlLive + "reset_cache"
      )
    } catch {
      throw "Error"
    }
  }
  loadCache() {
    try {
      return this.http.get(
        this.apiBaseUrlLive + "load_data"
      )
    } catch {
      throw "Error"
    }
  }
  changeMode(mode) {
    try {
      return this.http.post(
        this.apiBaseUrlLive + "mode/change",
        {
          mode: mode.toString()
        }
      )
    } catch {
      throw "Error"
    }
  }
  getMode(){
    try {
      return this.http.get(
        this.apiBaseUrlLive + "mode/get"
      )
    } catch {
      throw "Error"
    }
  }
  getAllConnections(){
    try {
      return this.http.get(
        this.apiBaseUrlLive + "get/all_stations_connections"
      )
    } catch {
      throw "Error"
    }
  }
}
