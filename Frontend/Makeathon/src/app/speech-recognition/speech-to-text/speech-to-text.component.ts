import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { VoiceRecognitionService } from '../service/voice-recognition.service';

interface SpeechConfigInterface {
  plant_ID: number;
  timestamp: string;
  sensordata_temp: number;
  sensordata_humidity: number;
}

interface RobotDriving{
  isInAction: boolean;
}

@Component({
  selector: 'app-speech-to-text',
  templateUrl: './speech-to-text.component.html',
  styleUrls: ['./speech-to-text.component.css']
})
export class SpeechToTextComponent implements OnInit {
  public plantInfo: any;
  text: string = 'Init';
  speechConfigInterface: SpeechConfigInterface;
  robotIsActive: boolean = false;

  constructor(
    public service : VoiceRecognitionService,
    private http: HttpClient
  ){
    this.service.init()
   }

  ngOnInit(): void {
    // ##### TEST Request #####
    // const url: string = 'assets/config.json';
    // this.http.get(url,{observe: 'body', responseType: 'json'}).subscribe((response) => {
    //   let obj: any = JSON.parse(JSON.stringify(response));
    //   console.log("HttpRequest ID:" + obj.plant_ID);
    //   console.log("HttpRequest Humidity:" + obj.sensordata_humidity);
    // })

    this.service.currentApprovalStageMessage.subscribe(msg => {
      this.text = msg;
      this.startHttpRequest(this.text);
    });
  }

  startService() {
    this.service.start();
  }

  startHttpRequest(text: string){
    text = text.replace(/\s/g, "");
    text = "howismyplantone";
    console.log("Text vor dem Request: |" + text + "|");

    this.isRobotActive();
      
    if(!this.robotIsActive){
      if(text === "howismyplantone"){
        this.http.get('http://192.168.0.110:5000/drive/1',
          {observe: 'body', responseType: 'json'}).subscribe(response => {
            let obj: any = JSON.parse(JSON.stringify(response));
            console.log("HttpRequest ID:" + obj.plant_ID);
            console.log("HttpRequest Humidity:" + obj.sensordata_humidity);
          })
      }
      else{
        console.log("kein richtiger Befehl");
      }
    }
    else{
      if(text === ''){
        //TODO Aufnehmen
        console.log("Aufnehmen!");
      }
      else if(text === 'givemethelatestmeasurementsforplantone'){
        this.http.get('http://192.168.0.102:5000/data/1',
        {observe: 'body', responseType: 'json'}).subscribe(response => {
          let obj: any = JSON.parse(JSON.stringify(response));
          console.log("HttpRequest ID:" + obj.plant_ID);
          console.log("HttpRequest Humidity:" + obj.sensordata_humidity);
          //TODO werte zuweisen an UI
        })
      }      
      }  
  }

  isRobotActive(){
    this.http.get('http://192.168.0.110:5000/drive/status',
    {observe: 'body', responseType: 'json'}).subscribe(response => {
      let obj: any = JSON.parse(JSON.stringify(response));
      this.robotIsActive = obj.available;
      console.log("Robot is in action: "+ this.robotIsActive);})
  }

}