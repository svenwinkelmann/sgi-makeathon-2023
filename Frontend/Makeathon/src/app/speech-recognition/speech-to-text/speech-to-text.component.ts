import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { map, Subscription, timer } from 'rxjs';
import { VoiceRecognitionService } from '../service/voice-recognition.service';

interface Plant {
  measurement_id: number,
  plant_id: number,
  timestamp: string,
  sensordata_temp: number,
  sensordata_humidity: number,
  sensordata_ground_humidity: number,
  pest_infestation: number,
  light_intensity: number
}

@Component({
  selector: 'app-speech-to-text',
  templateUrl: './speech-to-text.component.html',
  styleUrls: ['./speech-to-text.component.css']
})
export class SpeechToTextComponent implements OnInit {
  text: string = 'Init';
  robotIsReady: boolean;
  timerSubscription: Subscription;
  plants: Plant[] = [{ "measurement_id": 0, "plant_id": 0, "sensordata_humidity": 0, "sensordata_temp": 0, "timestamp": "", "sensordata_ground_humidity": 0, "pest_infestation": 0, "light_intensity": 0 },
  { "measurement_id": 0, "plant_id": 0, "sensordata_humidity": 0, "sensordata_temp": 0, "timestamp": "", "sensordata_ground_humidity": 0, "pest_infestation": 0, "light_intensity": 0 },
  { "measurement_id": 0, "plant_id": 0, "sensordata_humidity": 0, "sensordata_temp": 0, "timestamp": "", "sensordata_ground_humidity": 0, "pest_infestation": 0, "light_intensity": 0 },
  { "measurement_id": 0, "plant_id": 0, "sensordata_humidity": 0, "sensordata_temp": 0, "timestamp": "", "sensordata_ground_humidity": 0, "pest_infestation": 0, "light_intensity": 0 },
  { "measurement_id": 0, "plant_id": 0, "sensordata_humidity": 0, "sensordata_temp": 0, "timestamp": "", "sensordata_ground_humidity": 0, "pest_infestation": 0, "light_intensity": 0 },
  { "measurement_id": 0, "plant_id": 0, "sensordata_humidity": 0, "sensordata_temp": 0, "timestamp": "", "sensordata_ground_humidity": 0, "pest_infestation": 0, "light_intensity": 0 }];


  constructor(
    public service: VoiceRecognitionService,
    private http: HttpClient
  ) {
    this.service.init()
  }

  ngOnInit(): void {
    // ##### TEST Request #####
    // const url: string = 'assets/config.json';
    // this.http.get(url, { observe: 'body', responseType: 'json' }).subscribe((response) => {
    //   let obj: any = JSON.parse(JSON.stringify(response));
    //   this.isRobotActive = obj.statusRobot;
    //   for (let i = 0; i < 6; i++) {
    //     this.plants[i].measurement_id = obj.plants[i].measurement_id;
    //     this.plants[i].plant_id = obj.plants[i].plant_id;
    //     this.plants[i].timestamp = obj.plants[i].timestamp;
    //     this.plants[i].sensordata_temp = obj.plants[i].sensordata_temp;
    //     this.plants[i].sensordata_humidity = obj.plants[i].sensordata_humidity;
    //     this.plants[i].sensordata_ground_humidity = obj.plants[i].sensordata_ground_humidity;
    //     this.plants[i].pest_infestation = obj.plants[i].pest_infestation;
    //   }
    // })
    this.robotIsReady = true;
    this.timerSubscription = timer(0, 1000).pipe(
      map(() => {
        this.getAllData(); // load data contains the http request 
      })
    ).subscribe();

    this.service.currentApprovalStageMessage.subscribe(msg => {
      this.text = msg;
      if (this.text !== 'BehaviorSubject')
        this.startHttpRequest(this.text);
    });
  }

  startService() {
    this.service.start();
  }

  startHttpRequest(text: string) {
    text = text.replace(/\s/g, "");
    text = "drivetotheplantone";
    console.log("Text vor dem Request: |" + text + "|");

    if (true) {
      if (text === "drivetotheplants") {
        this.sendRobotToMeasurePlants();
      }
      else if (text === "drivetotheplantone") {
        this.sendRobotToMeasurePlantOne();
      }
      else {
        console.log("kein richtiger Befehl");
      }
    }
    else {
      if (text === '') {
        //TODO Aufnehmen
        console.log("Aufnehmen!");
      }
      else {
        //TODOOO
      }
    }
  }

  getAllData() {
    this.http.get('http://192.168.0.110:5000/data',
      { observe: 'body', responseType: 'json' }).subscribe(response => {
        let obj: any = JSON.parse(JSON.stringify(response));
        this.robotIsReady = obj.robot_status;
        for (let i = 0; i < 6; i++) {
          this.plants[i].measurement_id = obj.plants[i].measurement_id;
          this.plants[i].plant_id = obj.plants[i].plant_id;
          this.plants[i].timestamp = obj.plants[i].timestamp;
          this.plants[i].sensordata_temp = obj.plants[i].sensordata_temp;
          this.plants[i].sensordata_humidity = obj.plants[i].sensordata_humidity;
          this.plants[i].sensordata_ground_humidity = obj.plants[i].sensordata_ground_humidity;
          this.plants[i].pest_infestation = obj.plants[i].pest_infestation;
          this.plants[i].light_intensity = obj.plants[i].light_intensity;
        }
      })
  }

  // TODO IN POST !!
  sendRobotToMeasurePlants() {
    this.http.get('http://192.168.0.110:5000/drive',
      { observe: 'body', responseType: 'json' }).subscribe(response => {
        console.log(response);
      });

  }

  // TODO IN POST !!
  sendRobotToMeasurePlantOne() {
    this.http.get('http://192.168.0.110:5000/drive/1',
      { observe: 'body', responseType: 'json' }).subscribe(response => {
        console.log(response);
      });
  }

  isRobotReady() {
    return this.robotIsReady;
  }

}